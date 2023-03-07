import requests
from pprint import pprint


# curl -X GET --header 'Accept: application/json' --header 'Authorization: OAuth y0_AgAAAABjwBvtAADLWwAAAADcQTVQXtW170XrTnmM1DrlJlWJmY_A0dM' 'https://cloud-api.yandex.net/v1/disk'


class YaUploader:
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, access_token: str):
        self.token = access_token

    def auth_headers(self):
        return {'Authorization': f'OAuth {access_token}'}

    def get_upload_link(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(self.upload_url, params=params, headers=self.auth_headers())
        pprint(response.json())
        return response.json()
        # Тут ваша логика
        # Функция может ничего не возвращать


    def upload(self, file_path):
        href = self.get_upload_link(file_path).get('href')
        if not href:
            print('Пусто!')
            return
        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print('файл загружен')
                return True
            else:
                print('файл не загружен, код ошибки: ', response.status_code)
                return False

        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = 'krasivyj-border-kolli-1525426403.jpeg'
    access_token = 'y0_AgAAAABjwBvtAADLWwAAAADcQTVQXtW170XrTnmM1DrlJlWJmY_A0dM'
    uploader = YaUploader(access_token)
    result = uploader.upload(file_path)
    print('All working')

