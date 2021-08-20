import requests

#bu yazılım sahibi belirtilecek şekilde değiştirilebilir veya geliştirilebilir sadece, aksi takdirde dava açılır.
print("""

┌───── •✧✧• ─────┐
 -Yapımcı Mike adams 
└───── •✧✧• ─────┘
Web Site Open Source Clonner tool v1.0
""")
knk=input("site giriniz kopyalanacak: ")
qwe=requests.get(knk,verify=False)
fayil=open("site.txt","w")
fayil.write(str(qwe.content))
fayil.close()
