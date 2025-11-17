from curl_cffi import requests
# import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import pydash as _
# import os
# import sys
# sys.path.append(r"D:\Ajay_chauhan\thread_code")
# import proxies_token

# from dotenv import load_dotenv
# load_dotenv()
# scrapdo_token = os.getenv('scrapdo_token')
# print(scrapdo_token)

data = {
    "to_poi_type": "newes",
    "app_version": "7.1.16",
    "channel": "34",
    "client_type": "1",
    "font_scale_type": "0",
    "route_preference_type": "0",
    "v6x_version": "1",
    "map_type": "soso",
    "user_type": "1",
    "platform_type": "2",
    "model": "ASUS_Z01QD",
    "brand": "Asus",
    "order_type": "0",
    "terminal_id": "1",
    "source_from": "viewDidLoad",
    "call_car_type": "0",
    "appversion": "7.1.16",
    "multi_require_product": "",
    "access_key_id": "2",
    "origin_id": "1",
    "payments_type": "-1",
    "page_id": "conf",
    "datatype": "1",
    "lang": "en-US",
    # "lat": "22.31654912994877",
    # "lng": "114.17436872829806",

    "from_lat": "22.316337575757576",
    "from_lng": "114.17442939393939",
    # "to_lat": "22.28032",
    "to_lat": "22.283811446977797",
    # "to_lng": "114.13483",
    "to_lng": "114.14678487686811",
    "menu_id": "dache_anycar",
    "token": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
    "tab_id": "normal",
    "maptype": "soso",
    "business_id": "666"
}

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# token = proxies_token.scrapdo_token
# proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true&geoCode=us@proxy.scrape.do:8080".format(token)
# proxies = {
#     "http": proxyModeUrl,
#     "https": proxyModeUrl,
# }

# proxy_url = proxies_token.decodo_url
# proxies = {
#     "http": proxy_url,
#     "https": proxy_url,
# }

# scraper_api_token = proxies_token.scraperapi_token
# proxies = {
#     "http": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001",
#     "https": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001"
# }

def response_check(start_iteration, num_requests):
    """Perform multiple requests inside one thread to reduce overhead."""
    batch_results = []
    for i in range(num_requests):
        iteration = start_iteration + i
        st = time.time()
        try:
            response = requests.post(
                'https://api-hk.udache.com/gulfstream/pre-sale/v1/core/pMultiEstimatePriceV3',
                data=data,
                # params=params,
                # headers=headers,
                # cookies=cookies,
                # impersonate='chrome120',
                # proxies=proxies,
                # verify=False,
                timeout=120
            )
            if _.get(response.json(),'data.layout[0].price',None):
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'good',
                    'time_taken': time.time()-st
                }
                batch_results.append(return_dict)
                print(return_dict)
            else:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'bad',
                    'time_taken': time.time() - st
                }
                batch_results.append(return_dict)
                print(return_dict)
        except Exception as e:
            return_dict = {
                'iteration': iteration,
                'status': None,
                'response': f'error: {e}',
                'time_taken': time.time() - st
            }
            batch_results.append(return_dict)
            print(return_dict)
    return batch_results

results = []
thread_count = 20
total_requests = 3000
requests_per_thread = 1  # Each worker handles 10 requests

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    futures = []
    for start in range(1, total_requests + 1, requests_per_thread):
        futures.append(executor.submit(response_check, start, requests_per_thread))

    for future in as_completed(futures):
        batch = future.result()
        for result in batch:
            # print(result)
            results.append(result)

# Save results to Excel
file_name = 'didi_ride_feasibility_test02'
df = pd.DataFrame(results)
df.to_excel(f'{file_name}.xlsx', index=False)
print(f"Results saved to {file_name}.xlsx")


