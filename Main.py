# Headers
from Parser import ioc_url_get
from Extractor import get_Malpedia_data
import urllib.parse
import json

threat_url = get_Malpedia_data()
feeds=[]
for data in threat_url:
    feeds.append(data)
    print("Found article :",data)
print("Total articles found :",len(feeds))

if feeds:
    with open("feeds.txt", 'w') as file:
        for feed in feeds:
            file.write(feed + "\n")

for feed in feeds:
    try:
        response=ioc_url_get(feed)
        print(f"Processing feed: {feed} - Status: {response['status']}")
        if response["status"]=="success":
            parsed = urllib.parse.urlparse(feed)
            path_parts = parsed.path.strip('/').split('/')
            campaign = path_parts[-1]
            SHA256=response["data"]["FILE_HASH_SHA256"]
            SHA1=response["data"]["FILE_HASH_SHA1"]
            MD5=response["data"]["FILE_HASH_MD5"]
            with open(f"IOCs/{campaign}.json", 'w') as file:
                json.dump({
                    "SHA256": SHA256,
                    "SHA1": SHA1,
                    "MD5": MD5
                }, file, indent=4)

    except Exception as e:
        print(f"Error processing feed {feed}: {e}")
        pass
