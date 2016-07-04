import urllib.request
import urllib.parse
import re





def showDesc():

	urlData = input('Enter name of show(Please use - instead of spaces): ')
	url = 'http://watchseries.cr/series/' + urlData

	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req = urllib.request.Request(url, headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()


	paragraphs = re.findall(r'<div class="video-page-desc">(.*?)</div>',str(respData))

	for eachP in paragraphs:
		print(eachP)

showDesc()