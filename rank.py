# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import urllib
import unicodedata
import operator
import hashlib

user_name = ""
user_id = ""
user_fix = u"(고정닉)"
user_unfix = u"(유동닉)"

user_dic = {}

for page_num in range(1,74):

	html = urllib.urlopen("http://gall.dcinside.com/board/lists/?id=japanese&page="+str(page_num))
	soup = BeautifulSoup(html, "lxml")
	link = soup.find_all("td", { "class" : "t_subject" })

	for m in link:
		if(m.find("a", {"class":"icon_notice"})):
			pass
		else:
	  		if(m.parent.find("td",{"class":"t_writer user_layer"}).get('user_id') == ""):
	  			user_name = m.parent.find("td",{"class":"t_writer user_layer"}).get('user_name')
	  			user_id = "id = "+ m.parent.find("td",{"class":"t_writer user_layer"}).get('user_id')
	  			user_total = user_name + user_unfix
				#print user_id

	 			if user_total in user_dic:
	  				print "true"
	  				user_dic[user_total] += 1

	  			elif user_total not in user_dic:
	  				print "false"
	  				user_dic[user_total] = 1

	  			print user_total
	  			print "\n"



	  		else:
	  			user_name = m.parent.find("td",{"class":"t_writer user_layer"}).get('user_name')
	  			user_id = "id = "+ m.parent.find("td",{"class":"t_writer user_layer"}).get('user_id')
	  			user_total = user_name + user_unfix
				#print user_id

	 			if user_total in user_dic:
	  				print "true"
	  				user_dic[user_total] += 1

	  			elif user_total not in user_dic:
	  				print "false"
	  				user_dic[user_total] = 1

	  			print user_total
	  			print "\n"


	print "======================="+"page_num = "+str(page_num)

user_dic_sorted = sorted(user_dic.items(), key=operator.itemgetter(1))

for n in range(1,21):
	print str(n) + "위 = " + str(user_dic_sorted.pop())








