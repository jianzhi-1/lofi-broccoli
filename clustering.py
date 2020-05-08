import urllib
import urllib.parse
import urllib.request
import os
import math
import datetime
import shutil
from bs4 import BeautifulSoup
from pytube import YouTube
import re

class LofiMiner():
    def __init__(self):
        self.searchlimit = 5

    def from_url(self, videourl):
        youtube = YouTube(videourl)
        youtube.streams.filter(file_extension = "mp4")
        youtube.streams.get_by_itag(18).download()
        print("Video downloaded\n")

    def from_search(self, searchtext, limit = 10, length_limit = 300):

        query_string = urllib.parse.urlencode({"search_query" : searchtext})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

        #print(search_results)
        #print("http://www.youtube.com/watch?v=" + search_results[0])
        counter = 0
        for i in search_results:
            if (counter >= limit):
                break
            url = "http://www.youtube.com/watch?v=" + search_results[counter]
            print("http://www.youtube.com/watch?v=" + search_results[counter])
            try:
                youtube = YouTube(url)
            except:
                counter = counter + 1
                continue
            counter = counter + 1
            print(youtube.title)
            print(youtube.rating)
            print(youtube.length)
            if (youtube.length < length_limit):
                youtube.streams.filter(file_extension = "mp4")
                youtube.streams.get_by_itag(18).download()
                print("Video downloaded\n")
            #print(dir(youtube))
            #print(youtube.title)
            #print(youtube.player_response)


dm = LofiMiner()
#dm.from_url("https://www.youtube.com/watch?v=Lxvpj28upPY")
dm.from_search("lofi")
