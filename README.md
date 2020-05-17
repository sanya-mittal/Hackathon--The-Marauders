# Hackathon--The-Marauders


**Problem statement:** ETL happens to be an everyday process actually breaked out in three individual steps at Clients end. 


**Solution:**  How about an ability to do it in a single go?  
 Here is our implementation to achieve this in single go using  Webhook functionality on CleverTap dashboard. Webhook endpoint  is configured such a way, that as soon as the request triggers, endpoint in turn adds all the changes and hit back the data to CleverTap API's , completing a loop of Export transform and load in a single functionality. 


<br />

 **What needs to be done on CleverTap dashboard:** 
 
<br />
A Webhook Campaign has been streamed using custom KV's containing some predefined parameters in the script.We Would be fetching the account details  in webhook under which we be loading the data, be it same or different account. Setup is done such a way that we can either raise an event or profile properties or both. 

<br />

*Screenshot inline:*

<br />

![Campaign creation](https://firebasestorage.googleapis.com/v0/b/zeke-160bc.appspot.com/o/image%20(5).png?alt=media&token=ced47398-fb02-4754-94b1-d222e5d150ed)

![API pushed data back in the profile](https://firebasestorage.googleapis.com/v0/b/zeke-160bc.appspot.com/o/image%20(4).png?alt=media&token=12288aec-ed64-4aca-8755-659bfa340b40)


**Expected Output :** Once the campaign has been scheduled, you would be able to get the data in realtime or PBS, configure the data to be raised, and load it back to CleverTap. A whole process of Export transform and load would be catered under one ready to go script. 

**Use Cases Across Verticals:** Be it a better segmentation requirement or updating the data in real-time, every other use-case can be easily achievable. Some of the common use cases are listed in the Presentation. 


 **Upcoming Enhancements :**
 <br />

Given this our first try on the implementation, looking forward to following enhancements in near future.

__ Currently the script has hardcoded the details which needs to be loaded back to the account as an event or user property as soon as the request arrives. An attempt to role out making these data be completely dynamic would be the next achievement. 

__ We return the responses for success ingestion via API. Addition to it,  We would be Handling all the errors, be it around payload, or any outage which may in turn if fails the upload via API's, this would explicitly let the end user know in case of any breakout and the reason behind it. 

__ Making the process more scalable to raise 3 concurrent threads as what we currently accept in API calls .

<br />

**Sample expected Payload**

Payload received at your endpoint

```
{ "targetId" : 1589621729 , "key_values" : { "target_account" : "W44-Z4K-K65Z" , "target_passcode" : "IAA-ZAB-GEKL" , "profile_upload" : "yes" , "event_upload" : "yes"} , "profiles" : [ { "key_values" : { "target_account" : "W44-Z4K-K65Z" , "target_passcode" : "IAA-ZAB-GEKL" , "profile_upload" : "yes" , "event_upload" : "yes"} , "email" : "yash+567@clevertap.com" , "identity" : "1234" , "all_identities" : [ "1234" , "yash+123456@clevertap.com" , "yash+567@clevertap.com"] , "objectId" : "__189f188bf9394c0da3d219ea4959a785" , "profileData" : { "city" : "Mumbai" , "evtname" : "CSV upload event test" , "apitest" : 23 , "datetest" : "$D_1589290950" , "itp" : "1" , "test" : "1233"} , "name" : "Yash TEST" , "push_token" : "fcm:eBtus6A0RpKfL-HPuUzrlp:APA91bFiq_suxBi3eS5nMR7i3JfmvyLP4QURtXHZqZXyrc_iYq_VDfkipJcB5srObRbniQWVgmT6nvyyd8oqfDmi96Iwefnn-eN1Dp6wUmtItQEjLnPVV97SUMNDrlIFOTC4SPrJV7HC" , "event_properties" : { "Event Prop Name" : "Property value" , "CT App Version" : "2.2" , "CT Source" : "Mobile"}}]}
```

**Payload goes back to CleverTap**

<br />
*Profile Data*
<br />

```
{'d':[{'objectId':'__189f188bf9394c0da3d219ea4959a785','type':'profile','profileData':{'city': 'Mumbai', 'evtname': 'CSV upload event test', 'apitest': 23, 'datetest': '$D_1589290950', 'itp': '1', 'test': '1233'}}]}
```


*Events*
<br />
```
{ 'd': [ { 'objectId':'__189f188bf9394c0da3d219ea4959a785', 'type': 'event', 'evtName': 'From Webhook', 'evtData':{'Event Prop Name': 'Property value', 'CT App Version': '2.2', 'CT Source': 'Mobile'}} ] }
```
