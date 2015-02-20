'''
curl -H "Authorization:token 0b8d125e7e8ce077cc021824c8964d9cc6da02a0" --request POST --data '{"title": "Found a Dummy bummy gummy Bug"}' https://api.github.com/repos/rohspeed/Algo-world/issues
'''

import urllib2
import math
import json
from mail import read_mail
DEFAULT_TITLE = "ISSUES FOR Algo-World Repo"

def send_issues_to_github(msg_list):
	for subject,message in msg_list:
		if not subject: subject = DEFAULT_TITLE
		data = json.dumps({"title": subject, "body": message})
		req = urllib2.Request("https://api.github.com/repos/rohspeed/Algo-world/issues",
		      		      headers = {"Authorization": "token 0b8d125e7e8ce077cc021824c8964d9cc6da02a0",
			         		 "Content-Type": "application/json",
				                 "Accept": "*/*"},  
		      		      data = data)
		try:
			f = urllib2.urlopen(req)
			print "Msg sent to github repo"
		except urllib2.URLError, e:
			print 'It seems like the server is down. Code:' + str(e.code)

if __name__ == "__main__":
	username = "rohithfortopcoder"
	password = "8885376049"
	msg_list = read_mail(username, password)
	send_issues_to_github(msg_list)
