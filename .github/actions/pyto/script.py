import os
import re

index_file_path = '/build/web/index.html'

# muda o diretório uma pasta acima
os.chdir('..')

print(os.system('ls -la'))

print(os.system('pwd'))

with open(index_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(r'href="/*', 'href="./', content)


with open(index_file_path, 'w', encoding='utf-8') as file:
    file.write(content)