import requests
import pydash as _

url = "https://api-hk.udache.com/gulfstream/pre-sale/v1/core/pMultiEstimatePriceV3"
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

    # "from_lat": "22.31654912994877",
    # "from_lng": "114.17436872829806",

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


response = requests.post(
    url=url,
    data=data,
    timeout=30
)
print(response.status_code)
print(response.text)
print(_.get(response.json(),'data.layout[1].price',None))