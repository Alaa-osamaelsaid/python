from time import sleep
import requests
import webbrowser

# boredapi provides data that actviates every 2 sec
#while True:
  #URL=requests.get("https://www.boredapi.com/api/activity")
  #data= URL.json()["activity"]
  #print(data)
  #sleep(2)
#################################################################

#get my ip address and print it in text
url= requests.get("https://api.ipify.org/?format=json")
print(url.text)
#{"ip":"156.215.177.156"}

#to get the location
#loc= webbrowser.open_new_tab("https://ipinfo.io/156.215.177.156/geo")
loc= requests.get("https://ipinfo.io/156.215.177.156/geo")
print(loc.json())