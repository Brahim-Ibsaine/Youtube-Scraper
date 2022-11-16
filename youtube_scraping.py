# Packages 
from bs4 import BeautifulSoup
import json
import re
import requests
import argparse
import os
import sys


class youtube_crapping :
    
    def __init__(self, url) :
        self.url = url
        self.page = requests.get(url)
        self.soup =  BeautifulSoup(self.page.content, "html.parser")  
        self.title = ""
        self.author = ""
        self.id = 0
        self.like = 0
        self.description = ""
        self.links = []
        
        
    

    # function to get title
    def get_title(self) :
        data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1) 
        self.title = data['videoDetails']['title']
        return self.title


    # function to get author
    def get_author (self) :
        data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1) 
        self.author = data['videoDetails']['author']
        return self.author

     # funtion to get id : 
    def get_id(self):
        data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1) 
        self.id = data['videoDetails']['videoId']
        return self.id

    # function to get number of likes
    def get_likes (self) :
        data_init = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)  
        data = json.loads(data_init)
        videoPrimaryInfoRenderer = data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] 
        # number of likes  
        likes = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,### likes"  
        likes_str = likes.split(' ')[0].replace(',','')  
        self.likes = '0' if likes_str == 'No' else likes_str
        return self.likes

    # function to get the description of the video 
    def get_description (self) :
        
        pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
        self.description = pattern.findall(str(soup))[0].replace('\\n','\n')
        return self.description
    
    # get links from description 
    def get_links (self) :
        links = re.findall(r'(https?://\S+)', self.description)
        links = links + re.findall(r"[0-9]+:[0-9]{2}", self.description)
        return self.links


    
    # This function return dictionnry which contains information of the video
    def scrapping_information (self) :
        dict_scrap = {}
        dict_scrap['Title'] = self.get_title()
        dict_scrap['Author'] = self.get_author()
        dict_scrap['Id'] = self.get_id()
        dict_scrap['Likes'] = self.get_likes()
        dict_scrap['Description'] = self.get_description()
        dict_scrap['Links_description'] = self.get_links()

        # return the dictionary which contains information
        return dict_scrap




# Input json file
with open("input.json", "r") as f :
    video_id = json.load(f)["videos_id"]
    
# Output json file 
output = []
for id in video_id :
    data = youtube_crapping("https://www.youtube.com/watch?v=" + id).scrapping_information()
    data['Id'] = id
    print(data)
    output.append(data)

with open("output.json", "w") as f :
    f.write(json.dumps(output, indent=4))