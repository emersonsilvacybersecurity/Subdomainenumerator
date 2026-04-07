#  Verificador de Subdomínios (DNS Enumerator)

Dando continuidade à minha série de projetos em **Python para Cybersecurity**, o sexto projeto foca na fase de **Reconhecimento Ativo (Recon)**. Enquanto os projetos anteriores focaram em identificar portas abertas e detectar ataques locais, este script permite mapear a **Superfície de Ataque (Attack Surface)** externa de um domínio alvo.

A enumeração de subdomínios é uma etapa crítica em Pentests e Bug Bounty, pois subdomínios esquecidos (como `dev.alvo.com` ou `teste.alvo.com`) costumam ser portas laterais com menos camadas de segurança que o domínio principal.

---

##  Destaques Técnicos
* **Integração com Wordlists:** Processamento de listas de termos customizáveis para Brute Force de DNS.
* **Automação de Requisições:** Uso da biblioteca `requests` para validar se o subdomínio não apenas existe, mas está respondendo ativamente.
* **Tratamento de Exceções:** Implementação de filtros para `ConnectionError` e `Timeout`, garantindo que o script não trave em hosts offline.
* **Arquitetura Limpa:** Separação entre a lógica de busca e os dados de entrada (Wordlists).

---

Aviso Legal (Disclaimer)
Este projeto possui fins estritamente educacionais e laboratoriais, desenvolvidos como parte da minha graduação em Segurança Cibernética. O uso desta ferramenta em domínios sem autorização prévia é de inteira responsabilidade do usuário e pode ser considerado ilegal.
