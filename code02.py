import requests
import pydash as _

# 1. Base URL
url = "https://api-hk.udache.com/gulfstream/pre-sale/v1/core/pMultiEstimatePriceV3"

headers = {
    "Accept-Encoding": "gzip",
    "CityId": "357",
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded",
    # "didi-header-hint-content": '{"app_timeout_ms":27000,"utc_offset":"480","xregionkeyvalue":"357","location_cityid":357,"Cityid":357,"xregionkeyname":"passenger","lang":"en-US","locale":"en-US"}',
    # "didi-header-omgid": "EeH-xyw8RmONubxzXWp9fw",
    # "didi-header-rid": "769020c0691ae590000029b0715ca750",
    # "didi-header-ssuuid": "4b86a0be83cf5ccbe05b7b04af5a4ef6",
    "didi-httpdns": "1",
    "Host": "api-hk.udache.com",
    "net-lib-source": "Rabbit",
    # "ocid": "357",
    "Productid": "0",
    # "secdd-authentication": "0855568b49f85916c708ce43f718ce9b7e8763104ce1678ca9b63c430c2419cb33b03d6c98706de827dbf6c71b0c904f60dd0d919a01000001000000",
    # "secdd-challenge": "1,com.sdu.didi.psnger|1.0.29||||0||",
    # "ticket": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
    "TripCountry": "HK",
    "User-Agent": "com.sdu.didi.psnger/7.1.16 Rabbit/1.5.6.1 Carrot/1.7.8.10",
    # "wsgsig": "dd06-k7dJJMfX9SLy6f4DUUFNUGwYjwf7sAjMTxvhPpz7N2m1MjgrFb/UOASrm6wCeHvjEtGfXqMNiy1g4JzE62K3WUi8VTwVk5EfAZpd0ti5tq8PdwDodW4ish0+eySA4lDAqN0rupoFgb8VjP4QC1tCYchilyO1fHvjDHybY9MKprEGg2jjBeXAZ9uoHR8b-k7dJJfLOQ4CWMTkZyeG6mJSsR8HQBD0JOe9CWOLhOL4I8hzWPZD93NVXPn+f42zF7h0Uz4Lqqa1wZZ1JWTIikfY9TR1V5sPwMFIlgNs9U7qv4pyswIhKm4d6kiOrQ8YS9HTnTjvghJc/bnfH0qBUtGLIKqeMteYGQ+K/pmQHe7N20OsQzq7efLGHA3GfWHWZlGKTDYWKmghVFUFfQHw4rDtZPytugSld5R0TS55oPvJEKG7IIZ+3XmmpDdvkN7rAWmENnKsb/Z6z4NAE7TjMpbcIHj0cEBUslAyCZqbKHDZyg6oC2mijGuITY4cmzGW9CNPiV8TrasRaoiWc9oyYt5db7WCla+qbVRs622SYhHfH0XyZ2YOAKUylpjDBXF3PPaW/aIQU3L8pWsCfgiAZLKBUBBztwo0TJmlp520QXrYKJPIDjqQkugkT5CyoGnnAuwlKVQifBdkqnYHUYPgt/JmKHpLg7hX77Vg677iwq1tc/3dn7dKoFwZaAUKEqZz1nZJ8QnhtFsBxOovGULcuNg+rrX8lXyzgFzzRoqQTo7NmHF+DtbRYAZcdKqVA5Vwt0Oj10F+hJxwXq1OTjhutwfZyYIH8zaNQcT45B/0xVtq4HgVYXxVNeMHsDjAnJFQlL4DajC5+DAeI3tbSZVr6iItFGCbrIzXIAdRlRR/AnHeo3eLKXsMyPT9iUfIZjPST07RFmppCxe/2cnKohN8EaIKZLSsvGrxE6E2Ui7mXs6jgy55wzXTDbGzcB2m6+zgqT3nnYGmGbnDPWucFAbz7sUx/gwa94CYP+Y4p7A3Kmwyo2dqzaVO1LbLTl4QxoGr8ga8X5iJuih0zxos1RwJb9o8PHmvb2kXkqYxBZr/KDAElHG9lTtVrmsoVJXGaRLgfhkkq/fx82y5kOasgOuMH2LAIYfF+StVmq8GA47CnVt0dQfOnjBZht5xel8PzmNB+KY6JLnK9r2r1zX/zRpoV2WsEBdp+6I50dX142UUDLdHXgyQx/IScwArmsAOFKoDh3zH09aHQPRR4tkc/5TfCwXxtOkAqnrln6WJBv+1zVsP92kL+E+WqBoAYblVUg5480JrMn8wP4c9OYSqD7JzQB0FM2v4r2VWTVbThSMEngJXe3WGrUbMMRMdRHK0a2VWTVbThSME"
}

data = {
    "to_poi_type": "newes",
    "app_version": "7.1.16",
    "channel": "34",
    "client_type": "1",
    "font_scale_type": "0",
    # "uuid": "820DFC7179FFBB3CE9F0FB0AC1626B91",
    # "a3_token": "4M58nnuKoIly3wigxquaQOMD4wf2sOQj1BCHf0azNIK73ETpGODr1bga5b7HPSOGQbiFtB3rgTArxcpCZUPU+w+TgCsO99xUDFP/sDNmHXSi/cXYxzF5BTfs8WjulmSXcVtUPcHYIwSVZVvU8bLtKA==",
    "route_preference_type": "0",
    "v6x_version": "1",
    "map_type": "soso",
    "user_type": "1",
    "platform_type": "2",
    # "choose_f_searchid": "3a5ba76e691ae57a000029b0715ca72c",
    "model": "ASUS_Z01QD",
    "brand": "Asus",
    # "from_address": "20 meters southeast of the intersection of Nathan Road and Argyle Street, Yau Tsim Mong District, Hong Kong",
    # "from_poi_type": "cfcross_first",
    "order_type": "0",
    "terminal_id": "1",
    "lat": "22.31654912994877",
    "source_from": "viewDidLoad",
    # "dest_poi_code": "261200",
    "lng": "114.17436872829806",
    "call_car_type": "0",
    # "suuid": "4b86a0be83cf5ccbe05b7b04af5a4ef6",
    # "from_poi_code": "",
    "appversion": "7.1.16",
    # "to_address": "Belcher's St, Kennedy Town, Hong Kong",
    # "pixels": "720*1280",
    "multi_require_product": "",
    # "biz_appid": "10000",
    "access_key_id": "2",
    # "from_area": "357",
    "from_lng": "114.17442939393939",
    "origin_id": "1",
    # "from_name": "Hui Feng Zhong Xin - Xi Nan Men",
    # "vcode": "1207011604",
    "payments_type": "-1",
    # "dest_poi_tag": "地名地址:道路名",
    "page_id": "conf",
    "datatype": "1",
    "to_lng": "114.13483",
    # "networkType": "WIFI",
    "lang": "en-US",
    # "from_poi_id": "2027269949143126016_wecnyne3b7_89842530_100",
    "menu_id": "dache_anycar",
    "from_lat": "22.316337575757576",
    "to_lat": "22.28032",
    # "screen_scale": "1.5",
    # "choose_t_searchid": "2561e0d6691ae585000029b0715ca749",
    # "os": "9",
    "to_name": "Belcher's Street",
    "token": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
    "tab_id": "normal",
    # "to_poi_id": "805272638871044096",
    # "to_area": "357",
    "maptype": "soso",
    "business_id": "666"
}


response = requests.post(
    url=url,
    # headers=headers,
    data=data,
    timeout=30
)
print(response.status_code)
print(_.get(response.json(),'data.layout[0].price',None))