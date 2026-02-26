import requests
from bs4 import BeautifulSoup
from datetime import timedelta,date
import feedparser
from htmldate import find_date

def get_Malpedia_data():
    url = 'https://malpedia.caad.fkie.fraunhofer.de/feeds/rss/latest'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=15) #30 days
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        try:
            # Get the link and date of the entry
            title_string = entry.link
            page = requests.get(title_string)
            soup = BeautifulSoup(page.content, 'html.parser')
            link = soup.find('a',class_='btn btn-logo-red')
            title_string = link['href']
            date_string = find_date(title_string)
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))   
        except:
            pass                
    return results

