import json

import requests
from pycpfcnpj import cpfcnpj

from schubert_serpro.consulta.BasicConnection import BasicConnection


class CPF(BasicConnection):

    def get(self, cpf):
        # checa se CPF tem numero valido
        if cpfcnpj.validate(cpf):
                # remove mascara do cpf se veio mascarado
                unmasked_cpf = cpfcnpj.clear_punctuation(cpf)
                if self.get_auth_token():
                    url = self.CHECK_CPF_URL + unmasked_cpf
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
            raise ValueError('Numero de CPF invalido')
