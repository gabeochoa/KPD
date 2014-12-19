import praw # reddit api
import urllib # get images from url
import os # makes directories
import time # used to rerun mainFunc every 30 sec
import requests # used to get html for BS
from bs4 import BeautifulSoup # used to parse for imgur albums
import json #used to parse gfycat links

subreddits = dict([])

def parsefile():
	f = open('config.txt', 'r')
	
	#emulating do-while
	cont = True
	strs = []
	line = ''
	while cont:
		line = f.read()
		for partial in line.split('\n'):
			if partial != '' :
				broken = partial.split("::")
				keywords = (broken[1]).split(",")
				subreddits[(broken[0]).strip()] = keywords
		else :
			cont = False
	return

def mainfunc():
	#subreddits = ['kpics', 'apink', 'girlsday', 'AceOfAngels8']
	#names = ['Bomi', 'Eunji', 'Choa', 'Jimin', 'Hyeri']

	r = praw.Reddit(user_agent='KPD by /u/gabe1118 v3.0')

	for subreddit, keywords in subreddits.items():
		if not os.path.exists(subreddit):
			os.makedirs(subreddit)
	
		submissions = r.get_subreddit(subreddit).get_new(limit=100)

		downloadAll = False
		if (keywords[0]).strip() == '*':
			#print("downloading all images")
			downloadAll = True

		for x in submissions:
			strs = str(x)
			postTitle = (strs.split("::"))[1]
			for Ina in keywords:
				Iname = Ina.strip()
				fn = subreddit+os.sep
				if not downloadAll:
					fn += Iname
				if not os.path.exists(fn):
					os.mkdir(fn)
				if postTitle.lower().find(Iname.lower()) == -1 and not downloadAll:
					continue
				else :
					savefile(subreddit, x, x.url, fn, postTitle)

def savefile(subreddit, submission, url, filename, postTitle):
	while os.sep in postTitle :
		postTitle = postTitle.replace(os.sep, '-')
	while '/' in postTitle :
		postTitle = postTitle.replace('/', '-')
	while '\\' in postTitle :
		postTitle = postTitle.replace('/', '-')
		
	#if 'imgur' in url:
		#print(url, filename)

	if '.jpg' not in url and '.png' not in url and '.gif' not in url:
		if 'http://imgur.com/a/' in url:
			# This is an album submission.
			albumId = url[len('http://imgur.com/a/'):]
			htmlSource = requests.get(url).text

			soup = BeautifulSoup(htmlSource)
			matches = soup.select('.album-view-image-link a')
			for match in matches:
				imageUrl = match['href']
				if '?' in imageUrl:
					imageFile = imageUrl[imageUrl.rfind('/') + 1:imageUrl.rfind('?')]
				else:
					imageFile = imageUrl[imageUrl.rfind('/') + 1:]
				#localFileName = 'reddit_%s_%s_album_%s_imgur_%s' % (subreddit, submission.id, albumId, imageFile)
				if not os.path.exists(filename + os.sep + postTitle):
					os.mkdir(filename + os.sep + postTitle)
				if '.jpg' not in url or '.png' not in url or '.gif' not in url:
					continue
				localFileName = filename + os.sep + postTitle + os.sep + imageFile
				print("local" + ' ' + localFileName)
				if not os.path.isfile(localFileName):
					downloadImage('http:' + match['href'], localFileName)
		if 'gfycat.com' in url:
			downloadURL, filenameToSave = parsegfycat(url)
			
			if not os.path.exists(filename):
				os.mkdir(filename)

			if not os.path.isfile( filename + os.sep + filenameToSave):
				downloadImage(downloadURL, filename + os.sep + filenameToSave)
	else :
		if '.jpg' in url:
			postTitle += '.jpg'
		if '.png' in url:
			postTitle += '.png'
		if '.gif' in url:
			postTitle += '.gif'
		if not os.path.isfile( filename + os.sep + postTitle):	
			downloadImage(url, filename + os.sep + postTitle)

def parsegfycat(url):
	#http://gfycat.com/cajax/get/
	parsename = 'http://gfycat.com/cajax/get/'
	ext = url.split("gfycat.com/",1)[1] 
	if '.webm' in ext: #good this is our filename
		ext = ext.replace('.webm', '')
	
	parsename += ext

	json_data = requests.get(parsename)
	data = json.loads(json_data.text)
	
	newurl = (data['gfyItem'])['webmUrl']
	fnts = ext + '.webm'

	#print (newurl)
	return newurl, fnts

def downloadImage(url, filename):
	#http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return

def main():
	parsefile()
	while True:
		mainfunc()
		print('Time to sleep')
		time.sleep(30)
		print("Waking up")


if __name__ == '__main__':
	main()