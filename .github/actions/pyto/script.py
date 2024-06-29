import os
import re

index_file_path = 'otimizai_agronota_app/otimizai_agronota_app/build/web/index.html'

with open(index_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(r'href="/*', 'href="./', content)


with open(index_file_path, 'w', encoding='utf-8') as file:
    file.write(content)