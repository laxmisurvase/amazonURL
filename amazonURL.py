import os
import bs4
import requests
from sys import*
from urllib.request import urlopen

def MarvellousURLScrapper(url):
	connection=urlopen(url)

	raw_html=connection.read()

	connection.close()

	page_soup=bs4.BeautifulSoup(raw_html,"html.parser")

	container=page_soup.findAll("a",{"class":"a-link-normal a-text-normal"})

	return container

def main():
	print("---Demonstration of URL scrpper amazon----")

	print("application name:"+argv[0])

	if(len(argv)==2):
		if(argv[1]=="-h")or(argv[1]=="-H"):
			print("used to fetch URL of images")
			exit()

		if(argv[1]=="u")or(argv[1]=="-U"):
			print("usage:applicaiton name")
			exit()
	try:
		url="https://www.amazon.in/s?k=macbook&ref=nb_sb_noss"

		listout=MarvellousURLScrapper(url)

		print("URL from website is :")
		for elements in listout:
			print(elements['href'])

	except Exception as E:
		print("error:invalid input",E)




if __name__=="__main__":
	main()
