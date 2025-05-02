import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
timeout = 10

def screen_clear():
    os.system('cls')

def ftp(star, config_file):
    if "://" not in star:
        star = "http://" + star
        star = star.replace('\n', '').replace('\r', '')
        url = star + config_file

    try:
        check = requests.get(url, headers=headers, timeout=timeout, verify=False)
        if check.status_code == 200:
            resp = check.text
            if "file manager" in resp or "Tinymce" in resp:
                print(f"ftp {gr}OK{res} => {star}\n")
                with open("filemanager.txt", "a") as f:
                    f.write(f'{url}\n')
            else:
                print(f"{red}Not Found{res} Filemanager => {star}\n")
        else:
            print(f"{red}ERROR{res} {check.status_code} => {star}\n")
    except requests.exceptions.RequestException as e:
        print(f"{red}ERROR{res}  => {star}\n")

def filter(star):
    ftp(star, "/file-manager/tinymce")
    ftp(star, "/vendor/file-manager/tinymce")
    ftp(star, "/public/file-manager/tinymce")
    ftp(star, "/app/file-manager/tinymce")

def main():
    print(f'{gr}[ Tinymce Filemanager Finder ] | [ BY Atengg377 ]')
    list_file = input(f"{gr}Give Me Your List.txt/{red}ENC0D3R> {gr}${res} ")
    with open(list_file, 'r') as f:
        star = f.readlines()
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(filter, s) for s in star]
            for future in futures:
                future.result()
    except:
        pass

if __name__ == '__main__':
    screen_clear()
    main()
