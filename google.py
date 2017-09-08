
import sys
import pyperclip
import bs4
import requests
import webbrowser
__author__ = "sekar"
def main():
	if len(sys.argv) > 1:
		search = ' '.join(sys.argv[1:])
	else:
		search = pyperclip.paste()

	res=requests.get('http://google.com/search?q='+	search)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	linkElems = soup.select('.r a')
	numOpen = min(5, len(linkElems))

	for i in range(numOpen):
		webbrowser.open('http://google.com' + linkElems[i].get('href'))

if __name__ == '__main__':
	main()
