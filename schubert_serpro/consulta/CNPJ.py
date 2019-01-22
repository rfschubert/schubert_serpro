import json

import requests
from pycpfcnpj import cpfcnpj

from schubert_serpro.consulta.BasicConnection import BasicConnection


class CNPJ(BasicConnection):

    def get(self, cnpj):
        # checa se CNPJ tem numero valido
        if cpfcnpj.validate(cnpj):
                # remove mascara do CNPJ se veio mascarado
                unmasked_cnpj = cpfcnpj.clear_punctuation(cnpj)
                if self.get_auth_token():
                    url = self.CHECK_CPF_URL + unmasked_cnpj
                    headers = {
                        'Authorization': 'Bearer ' + self.bearer_token,
                        'Accept': 'application/json'
                    }
                    # tenta se conectar na API por X vezes antes de efetuar um raise de erro
                    for i in range(self.CONNECTION_RETRY_LIMIT):
                        try:
                            response = requests.get(url, headers=headers, timeout=1)
                            response.raise_for_status()
                        except Exception:
                            continue
                        else:
                            # retorna dicionario com informacoes da SERPRO
                            return json.loads(response.text)
                    else:
                        raise ConnectionError("Nao foi possivel se conectar na SERPRO")
                else:
                    raise ConnectionError("Nao foi possivel gerar o Bearer Token")
        else:
            raise ValueError('Numero de CNPJ invalido')
