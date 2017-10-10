from bs4 import BeautifulSoup as soup 
import urllib2 

my_url = 'https://www.youtube.com/watch?v=_k5_HmjxPwQ&list=PLbuSNdsf9BjSU2qB-PPv98olOA5yU5Wkx'

# Opening up connection, grabbing the page 
req = urllib2.Request(my_url)
uClient = urllib2.urlopen(req)
page_html = uClient.read() 
uClient.close()

# HTML parser 
page_soup = soup(page_html, "html.parser")

# Now you can do ==> page_soup.h1 ==> and displays the h1 from the web 
videos = page_soup.findAll("ol", {"class":"playlist-videos-list"})

for video in videos: 
	href = video["href"]
	# Print all hrefs from all <a> tags 
	print href 

      