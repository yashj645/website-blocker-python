import time
from datetime import datetime as dt
host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts" # r means that we are passing raw string,instead of r we can
                                                   #use \\ instead of \
redirect="127.0.0.0"
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("workng hours....")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:

        with open(host_path,'r+')as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours")

    time.sleep(5)
