from bs4 import BeautifulSoup as soup 
import urllib2

my_url = 'http://www.xn--votamonopolyespaa-uxb.com/vota.php?id=3790'

# Opening up connection, grabbing the page 
req = urllib2.Request(my_url)
uClient = urllib2.urlopen(req)
page_html = uClient.read()
uClient.close()

# HTML parser 
page_soup = soup(page_html, "html.parser")

form_button = page_soup.findAll("form", {"id":"votaForm"})

for form in form_button: 
	button_class = form.button.attrs.get("class")
	del_class_button = form.button.attrs
	del del_class_button['class']
	print form.button
	print form.button.attrs.keys() 