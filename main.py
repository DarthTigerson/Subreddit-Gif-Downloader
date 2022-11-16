import shutil
from sys import exit
from unicodedata import name
import requests
import os
from functions_csv import csv_return_cell_data, csv_return_list_total
    

def makeUrl(afterID, subreddit):
        newUrl = subreddit.split('/.json')[0] + "/.json?after={}".format(afterID)
        return newUrl
    

def splitUrl(imageUrl):
        if 'jpg' or 'webm' or 'mp4' or 'gif' or 'gifv' or 'png' in imageUrl:
            return imageUrl.split('/')[-1]  

def os_create_directory(directory_path):
    try:
        os.mkdir(directory_path)
    except:
        print('Directory allready exists')

def downloadImage(imageUrl, imageAmount, folder): 
        os_create_directory(f'{folder}/')
        filename = splitUrl(imageUrl)
        if filename:
            r = requests.get(imageUrl, stream=True)  
            with open(f'{folder}/{filename}', 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                print("Successfully downloaded: " + imageUrl)
                imageAmount += 1
        return imageAmount


def logic(subreddit,name,limit):
    subJson = ''
    x = 0
    while x < limit:
        if subJson:
            url = makeUrl(subJson['data']['after'], subreddit)
        else:
            url = makeUrl('', subreddit)
        subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
        try:
            post = subJson['data']['children']
            postCount = range(len(post))

            for i in postCount: 
                imageUrl = (post[i]['data']['url'])
                _imageUrls = []
                _imageUrls.append(imageUrl)
                x = downloadImage(_imageUrls[0], x, name)
                if x == limit:
                    break
        except:
            print('Unable to read json')

def main():
    filePath = 'list.csv'
    downloadLimit = 100

    counter = 0
    totalCounter = csv_return_list_total(filePath)

    while counter != totalCounter:
        tempData = csv_return_cell_data(filePath,'domain',counter)
        tempName = f'r/{csv_return_cell_data(filePath,"name",counter)}'
        logic(tempData,tempName,downloadLimit)
        counter += 1

main()