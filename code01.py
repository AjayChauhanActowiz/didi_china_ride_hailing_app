import requests
import urllib.parse
import pydash as _

# URL (already decoded for readability; requests will re-encode as needed)
url = (
    "https://api.udache.com/gulfstream/pre-sale/v1/core/pMultiEstimatePriceV3"
    "?wsgenv=eV60AFKmiKuAsrPPAAAAA0ADAABwGTKryYVjwSlp3rHkrLmUAdxbsIINSwaLSXlQ2BbW8lECMxYYFyhhbJ9p%2F6G5IWCxf6FeEmSgtp9h8npJrEImRihVm5fV09Hrb1A%2FUY005b4QUSflC2PzhZ22iNgCFtIgsftsjG%2BDvRkKmKh95KcJLdsQx3mk8ko9%2F0Y59JBngSrDnpvfmooIOc5zLruAVXwRYGaqNGdzAtAXI26VDpChCuATknnBhA3ICVqilbUM6z6rBsaPeMOzeYHA1zLP62vqNtZLyrNmiNR1rt8HhRUyQzUdekwB0PqbAMebAe1R74RY3q%2BhEf1xnMDEx2E4ND5U9OfY8kcoQ0WAykG2cKljgLS4zwFU11TlY2WCiD1ZNhSNygTEdn%2FFn%2FuK%2ByQChRRjAvA0UJdpzGdKgU9Xap63cjT%2BAgBn3FAEv9kBFSGj1kKei9jyzQkctn4PwEDVGyW%2F%2BA579fGHpcoDzoVkb7BoD9O6Ia%2BmkoZe3JB5x4hDfZWkCj5nqSSdzjr56lD1e4CK5pYhVCsPJSU4DwZxnN%2BgW08CayAYWMAT8EiLR91KbBx7bdloFX%2BAJrpwKAMtUzsq%2Fbq7lnh2bcNKzM4f54OCx%2FISx3Eb7t4tn%2F24Y5HEM7eJKVY0bazvN0UHpY3alya7DsDfNREUpW4s%2FLiMaJLK0ZeLw9A723%2FjTKZOJVm1Hw3Ok6GO6UzLay7XGk4Tkov31aQH9qjJDsJCUvgaZH3xGD5PG4VBfJytsuqd4911hisVP9GbGlUjkWEOPOPZNAnUJl%2Fhzb6JClGII62wdXU3tBOSd7vva185bKmN%2BiYVzX4VBqyrAq2lJUaACqVCKvLEtAHVbFYAkT5qQTbXILVNG70QhZKBkD7noP1TLrZN770iFK%2F5pYLjqlqzljmkOSaXQcKeoxbSudfFV74dIqFMWOZpCZ0bXtViEBjPXKJneDWm91ebQvwUE0120VECo8f9pFbEvzsKJHxYEiVNDzZTHWr29pP%2FaDUUBLtHFIP5iJ233bC%2FaPdyc6M7kl%2FnHoJUm1ArE9i1HTYKyerK%2Bt8BW2hWGS6an8TJ5LtDgj%2BUMBqXS%2BQ2Pipx0mdmJzYvyduPItsJBtSxUnr8VVZhW7gthE1c9i%2BA9sivC6R8mNl3kFZdpm9pB%2Br%2FWVPNqLMLqLCpHCh3wg4CoXdV1RBYrrCy"
)

