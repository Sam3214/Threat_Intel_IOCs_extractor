# Headers
from Parser import ioc_url_get
from Extractor import get_Malpedia_data

if __name__ == "__main__":
    threat_url = get_Malpedia_data()
    feeds=[]
    for data in threat_url:
        feeds.append(data)
        print("Found articles :",data)
    with open("IOCs/Threat_URL.txt", "w") as file:
            file.write('\n'.join(feeds) + '\n')

    response=ioc_url_get(threat_url[0])
    print(f"Extracting IOCs from the article: {threat_url[0]}")
    if response["status"]=="success":
        print("Found IOCs and extracted successfully.")
        FILE_HASH_SHA256=response["data"]["FILE_HASH_SHA256"]
        FILE_HASH_SHA1=response["data"]["FILE_HASH_SHA1"]
        FILE_HASH_MD5=response["data"]["FILE_HASH_MD5"]
        if FILE_HASH_SHA256:
            with open("IOCs/FILE_SHA256.txt", 'w') as file:
                file.write("\n".join(FILE_HASH_SHA256))

        if FILE_HASH_SHA1:
            with open("IOCs/FILE_SHA1.txt", "w") as file:
                file.write("\n".join(FILE_HASH_SHA1))

        if FILE_HASH_MD5:
            with open("IOCs/FILE_MD5.txt", "w") as file:
                file.write("\n".join(FILE_HASH_MD5))
    else:
        print("No IOCs found or an error occurred during extraction.")
