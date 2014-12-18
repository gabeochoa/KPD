KPD
===

An image downloader for reddit (imgur)

===

The program will go through each of the subreddits and search for the terms in names. Then it will download any images with posts containing
those keywords. 

It will place the images into a folder in this format:

subreddit/keyword/postname.extention or
subreddit/keyword/postname/imgurfilename.extention (for albums)

===

You can run by typing: 
	>python kpd.py
===

Right now you must change the arrays at the beginning to change subreddits and search terms

import praw # reddit api
import urllib # get images from url
import os # makes directories
import time # used to rerun mainFunc every 30 sec
import requests # used to get html for BS
from bs4 import BeautifulSoup # used to parse for imgur albums

===

Apologies for any bad syntax or practicies, I am usually a C++/Java programmer,
and am still learning. 
