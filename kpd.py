import praw
import urllib
import os
import time
import requests
from bs4 import BeautifulSoup

def mainfunc():
	subreddits = ['kpics', 'apink', 'girlsday', 'AceOfAngels8']
	names = ['Bomi', 'Eunji', 'Choa', 'Jimin', 'Hyeri']

	r = praw.Reddit(user_agent='KPD by /u/gabe1118')

	for subreddit in subreddits:
		if not os.path.exists(subreddit):
	   		os.makedirs(subreddit)
		
		submissions = r.get_subreddit(subreddit).get_new(limit=10)
		for x in submissions:
			strs = str(x)
			postTitle = (strs.split("::"))[1]
			for Iname in names:
				fn = subreddit+os.sep+Iname
				if not os.path.exists(fn):
					os.mkdir(fn)
				if postTitle.lower().find(Iname.lower()) == -1:
					continue
				else :
					savefile(subreddit, x, x.url, fn, postTitle)

def savefile(subreddit, submission, url, filename, postTitle):
	print(url, filename)

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
	            localFileName = filename + os.sep + postTitle + os.sep + imageFile
	            downloadImage('http:' + match['href'], localFileName)
	else :
		if '.jpg' in url:
			postTitle += '.jpg'
		if '.png' in url:
			postTitle += '.png'
		if '.gif' in url:
			postTitle += '.gif'
		downloadImage(url, filename + os.sep + postTitle)

def downloadImage(url, filename):
	print('downloading')
	file = open(filename,'wb')
	file.write(urllib.urlopen(url).read())
	file.close()

def main():
	while True:
		mainfunc()
		print('Time to sleep')
		time.sleep(30000)
		print("Waking up")


if __name__ == '__main__':
	main()