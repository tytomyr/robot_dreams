import requests


AUTH_TOKEN = '2b8d97ce57d401abd89f45b0079d8790edd940e6'



class GetDataFromAPI:
    def __init__(self):
        self.purchase_list = None
        self.status_code = None

    def main(self):

        response = requests.get(
            url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
            params={'date': '2022-08-09', 'page': 2},
            headers={'Authorization': AUTH_TOKEN},
        )
        self.status_code = response.status_code
        self.purchase_list = response.json()


