import os
from datetime import datetime
os.getcwd() # diretorio atual
os.chdir('/home/tarcisio/Desktop/') # troca de diretorio
os.listdir() # lista o que tiver dentro do diretorio
os.makedirs('nome/nome2/nome3') # cria diretorios dentro de diretorios
os.mkdir('nome') # cria o diretorio sem possibilidade de criar outros
os.rmdir('nome') # remove diretorio
os.rename('nome.txt','nome2.txt') # renomeia o arquivo
os.stat('arquivo.txt'.st_size) # tamanho do arquivo

a=os.stat('arquivo.txt').st_mtime
datetime.fromtimestamp(a) # ultima alteracao do arquivo

os.path.isdir('diretorio') # retorna true se for um diretorio
os.path.isfile('arquivo') # retorna true se for um arquivo

os.path.splitext('/etc/arquivo.txt') # separa e extensao .txt do restante do arquivo

