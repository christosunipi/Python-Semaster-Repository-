from operator import concat
import requests
import json
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
li=[]
current=data["round"]
for i in range (100):
    app = requests.get('https://drand.cloudflare.com/public/%d'%(current-i), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    li.append(data["randomness"])
for i in range(len(li)):
    li[i]=str(bin(int((li[i]),base=16)))
    li[i]=li[i][2:]

li=''.join(li)
max0,max1,temp0,temp1=-1,-1,0,0
for i in range(len(li)):
    if li[i]=="0":
        temp0+=1
    else:
        if temp0>max0:
            max0=temp0
        temp0=0
for i in range(len(li)):
    if li[i]=="1":
        temp1+=1
    else:
        if temp1>max1:
            max1=temp1
        temp1=0
print(max0,max1)
