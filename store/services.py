import requests


def consultar_cep(cep):
    cep = cep.replace('-', '')

    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get(
        url,
        timeout=5
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get('erro'):
        return None

    return data