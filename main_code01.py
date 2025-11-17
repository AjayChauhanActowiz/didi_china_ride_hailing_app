import requests
import pydash as _
import pandas as pd
from datetime import datetime

total_data = []
def get_drop_off_detail(search_address):
    params = {
        "access_key_id": "2",
        "app_version": "7.1.16",
        "channel": "34",
        "request_page_num": "1",
        # "select_lat": "22.31633758544922",
        # "select_lng": "114.17443084716797",
        "platform": "2",
        "transnational_type": "0",
        "map_type": "dmap",
        # "city_block_strategy_exp": "1",
        "sub_app_version_60": "v1",
        "product_id": "666",
        "place_type": "2",
        # "start_lat": "22.316337575757576",
        # "start_lng": "114.17442939393939",
        # "is_test": "",
        "lang": "en-US",
        # "urbo": "357",
        "app_id": "com.sdu.didi.psnger",
        "coordinate_type": "gcj02",
        "order_type": "0",
        "mansearch": "0",

        # "query": "Kennedy Town Belcher’s Street",
        "query": search_address,
        # "user_loc_lat": "22.31654912994877",
        # "user_loc_lng": "114.17436872829806",
        "user_loc_lat": "22.316337575757576",
        "user_loc_lng": "114.17442939393939",

        "didi_textsearch_sessionid": "",
        "multiple_req": "1",
        "api_version": "1.0.4",
        "acc_key": "HA1UC-TH0WZ-DXT1E-4CLUM-AJD4X-K8ESZ",
        "is_show_door_close": "2",
        "requester_type": "1",
        "token": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
        "source_tab": "domestic",
        "user_id": "299074974472477",
        "caller_id": "map_default",
        "update_time_favorite": "0",
        "jw_req_type": "2",
        "assist": "",
        "sub_app_version": "app_version_6_0",
        "user_loc_type": "0",
        "is_no_cache": ""
    }
    headers = {
        "Accept-Encoding": "gzip",
        "CityId": "357",
        "Connection": "Keep-Alive",
        "didi-header-hint-content": '{"app_timeout_ms":9000,"utc_offset":"480","location_cityid":357,"Cityid":357,"lang":"en-US","locale":"en-US"}',
        "didi-header-omgid": "EeH-xyw8RmONubxzXWp9fw",
        "didi-header-rid": "2561e0d6691ae585000029b0715ca749",
        "didi-header-ssuuid": "4b86a0be83cf5ccbe05b7b04af5a4ef6",
        "didi-httpdns": "1",
        "Host": "poi-hk.map.xiaojukeji.com",
        "net-lib-source": "Rabbit",
        "Productid": "0",
        "secdd-authentication": "0855568b49f85916c708ce43f718ce9b7e8763104ce1678ca9b63c430c2419cb33b03d6c98706de827dbf6c71b0c904f60dd0d919a01000001000000",
        "secdd-challenge": "1,com.sdu.didi.psnger|1.0.29||||0||",
        "ticket": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
        "TripCountry": "HK",
        "User-Agent": "com.sdu.didi.psnger/7.1.16 Rabbit/1.5.6.1 Carrot/1.7.8.10",
        "wsgsig": "dd06-hNdJJLQS9SLt6f4DsEFNU1UojwdYD8hbcSnBz5eXPZa5yFY0jwtQL9Arm6zXeHvjCDGfXzrNiy154JzE3IK3WtW8VTwQk5Efy2pd0sW5tq8NdwDobG4is/K+eypV4lDATo0rupCFgb8QjP4QzHtCYbVilyRxfHvjAOybY+rKpr0vg2jjylXAZ97oHR80-hNdJJeqOQ4DTgKRahQsR15ri5ldOGUxYUsubp7bFGU84R2/WbtFiQ1/PuVzZCuNjrVjoSrhukvL5xhfo3bXacv7Y43B9SAPkUEdtLv3wfUJS4pysZhIFLvwHbwJkAzTwxP6ImBXrvd/0KxPkrLfC6GC8LZnKteYG5Q1/XyTEQeIh+ZNIiwtZqXOIInJS7PCsfD1kemxZtuJavBl3ccpq6JtrstHrF8yLojqGzWIpdF338oDFwXLfgG+gkgn40ouaWydJHmJgId7PxnbOzCwXqu8IHj01gczRRL8qYBPbTK+HlNI+5XNPcdJWGKIMJuxh8OkgsWHRk6YJSCdGTjy3xFlBAibmmfMF5LxrmIISolSzfHpGxXivQhul9rVUvgo4uGk3Az3mWu6y0xnaczmamV7USqfIGear7JOKHkkP02jyCm0W8xa3peIMRVrG8xkHl3+Abu3FD4LhILjqQY9AXjtzR6hOwJ1NLmNEpcJDhvisKWVoQhi4e8dfDPtY8vTNZjDeW/TLQf6lruN9X7JMX0fXZtMy/FlJaQT4nTDTY44B4H7xrhmWc0fuSrHN1YjpFVdYf/WZOzT+zfVfShphMmuJ500rh4HGoNcr2mCzBq55DU9HTxVNeLo/IBUCq758TuypK7ENnnZ9xN6uSRiwrpk6k7KDqs+3/WKHk8/maco4CPy2IsUSm5rHM75HuI4wiLsV+0+fe6O+XG75IShLt56qnrlj36sSjzXG2GMyZYR+5X0cUUizOWtfLqRYKgUg3v0ClpPFl9CyhwPWDILtppi+J3cLyVefAii7yrSr4l066Vsxidi2bKCk9Amcl+D7VeHNFTbMs57e//r2fsVhrMjPHmv0TOgFHQ2dtx4QisXX+8ytccNq6U/xwwvaUDiKVYIN6n3Tdx1veBSPfS6EwsVPzfouIVNvciem0Ar71zWy2JA8ulytB2AUyZjgn+bYORjmbDemeybHGmTGsqVN8SM9qthXcvLURtaciOpo+o3je9VOGskpJeKiYku3i4tEDEeouaa8G0x8DLu1F5bT2dN/MOlPXnNoAs1QbYDjamKI03QHs6NLk5Jk3QYK4AMJwKrjZ7IO2iOFBCtFAO/E5IBQ2v4m2VWTsiThSLHngJX33WGrriMMRLORHK0G2VWTsiThSLH"
    }

    response = requests.get(
        'https://poi-hk.map.xiaojukeji.com/mapapi/textsearch',
        # headers=headers,
        params=params,
        timeout=30
    )
    # print(response.status_code)
    if response.status_code == 200:
        if _.get(response.json(),'result[0].base_info.address',None):
            return {
                'Drop_off_Location': _.get(response.json(),'result[0].base_info.address',None),
                'Drop_off_Location_Lat': str(_.get(response.json(),'result[0].base_info.lat',None)) if _.get(response.json(),'result[0].base_info.lat',None) else None,
                'Drop_off_Location_Long': str(_.get(response.json(),'result[0].base_info.lng',None)) if _.get(response.json(),'result[0].base_info.lng',None) else None,
                'Distance_km': _.get(response.json(),'result[0].extend_info.distance',None)
            }
        return None
    return None
