# Headers
from Parser import ioc_url_get
import csv
from Extractor import get_Malpedia_data

if __name__ == "__main__":
  threat_url = get_Malpedia_data()
  response=ioc_url_get(threat_url)
  if response["status"]=="success":
    FILE_HASH_SHA256=response["data"]["FILE_HASH_SHA256"]
    FILE_HASH_SHA1=response["data"]["FILE_HASH_SHA1"]
    FILE_HASH_MD5=response["data"]["FILE_HASH_MD5"]
    if FILE_HASH_SHA256:
        with open("IOCs/FILE_SHA256.txt", 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(FILE_HASH_SHA256)

    if FILE_HASH_SHA1:
        with open("IOCs/FILE_SHA1.txt", "w") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(FILE_HASH_SHA1)

    if FILE_HASH_MD5:
        with open("IOCs/FILE_MD5.txt", "w") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(FILE_HASH_MD5)