# Headers
headers = {
    "Accept-Encoding": "gzip",
    "Cityid": "0",
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "didi-header-hint-content": '{"app_timeout_ms":27000,"utc_offset":"330","xregionkeyvalue":"357","location_cityid":-1,"Cityid":-1,"xregionkeyname":"passenger","lang":"en-US","locale":"en-US"}',
    "didi-header-omgid": "Zq-n3DncRgO0vU-LvTSs6g",
    "didi-header-rid": "7a2a5cf3691acb80000013801ca98468",
    "didi-header-ssuuid": "b18114818bd1d34c3850ea6a039a34cb",
    "didi-httpdns": "1",
    "Host": "api.udache.com",
    "net-lib-source": "Rabbit",
    "ocid": "357",
    "Productid": "0",
    "secdd-authentication": "11f3264d616cb0e270b5df8f4145720521999ec8444a55c3e789182aa90b17523fbfee4e8f4fae03712c58efbd0db7496f66a9909a01000001000000",
    "secdd-challenge": "1,com.sdu.didi.psnger|1.0.29||||0||",
    "ticket": "mduz4QSmd9PIjDAqrRoMcrE9Mw9dFqBADaeByB9_4ackzEtKBkEMAOG71NYwJJ3ujsk1xAP4GB-bFhRXg3eXmX9bFN_BUgrfdFOEZZQJq1GmqiospyxGZmbM5t2HsPrZwsyzeQprUDw-IDxRIDxTLVOjZ_QerUcIr5e8Uwc_X7_fLzulf8LbSU336Rf1TnFn3e-n5dRhCB838_P8_wMAAP__",
    "TripCountry": "HK",
    "User-Agent": "com.sdu.didi.psnger/7.1.16 Rabbit/1.5.6.1 Carrot/1.7.8.10",
    "wsgsig": "dd06-/5SJJLf635LoGW4DqsMNU7kkjwdQKdofKmsn2tuUl+5PmWojSRRtuzSgm6zs7YvjArNfXzMEiy10EuzE20t3WthVVTwlMSEfwY0d0shstq8I7LDo9Ujis/0FeypqFFDASL+ruoTRgb8laIjhwfuaZprXkydk8w8hxU+GEiHzqhDx9S4lwdDDEzWdHR8C-/5SJJeL7Q4D4KE8U/HjwvUm/7OBWSwH/iocDAQILuLCrxjse812Pj6QiL3teF6EPe9DdQKv1wpBNk+8W1w3yG3esVCkNuBbMXDrYgd6WrNq5F8ysY+XJQLc+GTlaSR4U3VDlD9ZnY+J3ypOKLLvqv1Femor9SVYGiErWgijx9pJPeU3QH2BkWn4j8v7OumJkjpm1pCu7TlKRWQWjqyNk3x0lekZjScySDdPPKzPFYbfX0WaJO9afuQmhYQrEBORt2ZZZDIwWJFIxm2ohhJmw2mGzHj0DThYGDIYofwxAn43retlqVPYBhB5iYJHFnI8dRz6r7UrpD4lm0FK3KFjvHa7eHXVQGfsBiaKbxHwF1VHngTMR0iKHZDTF3u56EC6JGkrS4AEthYKVxJWOK2DayE7sDsofm1ZM8F4eYfxT2PElDUrJI+JqnkofS2hNiy6a+Bo3xhPgRcJNjAfo6Fg/s5yckYQGHxUF69JFLHQ1HPqjSfhQyk9T7Vce+SNaDtNBEeQhqD7PAq+AKvuireENwgjBzTVQ+UzJk1SCeoSdPfqKU+YApnERaA1AyepN4F2hmqVvxaawNREQM3C9DtEPPJGTQumXzK0/5uHC6Be/qvHM5xXESL6NeLJVyRAiEGG8aQRw2y+XjMYypCWke7mBm/RpZ8arjf/AL3VajPbZSiZW4tv4zMyNyAkE56/Ln+at+p+nw0rUzeFib69n2cRK13WygaYJc6XK8W3xcaJf0rqChqgfoYiiG/N4mi+NfKCmDpqfWQZjrWnmQrrdbF/9YAEx6eWvIsQhsU6zw5XZ5fFEraDKnAL6R3CZUeUqPoMfVtRp8kECM2m3Vd8pK80Oax88HmvC1WlB6d0wbWthmb+o9sqVW2cuzq6vJem23esvDb8aUVhS377E88atEyQNIOQkmPQynY850LWe0AGxKf/oAPzYe90QVC1aVylkH78sEj+WLqzkFDmF+IxGtJHalT05PS9tgeQNp2pWyCoYXBfNeeT4dmjibdapwv2jVlOxnG6t+EKfEmy5F6MRDxiZTcX4fxyX0jfLWbz2bMuwGKk9A7e0G0tJcboCfrmdhH9r8C9KnjoqaIc43L0eyCaCv/V32v4hDeWTraFhSLE6gJXFEfGrq9VMRLdaHK0BDeWTraFhSLE"
}