def extract_data(drop_off_search):
    Pickup_Location_Lat = '22.316337575757576'
    Pickup_Location_Long = '114.17442939393939'
    drop_detail = get_drop_off_detail(drop_off_search)
    if not drop_detail:
        return None
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

        "from_lat": Pickup_Location_Lat,
        "from_lng": Pickup_Location_Long,
        "to_lat": drop_detail['Drop_off_Location_Lat'],
        "to_lng": drop_detail['Drop_off_Location_Long'],

        "menu_id": "dache_anycar",
        "token": "uZQseSl71SzBFTtD3Hs44RTu1FHfyZ2sfE36L_P5_bAkzEtKRUEMANG91NTwSDrpjsk2xAX4eX4mLSiOLu5drk6L4hxspfGLXhRhG23CHrSpqgrbactZVZVrePgUdpwtzWK5hrAnzf0dwgMNwiM9qjSjMiJHZArPtAtX-uDr4_vz6Urrj_ByUss99Y96pbmx8NtltXQawtu_-X7-vwEAAP__",
        "tab_id": "normal",
        "maptype": "soso",
        "business_id": "666"
    }
    response = requests.post(
        'https://api-hk.udache.com/gulfstream/pre-sale/v1/core/pMultiEstimatePriceV3',
        data=data,
        timeout=30
    )
    if response.status_code == 200 and _.get(response.json(),'data.layout[0].price',None):
        layouts = _.get(response.json(),'data.layout',[])
        ids = []
        for layout in layouts:
            if _.get(layout, 'groups[0].products[0]', None):
                ids.append(_.get(layout,'groups[0].products[0]',None))
        json_data = response.json()
        for id in ids:
            docu = {
                'id': id,
                'Pickup_Location': '20 meters southeast of the intersection of Nathan Road and Argyle Street, Yau Tsim Mong District, Hong Kong',
                'Pickup_Region': 'Hong Kong',
                'Pickup_Location_Lat': Pickup_Location_Lat,
                'Pickup_Location_Long': Pickup_Location_Long,
                'Drop_off_Location': None,
                'Drop_off_Location_Lat': None,
                'Drop_off_Location_Long': None,
                'Distance_km': None,
                'Fare': _.get(json_data,f'data.estimate_data.{id}.fee_amount'),
                'Car_Title': _.get(json_data,f'data.estimate_data.{id}.car_title'),
                'Scraped_Date': str(datetime.now().strftime('%Y-%m-%d')),
                'Scraped_Time': str(datetime.now().strftime('%H:%M:%S')),
            }
            docu.update(drop_detail)
            total_data.append(docu)
drop_off_list = ['Kennedy Town Belcher’s Street','Sai Ying Pun MTR Station','Wan Chai Convention Centre','Central IFC Mall Entrance','Tai Kok Tsui Olympian City','Admiralty Pacific Place','Quarry Bay Taikoo Place']
for l in drop_off_list:
    extract_data(l)
    print(f'{l} done')
df = pd.DataFrame(total_data)
df.fillna("N/A", inplace=True)
# Export to Excel
file_name = 'didi_china_sample_data'
df.to_excel(f"{file_name}.xlsx", index=False,engine='openpyxl')
print(f"✅ Data exported to '{file_name}.xlsx' (excluding _id and path).")
