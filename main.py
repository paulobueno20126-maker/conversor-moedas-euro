import requests

def converter_moeda():
    # API gratuita para pegar cotações atualizadas
    url = "https://economia.awesomeapi.com.br/last/EUR-BRL"
    
    try:
        requisicao = requests.get(url)
        dados = requisicao.json()
        
        # Pega o valor de compra (bid) do Euro
        cotacao_euro = float(dados['EURBRL']['bid'])
        
        print("--- CONVERSOR EURO -> REAL (PLANO PELOTAS) ---")
        euros = float(input("Digite o valor em Euros (€) que quer poupar: "))
        reais = euros * cotacao_euro
        
        print(f"\nCom o Euro hoje a R$ {cotacao_euro:.2f}:")
        print(f"€ {euros:.2f} equivalem a R$ {reais:.2f} na conta da Wise.")
        
    except Exception as e:
        print("Erro ao conectar com a API. Verifica a tua internet.")

if __name__ == "__main__":
    converter_moeda()
