# Eliza, uma simples assistente pessoal para linux 
Feita com propósito de auxiliar tarefas no meu dia a dia no uso do linux

# Ações que Eliza faz:
    - salva e edita renomeia e exclui arquivos de texto e diretórios
    - toca músicas
    - localiza onde você está
    - checa o seu IP externo
    - checa o clima de uma cidade
    - checa a cotação do Dolar, Euro e BTC
    - Envia emails com as novidades e promoções de sites
    
# Testado nos sistemas:
- ubuntu
- kali linux
- deepin linux

# Versão do python
- 2.7

# Download
    ~$ git clone https://github.com/tarcisio-marinho/Eliza.git

# Execução normal
    ~$ python main.py

# Primeira vez rodando
Para pular todos os passos abaixo, execute o arquivo compilador.sh:

     ~$ chmod +x compilar.sh

     ~$ ./compilar.sh

porém se desejar fazer manualmente, siga os passos abaixo:
é necessário instalar o instalador de modulos do python, o pip para poder instalar a biblioteca requests.

Você pode baixar manualmente seguindo os comandos :

     ~$ sudo apt-get update 

     ~$ sudo apt-get install python-pip

     ~$ sudo apt-get install espeak

     ~$ pip install requests

     depois você precisa tornar executável os scripts:

     ~$ chmod +x esvaziar.sh tocar.sh teste.sh



# Digite ajuda para obter ajuda
