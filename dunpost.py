import requests
import sys
import time
from threading import Thread as thread
import urllib.parse as parse

id_post = []
token = input("Token : ")
def addpostid():
	try:
		with open("id.txt","r") as file:
			for i in file.read().splitlines():
				if (i == ""):
					continue
				else:
					id_post.append(i)
	except FileNotFoundError:
		sys.exit("File not found!")

def posttogroup():
	url = "https://graph.facebook.com/{0}/comments?method=POST&message={1}&access_token={2}".format(idp,parse.quote(message),token)
	respond = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
	if respond.status_code == 200:
		print("Successful [ {0} ]".format(idp))
	else:
		print("Failed [ {0} ]".format(idp))

if __name__=="__main__":
	addpostid()
	if (len(id_post)) != 0:
		pass
	else:
		sys.exit("Getting 0 in id.txt")
	message = input("\nMessage : ")
	sleep = int(input("Delay in seconds : "))
	while 1:
		for idp in id_post:
			th = thread(target=posttogroup)
			th.start()
			th.join()
		print("Sleeping... [{0} seconds]".format(sleep))
		time.sleep(sleep)