import requests, time, json, urllib.parse, random, threading
from pystyle import Colorate, Colors, Write, Add, Center
#7138367478103574021 7138368303832090374
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
import ssl
import queue
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
import requests, time, json, urllib.parse, random, threading
link = input(
        Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Enter video link " + Col.purple + "[" + Col.reset + "press " + Col.blue + "Enter" + Col.reset + " to start" + Col.purple + "]" + Col.reset + " -> ")

video = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
os.system('cls' if os.name == 'nt' else 'clear')

def view(video):
   # try:
        
        ve= random.choice(
            [247, 312, 322, 357, 358, 415, 422, 444, 466]
        )
      
        device = random.choice(
            ["SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                          "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B",
                          "SM-A525F"]
        )
        host = random.choice( ["api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                          "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"])

       
        
       # ve=random.randint(100,2600)
        params = urllib.parse.urlencode(
            {
                "app_language": "fr",
                "iid": IID,
                "device_id": DID,
                "channel": "googleplay",
                "device_type": device,
                "ac": "wifi",
                "os_version": random.randint(5, 11),
                "version_code": ve,
                "app_name": "trill",
                "device_brand": "samsung",
                "ssmix": "a",
                "device_platform": "android",
                "aid": 1180,
                "as": "a1iosdfgh",  
                "cp": "androide1",
            }
        )

        response = r.post(
            url = (
                "https://"
                    + host
                    + "/aweme/v1/aweme/stats?"
                    + params
            ),
            
            data = (
                f'&manifest_version_code={ve}'
                    + f'&update_version_code={ve}0'
                    + '&play_delta=1'
                    + f'&item_id={video}'
                    + f'&version_code={ve}'
                    + '&aweme_type=0'
            ), 
            headers = {
                "host": host,
                "connection": "keep-alive",
                "accept-encoding": "gzip",
                "x-ss-req-ticket": str(int(time.time())),
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": f"com.ss.android.ugc.trill/{ve} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
                
            },
            
        )
        try:
         print(response.json())
        except:
         pass



