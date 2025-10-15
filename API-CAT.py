import requests

def pegar_info_racas():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)

    if response.status_code == 200:
        racas = response.json()
        for raca in racas[:5]:
            nome = raca.get('name', 'N/A')
            origem = raca.get('origin', 'N/A')
            descricao = raca.get('description', 'N/A')
            print(f"Raça: {nome}")
            print(f"Origem: {origem}")
            print(f"Descrição: {descricao}\n")
    else:
        print(f"Erro ao acessar API: {response.status_code}")

if __name__ == "__main__":
    pegar_info_racas()