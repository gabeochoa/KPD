KPD
===

An image downloader for reddit (imgur)


v4.5

	imgur galleries fixed
	fixed ascii problems with other languages
	fixed bug where it would download all pictures sometimes

===

The program will go through each of the subreddits and search for the terms in names. Then it will download any images with posts containing
those keywords. 

It will place the images into a folder in this format:

	subreddit/keyword/postname.extention or
	subreddit/keyword/postname/filename.extension (for albums)

===

You can run by typing: 
	python kpd.py

Make sure to have a config.txt file. Don't forget to install the requirements after creating a virtual environment. The format for subreddits is

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
from imgurpython import ImgurClient #allows fix of image albums
import json #used to parse gfycat links
from keys import *

===
	TODO:
	
	Make it into a taskbar app
	Update folder creation code
	Support other images/video sites (youtube, flicker)

===

Apologies for any bad syntax or practicies.
