import requests
import urllib3
urllib3.disable_warnings()

class QaTestController:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def _get_headers(self):
        headers = {
            'Content-Type': 'application/json'
        }

        return headers

    def getUserById(self, endpoint, params=None):
        url = f'{self.baseUrl}/{endpoint}'
        try:
            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()

            status = response.status_code
            return status
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP ошибка: {http_err}')
        except Exception as err:
            print(f'Ошибка: {err}')

    def getUsersByGender(self, endpoint, params=None):
        url = f'{self.baseUrl}/{endpoint}'
        try:
            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()

            status = response.status_code
            return status
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP ошибка: {http_err}')
        except Exception as err:
            print(f'Ошибка: {err}')


