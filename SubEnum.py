import requests
import sys

def verificar_subdominios(dominio_alvo, arquivo_wordlist):
    print(f"\n" + "="*50)
    print(f"🔍 BUSCANDO SUBDOMÍNIOS EM: {dominio_alvo}")
    print("="*50 + "\n")

    try:
        with open(arquivo_wordlist, "r") as arquivo:
            for linha in arquivo:
                subdominio = linha.strip()
                url = f"http://{subdominio}.{dominio_alvo}"
                
                try:
                    # Fazemos uma requisição rápida para checar se o host responde
                    requests.get(url, timeout=2)
                    print(f"[+] DISPONÍVEL: {url}")
                except requests.ConnectionError:
                    # Se não conectar, o subdomínio provavelmente não existe ou está offline
                    pass
                except requests.Timeout:
                    pass
    except FileNotFoundError:
        print(f"[!] ERRO: O arquivo {arquivo_wordlist} não foi encontrado.")

if __name__ == "__main__":
    # Exemplo de uso: python SubEnum.py google.com wordlist.txt
    if len(sys.argv) < 3:
        print("Uso: python SubEnum.py <dominio> <wordlist.txt>")
    else:
        verificar_subdominios(sys.argv[1], sys.argv[2])