import requests
import ssl
import re
import cursor

cursor.hide()
import requests, time, json, urllib.parse, random, threading
import ssl
import requests, time, json, urllib.parse, random, threading,hashlib

import time
import queue
import threading
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from pystyle import *
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning

from xgorgon import Gorgon
from device_gen import *
import time

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


class BytedanceFuck:
    def __init__(self, __aweme_id) -> None:
        self.__aweme_id = __aweme_id
        self.__success = 0
        self.__errors = 0
        self.__devices = 0
        self.__device = 0
        self.__version = "2.0"
        self.__lock = threading.Lock()
        self.__devices = ["SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                          "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B",
                          "SM-A525F"]
        self.__domains = ["api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                          "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"]
        self.__versions = ["190303", "190205", "190204", "190103", "180904", "180804", "180803", "180802"]
        self.__client = requests.Session()
        self.__proxies = open("proxies.txt", "r").read().splitlines()        
        self.__client.cookies.set_policy(BlockCookies())
    def __safe_print(self, arg):
        self.__lock.acquire()
        print(arg)
        self.__lock.release()
    def __send_request(self, __device_id, __install_id):
        try:
            proxy = random.choice(self.__proxies)
            params = urlencode(
                {
                    "device_id": __device_id,
                    "iid": __install_id,

                    "device_type": random.choice(self.__devices),
                    "app_name": "musical_ly",
                    "host_abi": "armeabi-v7a",
                    "channel": "googleplay",
                    "device_platform": "android",
                    "version_code": random.choice(self.__versions),
                    "device_brand": "samsung",
                    "os_version": random.randint(6, 9),
                    "aid": 1233,
                }
            )
            payload = urlencode(
                {
                    "item_id": self.__aweme_id,
                    "play_delta": 1
                }
            )
            sig = Gorgon(params, payload, None).get_value()
            response = self.__client.post(
                url=(
                        "https://"
                        + random.choice(self.__domains)
                        + "/aweme/v1/aweme/stats/?"
                        + params
                ),
                headers={
                    "x-gorgon": sig["X-Gorgon"],
                    "x-khronos": sig["X-Khronos"],
                    "user-agent": "okhttp/3.10.0.1",
                },
                data=payload,
                verify=False
            )
            try: 
             print(response.json())
            except:
             pass
        except Exception as e:
           pass
    def __view_loop(self, __device_id, __install_id):
        __thread_contition = 0
        while __thread_contition < 2000:
            if threading.active_count() < 1000:
                threading.Thread(target=self.__send_request, args=[__device_id, __install_id]).start()
                __thread_contition += 1
    def __device_loop(self):
        while True:
         for x in range(10000000):
            try:
                proxy = random.choice(self.__proxies)
                __start = time.time()
                device: dict = Device().create_device()

                __device_id, __install_id = Applog(device, proxy).register_device()
                Xlog(__device_id, proxy).bypass()

                self.__device += 1
                #print(
                   # Col.purple + "{" + Col.reset + "*" + Col.purple + "}" + Col.reset + f"{Col.reset} Generated device {Col.blue}! {Col.purple}[{Col.blue}{__device_id} {Col.reset}|{Col.blue} {__install_id}{Col.purple}] {Col.purple}[{Col.reset}Execution time: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                print(f" ~ [✓] => [{__device_id}] </> [{__install_id}] ")
                print('- '*25)
                print(' ~ [✓] => Đang Tiến Hành Duyệt Dữ Liệu.                                   ',end="\r")
                print('- '*25)
                threading.Thread(
                    target=self.__view_loop,
                    args=[
                        __device_id, __install_id
                    ]
                ).start()

            except Exception as e:
                print(e)
                continue

    def start(self):
        for x in range(5):
            threading.Thread(target=self.__device_loop).start()


def init():
    os.system(f'cls' if os.name == 'nt' else 'clear')
    link = input(
        Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Enter video link " + Col.purple + "[" + Col.reset + "press " + Col.blue + "Enter" + Col.reset + " to start" + Col.purple + "]" + Col.reset + " -> ")

    __aweme_id = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(__aweme_id)
    BytedanceFuck(__aweme_id).start()

def fetch_proxies():
    response = requests.get(
        url="https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt"
    )

    if response.ok:
        os.unlink("proxies.txt")
        with open("proxies.txt", "w") as f:
            f.write(response.text)
            f.close()
            print("proxy list fetched :)")

    else:
        print("proxy list fetch error...")
        exit(1)


if __name__ == '__main__':

    
    os.system(f'cls' if os.name == 'nt' else 'clear')

    
    link = input(
        Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Enter video link " + Col.purple + "[" + Col.reset + "press " + Col.blue + "Enter" + Col.reset + " to start" + Col.purple + "]" + Col.reset + " -> ")

    __aweme_id = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])

    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ~ [✓] => Loading..!                         ",end="\r")
    BytedanceFuck(__aweme_id).start()
