from pytube import YouTube
import os
DownloadFile = ""
os.system("clear")
print('''\033[1;36;40m__   _______   ____                      _                 _
\ \ / /_   _| |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
 \ V /  | |   | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | |   | |   | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
  |_|   |_|   |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|\033[0m

			\033[1;34;40mcreated by\033[0m \033[1;33;40mTechnical Dangwal\033[0m
''')

link=input("\033[1;33;40mEnter the link of youtube vedio you want to download :\033[0m \033[1;32;40m")
Inp=int(input("\033[1;33;40m [1] Video \n [2] Audio \n Choose :\033[0m \033[1;32;40m"))
ys=YouTube(link)
if (Inp == 1):
      vedios=ys.streams.filter(file_extension='mp4')
elif (Inp == 2):
      vedios=ys.streams.filter(only_audio=True)
else:
      pass
i=1
for vedio in vedios:
	print(f"\033[1;32;40m{i}.\033[0m \033[1;33;40m {vedio}\033[0m")
	i+=1
res=input("\033[1;33;40mEnter the resolution :\033[0m \033[1;32;40m")
os.system("clear")
print(f"\033[1;33;40mTitle of vedio  :\033[0m \033[1;32;40m{ys.title}\033[0m")
print(f"\033[1;33;40mViews of vedio  :\033[0m \033[1;32;40m{ys.views}\033[0m")
print(f"\033[1;33;40mLength of vedio  :\033[0m \033[1;32;40m{ys.length}\033[0m")
print(f"\033[1;33;40mRating  :\033[0m \033[1;32;40m{ys.rating}\033[0m")
print(f"\033[1;33;40mDescription of vedio  :\033[0m \033[1;32;40m{ys.description}\033[0m")
vedios=vedios[int(res)-1]
vedios.download(DownloadFile)
