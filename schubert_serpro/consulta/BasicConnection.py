import base64

import requests


class BasicConnection:
    CONNECTION_RETRY_LIMIT = 10

    def __init__(self, api_url: str, consumer_key: str, consumer_secret: str, connection_retry_limit=10):
        self.CONNECTION_RETRY_LIMIT = connection_retry_limit
        self.main_api_url = api_url
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.secret_enc = base64.b64encode(str(self.consumer_key + ":" + self.consumer_secret).encode()).decode()
        self.TOKEN_URL = self.main_api_url + "/token"
        self.CHECK_CPF_URL = self.main_api_url + "/consulta-cpf/v1/cpf/"
        self.CHECK_CNPJ_URL = self.main_api_url + "/consulta-cnpj/v1/cnpj/"
        self.bearer_token = None

    def get_auth_token(self):
        payload = "grant_type=client_credentials"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': "Basic " + self.secret_enc
        }
        for i in range(self.CONNECTION_RETRY_LIMIT):
            try:
                response = requests.post(self.TOKEN_URL, data=payload, headers=headers, timeout=1)
                response.raise_for_status()
            except Exception:
                self.bearer_token = ''
            else:
                self.bearer_token = response.json()['access_token']
                return True
        else:
            return False
