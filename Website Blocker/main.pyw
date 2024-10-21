import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts.file"
redirect = "www.google.com"
website_list = ["www.youtube.com", "youtube.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("running")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    #file.write(redirect + " " + website + "\n")
                    file.write(f"{redirect} {website} \n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("not running")
    time.sleep(5)