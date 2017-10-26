from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time



start_url = 'https://en.wikipedia.org/wiki/Love'
target_url = 'https://en.wikipedia.org/wiki/Social_group'


def continue_crwal(searched_list,target_url,max_step=25):
	if searched_list[-1] == target_url:
		print('we found!!!')
		return False
	elif len(searched_list)>max_step:
		print('large searching!!!!')
		return False
	elif searched_list[-1] in searched_list[:-1]:
		print('getting loop!!!')
		return False
	else:
		return True

def findFirstLink(url):
	response = requests.get(url)
	htmltext = response.text
	soup = BeautifulSoup(htmltext,'html.parser')
	div_element = soup.find(id='mw-content-text').find(class_='mw-parser-output')
	suffix = None
	for element in div_element.find_all('p',recursive=False):
		if element.find('a',recursive=False):
			suffix = element.find('a',recursive=False).get('href')
			break

	if not suffix:
		return

	url = urljoin('https://en.wikipedia.org/', suffix)
	return url

searched_list = [start_url]

while continue_crwal(searched_list,target_url):
	print(searched_list[-1])
	url = findFirstLink(searched_list[-1])
	if not url:
		print('article with no url!!!')
		break
	searched_list.append(url)
	time.sleep(2)


