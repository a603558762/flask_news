import requests
url='http://202.103.233.132:9080/ermsLogin/login.do'
headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length': '47',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'202.103.233.132:9080',
'Origin':'http://202.103.233.132:9080',
'Cookie':'CWJSESSIONID=9AB4FF378ABA2DCA85DD2E68EF4114AF; cwsid=ee0b545576b746e0804b6cc6d183801f',
'Referer':'http://202.103.233.132:9080/ermsLogin/view.do',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'

}

formdata={
'system': 'normal',
'userName': 'p0086819',
'password': '123456',

}

r=requests.post(url,headers=headers,data=formdata).content

print(r.decode())





