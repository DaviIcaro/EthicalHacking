**EthicalHacking**

**Made by:**[Davi Icaro](https://www.linkedin.com/in/davi-icaro/)

# Descrição

**Esse programa em Python busca as senhas de redes Wi-Fi salvas em um computador Windows e as envia para um webhook. Para isso, utiliza bibliotecas padrão do Python, como o "subprocess" para executar um comando do sistema operacional, o "os" para acessar o diretório atual e o "requests" para enviar uma requisição HTTP para um URL específico.**

**O programa começa definindo a URL do webhook para onde as informações serão enviadas. Em seguida, cria um arquivo chamado "passwords.txt" para armazenar as senhas das redes Wi-Fi encontradas. O programa utiliza o comando "netsh" para exportar os perfis de rede Wi-Fi, que são salvos em arquivos XML no diretório atual. O programa então lê cada arquivo XML e extrai as informações de nome e senha de cada rede Wi-Fi. As informações são adicionadas ao arquivo "passwords.txt", que é posteriormente enviado para o webhook especificado.**

# Exemplo de output

**Um exemplo de output seria um arquivo de texto chamado "passwords.txt" que contém as seguintes informações:**

**Hello sir! Here are you passwords:**  

**SSID: Wi-Fi da Casa**
**Password: minha_senha_wifi**

**SSID: Wi-Fi do Trabalho
Password: senha_do_trabalho_wifi**

**DETALHE: "SSID" é o "Nome do Wifi"  e "Password" é a senha.**

# ATENÇÃO!!

**As informações acima representam os nomes e senhas das redes Wi-Fi encontradas e são enviadas para o webhook especificado no código Python. É importante ressaltar que o código acima é apenas um exemplo e não deve ser utilizado para fins ilegais ou sem a devida autorização.**

