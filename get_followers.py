""" 
from twitter_scrape_followers import *
import time
true=True;false=False
list_of_cookies=[
{
    "domain": ".twitter.com",
    "expirationDate": 1676520136,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1110230825266.1610349768",
    "id": 1
}]
#please replace the above sample cookies with your cookies, can see below link of how to fetch cookies
twitter.login_cookie(cookies=list_of_cookies)
twitter.open("https://twitter.com/SunnyLeone/followers")
time.sleep(2)
all_data=[]
for i in range(0,2):
       response=twitter.get_followers()
       data=response['body']
       print(data)
       # all_data.extend(data)

"""

from twitter_scrape_followers import *
import time
true=True;false=False
list_of_cookies=[
{
    "domain": ".twitter.com",
    "expirationDate": 1676520136,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1110230825266.1610349768",
    "id": 1
}]
#please replace the above sample cookies with your cookies, can see below link of how to fetch cookies
twitter.login_cookie(cookies=list_of_cookies)
twitter.open("https://twitter.com/narendramodi/followers")
time.sleep(2)
response=twitter.get_followers()
data=response['body']
print(data)
#data=[{"Link": "https://twitter.com/rupeshj08678392", "Info": "Rupesh Jain"},...]