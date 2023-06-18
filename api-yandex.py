import json
from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        file_name = os.path.basename(file_path)
        params = {
             "path": file_name,
             "overwrite" : "true"
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:
            # print(response.status_code)
            # pprint(response.json())
            url_upload = response.json()['href']
            with open(file_path, 'rb') as file:
                response2 = requests.put(url_upload, files={"file": file})
                print(response2.status_code)
        else:
            print(response.status_code)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь к загружаемому файлу: ")
    token = f"OAuth {input('Введите свой токен: ')}"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)