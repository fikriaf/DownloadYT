import os

try:
	from pytube import YouTube
except:
	os.system("pip install -r requirements.txt")
	os.system("clear")

print("""
************************
   Download Youtube
************************
""")
link=input("Masukkan Link YT: ")

yt = YouTube(link)
print(yt.streams.filter(progressive=True))
print('downloaded', link)
