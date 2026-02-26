# Headers
from Parser import ioc_url_get
from Extractor import get_Malpedia_data

threat_url = get_Malpedia_data()
feeds=[]
for data in threat_url:
    feeds.append(data)
    print("Found article :",data)
print("Total articles found :",len(feeds))

if feeds:
    with open("IOCs/feeds.txt", 'w') as file:
        for feed in feeds:
            file.write(feed + "\n")


import json
for feed in feeds:
    try:
        response=ioc_url_get(feed)
        print(response)
        if response["status"]=="success":
            with open(f"IOCs/{response['meta']['title']}.json", 'w') as file:
                json.dump(response, file)

    except Exception as e:
        print(f"Error processing feed {feed}: {e}")
        pass