# Request body (form-urlencoded data)
# Note: urllib.parse.urlencode is NOT used here because the body is already a raw string.
# We just need to ensure it's passed as bytes/string in the correct format.

data = (
    "to_poi_type=ud_Dfm_top&app_version=7.1.16&channel=34&client_type=1&font_scale_type=0&uuid=0979748AE7E1D2EBD0D2EE0C4A974B5B"
    "&a3_token=4M58nnuKoIly3wigxquaQCzL32AYb778Tan2ry6g716VmaIgaXEbnCnETJabB3HJQbiFtB3rgTArxcpCZUPU%2BxRjbl0NPcC5npNg202pnscDggjA8ygPIe0ylQfRLNwa8pOWJOCJCnjoPqNUQIaBUw%3D%3D"
    "&route_preference_type=0&v6x_version=1&map_type=soso&user_type=1&platform_type=2&choose_f_searchid=1832ffb4691acb76000013801ca98449"
    "&model=SM-S9210&brand=samsung&from_address=Airport+Taxi+Pick-up+Point+-+Regal+Airport+Hotel+Hong+Kong"
    "&from_poi_type=pgcstation&order_type=0&terminal_id=1&lat=0.0&source_from=viewDidLoad&dest_poi_code=801010&lng=0.0"
    "&call_car_type=0&suuid=b18114818bd1d34c3850ea6a039a34cb&from_poi_code=&appversion=7.1.16"
    "&to_address=%E4%B8%AD%E8%A5%BF%E5%8D%80-%E7%89%B9%E5%88%AB%E8%A1%8C%E6%94%BF%E5%8C%BA%E4%B8%AD%E8%A5%BF%E5%8C%BA%E6%B0%91%E7%A5%A5%E8%A1%97%E4%B8%8E%E6%B0%91%E8%80%80%E8%A1%97%E4%BA%A4%E5%8F%89%E5%8F%A3%E6%AD%A3%E5%8C%97%E6%96%B9%E5%90%9168%E7%B1%B3%E5%B7%A6%E5%8F%B3"
    "&pixels=720*1280&multi_require_product=&biz_appid=10000&access_key_id=2&from_area=357&from_lng=113.93895&origin_id=1"
    "&from_name=Hong+Kong+International+Airport+-+Regal+Airport+Hotel+-+Taxi+Pick-up+Point&vcode=1207011604"
    "&payments_type=-1&page_id=conf&datatype=1&to_lng=114.164379&networkType=WIFI&lang=en-US"
    "&from_poi_id=R1152921683971539951&menu_id=dache_anycar&from_lat=22.31627&to_lat=22.282403&screen_scale=1.5"
    "&choose_t_searchid=&os=9&to_name=IFC+Mall+East+Entrance"
    "&token=mduz4QSmd9PIjDAqrRoMcrE9Mw9dFqBADaeByB9_4ackzEtKBkEMAOG71NYwJJ3ujsk1xAP4GB-bFhRXg3eXmX9bFN_BUgrfdFOEZZQJq1GmqiospyxGZmbM5t2HsPrZwsyzeQprUDw-IDxRIDxTLVOjZ_QerUcIr5e8Uwc_X7_fLzulf8LbSU336Rf1TnFn3e-n5dRhCB838_P8_wMAAP__"
    "&tab_id=normal&to_poi_id=1772599195262271494&to_area=357&maptype=soso&business_id=666"
    "&xpsid=4e70cda44c0190a877164ddcc8b05214&xpsid_root=bc635f223e532d3a41f74923bfdb39ad"
)

# try:
#     response = requests.post(url, headers=headers, data=data, timeout=30)
#     print("Status Code:", response.status_code)
#     print("Response Headers:", response.headers)
#     print("Response Text (first 500 chars):", response.text[:500])
# except requests.exceptions.RequestException as e:
#     print("Request failed:", e)
response = requests.post(url, headers=headers, data=data, timeout=30)
print(response.status_code)
print(response.text)
print(_.get(response.json(),'data.layout[0].price',None))