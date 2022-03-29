import requests
import os
from pprint import pprint

class YaDiskAPI:
    '''
    Класс для работы с яндекс диском.
    '''

    def __init__(self, token):
        '''
        Инициализация класса с указанием Вашего токена.
        '''
        self.token = TOKEN

    def get_headers(self):
        '''
        Параметры запроса.
        '''
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_resp(self):
        '''
        Получение списка всех файлов в формате json.
        '''
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        resp = requests.get(url, headers=headers, timeout=5)
        # pprint(resp.json())
        return resp

    def get_upload_link(self, disk_file_path: str):
        '''
        Получение пути на яндекс.диск для загрузки Вашего файла.
        '''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params, timeout=10)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str):
        '''
        Загрузка файла на яндекс диск.
        '''
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        headers = self.get_headers()
        response = requests.put(href, data=open(disk_path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success!')




if __name__ == '__main__':

    TOKEN = '' # введите Ваш токен

    disk_path_to_file = os.path.abspath("...") # указывает полный путь к загружаемому файлу на Вашем ПК
    disk_file_path = "disk:/..." # вместо "..." введите имя файла с которым он будет сохранён

    test = YaDiskAPI(TOKEN)
    test.get_resp()
    test.get_upload_link(disk_file_path)
    test.upload_file_to_disk(disk_file_path)
