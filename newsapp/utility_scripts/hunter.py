import django
import os 
import sys
import bs4
from bs4 import BeautifulSoup
sys.path.append("C:\\Users\\Coder\\Documents\\CodeProject\\globepost")
import globepost
from globepost import settings
os.environ['DJANGO_SETTINGS_MODULE']="globepost.settings"
django.setup()
import feedparser,re
from dateutil import parser
import requests
from newsapp.models import Country, Channel, Website, Post

def go_fishing_channel_title(url,pk):
    print("Processing ",url,"..................")
    try:
        feed=feedparser.parse(url)
        channel_title=feed['feed']['title']
        mychannel=Channel.objects.get(pk=pk)
        mychannel.channel_title=channel_title
        mychannel.save()
        print("Successfully saved ",channel_title," at ",str(pk))
    except Exception as e:
        pass

def go_fishing_get_post(url):
    print("Processing ",url,"..................")
    reg=r'<img src="(?P<link1>\w+://[\w+./-]+)'
    try:
        html=requests.get(url).content
        #print(html)
        if(str(url).find("reuters.com") > 0):
            html=html.replace(b'&lt;',bytes("<","utf-8")).replace(b'&gt;',bytes(">","utf-8"))
            #print(html)
        feed=feedparser.parse(html)
        items=feed.entries
        for item in items:
            pub_date=item.published
            title=item.title
            post_url=item.links[0]['href']
            summary=item.summary
            summary= re.sub(r'[^\x00-\x7f]+','',BeautifulSoup(summary).text)    
            if(str(url).find("reuters.com") > 0):
                    summary= re.sub(r'[^\x00-\x7f]+','',BeautifulSoup(summary).text)      

            try:
                content=item.content[0].value
               
            except AttributeError as e: 
                content=summary

            

            if(str(url).find("reuters.com") > 0):
                try:
                    thumbnail=get_thumbnail2(item)
                except Exception as e:
                    print(e)
            elif(str(url).find("yahoo.com") > 0):

                thumbnail=get_yahoo_thumbnail(item)
                

            else:
                try:    
                    thumbnail=re.search(reg,content).groups('link1')[0]
                except Exception as e:
                    print(e)
                    try:
                        thumbnail=get_thumbnail(item)
                    except Exception as e:
                        thumbnail=item.thumbnail
                        #thumbnail="http://nothumbnail.com"    




            feed_url=Channel.objects.get(feed_url=url)
            Post.objects.get_or_create(pub_date=parser.parse(pub_date).date().strftime("%Y-%m-%d"),title=title,summary=summary,content=content,thumbnail=thumbnail,feed_url=feed_url,post_url=post_url)
            print("Successfully saved ")
    except Exception as e:
        print(e)

def get_thumbnail(item):
    #soup=BeautifulSoup(str(item))
    #print(soup.title)
    #url=find("media:thumbnail").attrs["url"]
    d=item.media_thumbnail
    if(len(d)>0):
        if len(d)>1:
            d2=item.media_thumbnail[1]
        else:
            d2=item.media_thumbnail[0]
        url=d2.get("url")
        return url
def get_thumbnail2(item):
    soup=BeautifulSoup(item.summary)
    url=soup.find("img").attrs["src"]
    return url

def get_yahoo_thumbnail(item):
     
    return item.media_content[0]["url"]  
    
def channel_title():
    channels=Channel.objects.all()
    for channel in channels:
        go_fishing_channel_title(channel.feed_url,channel.pk)

def get_post():
    channels=Channel.objects.all()
    for channel in channels:
        go_fishing_get_post(channel.feed_url)
 
#channel_title()   
get_post()
