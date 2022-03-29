import requests
import os
from pprint import pprint

class YaDiskAPI:

    def __init__(self, token):
        self.token = TOKEN

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_resp(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        resp = requests.get(url, headers=headers, timeout=5)
        # pprint(resp.json())
        return resp

    def get_upload_link(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params, timeout=10)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str, name: str):
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        headers = self.get_headers()
        response = requests.put(href, data=open(disk_path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success!')




if __name__ == '__main__':
    with open('text.txt') as file:
        TOKEN = file.read()

    # TOKEN = ''

    disk_path_to_file = os.path.abspath("") # полный путь к загружаемому файлу
    disk_file_path = "disk:/search_info.py"
    name = 'search_info.py'

    test1 = YaDiskAPI(TOKEN)
    test1.get_resp()
    test1.get_upload_link(disk_file_path)
    test1.upload_file_to_disk(disk_file_path, name)
