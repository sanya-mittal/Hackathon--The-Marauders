import json
from botocore.vendored import requests


print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string params
	print(event)

	#2. Construct the body of the response object
	transactionResponse = {}

	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	webhook_req =  event['body']
	responseObject['body'] = webhook_req
	webhook_req = json.loads(webhook_req)
	print(type(webhook_req))
	
	
	
	
	
	#check if event or profile
	if (webhook_req['key_values'].get('event_upload')=="Yes" or webhook_req['key_values'].get('event_upload')=="yes"):
		iseventupload =True
	else:
		iseventupload =False
	if(webhook_req['key_values'].get('profile_upload')=="Yes" or webhook_req['key_values'].get('profile_upload')=="yes"):
		isprofileupload = True
	else:
		isprofileupload = False
		
	#Form the API request
	Acc_ID = webhook_req['key_values'].get('target_account')
	Pass_code = webhook_req['key_values'].get('target_passcode')
	headers = {
    'X-CleverTap-Account-Id': ""+str(Acc_ID)+"",
    'X-CleverTap-Passcode': ""+str(Pass_code)+"",
    'Content-Type': 'application/json'
	}
	
	#Check number of objects in the request
	len_of_object = len(webhook_req['profiles'])


	#Get the various identities... will use objId for this POC
	for i in range(0,len_of_object):
		try:
			webhook_req['profiles'][i]['email']
		except NameError:
			#Donothing
			email=""
		else:
			email = webhook_req['profiles'][i]['email']
		try:
			webhook_req['profiles'][i]['identity']
		except NameError:
			#Donothing
			identity=""
		else:
			identity = webhook_req['profiles'][i]['identity']
		try:
			webhook_req['profiles'][i]['objectId']
		except NameError:
			#donothing
			ob_id=""
		else:
			ob_id = webhook_req['profiles'][i]['objectId']

	
	#Raise events
	if iseventupload==True:
		
		evt_props = webhook_req['profiles'][i]['event_properties']
		url_evt = "https://api.clevertap.com/1/upload"
		payload_evt = '{ \'d\': [ { \'objectId\':''\''+str(ob_id)+'\', \'type\': \'event\', \'evtName\': \'From Webhook\', \'evtData\':'+str(evt_props)+'} ] }'
		response_evt = requests.request("POST", url=url_evt, data=payload_evt, headers=headers)
		print(response_evt.text)
		print(response_evt.request.body)

	#upload profile
	if isprofileupload==True:
		profile_data = webhook_req['profiles'][i]['profileData']
		url_profile = "https://api.clevertap.com/1/upload"
		payload_profile = '{\'d\':[{\'objectId\':''\''+str(ob_id)+'\',\'type\':\'profile\',\'profileData\':'+str(profile_data)+'}]}'
		response_profile = requests.request("POST", url=url_profile, data=payload_profile, headers=headers)
	
		print(response_profile.text)
		print(response_profile.request.body)
	
	#4. Return the response object
	return responseObject

	
