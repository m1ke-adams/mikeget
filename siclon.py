import requests
knk=input("site giriniz kopyalanacak: ")
qwe=requests.get(knk,verify=False)
fayil=open("site.txt","w")
fayil.write(str(qwe.content))
fayil.close()
