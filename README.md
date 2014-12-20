KPD
===

An image downloader for reddit (imgur)


v3.0

	Gfycat now supported
	Allows keyword for each subreddit (* for all)

===

The program will go through each of the subreddits and search for the terms in names. Then it will download any images with posts containing
those keywords. 

It will place the images into a folder in this format:

	subreddit/keyword/postname.extention or
	subreddit/keyword/postname/filename.extention (for albums)

===

You can run by typing: 
	python kpd.py

Make sure to have a config.txt file, the format for subreddits is

	subreddit :: name, name2, name3 
	subreddit :: * 
	^ for all pictures

===

Right now you must change the arrays at the beginning to change subreddits and search terms

import praw # reddit api
import urllib # get images from url
import os # makes directories
import time # used to rerun mainFunc every 30 sec
import requests # used to get html for BS
from bs4 import BeautifulSoup # used to parse for imgur albums

===
	TODO:
	
	Make it into a taskbar app
	Update folder creation code
	Support other images/video sites (youtube, flicker)

===

Apologies for any bad syntax or practicies.
