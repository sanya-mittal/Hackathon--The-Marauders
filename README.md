# Hackathon--The-Marauders


**Problem statement:** ETL happens to be an everyday process actually breaked out in three individual steps at Clients end. 


**Solution:**  How about an ability to do it in a single go?  
 Here is our implementation to achieve this in single go using  Webhook functionality on CleverTap dashboard. Webhook endpoint  is configured such a way, that as soon as the request triggers, endpoint in turn adds all the changes and hit back the data to CleverTap API's , completing a loop of Export transform and load in a single functionality. 


<br />

 **What needs to be done on CleverTap dashboard:** 
 
<br />
A Webhook Campaign has been streamed using custom KV's containing some predefined parameters in the script.We Would be fetching the account details  in webhook under which we be loading the data, be it same or different account. Setup is done such a way that we can either raise an event or profile properties or both. 



*Screenshot inline:*

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
