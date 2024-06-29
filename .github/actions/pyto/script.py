import os
import re

index_file_path = '/home/runner/work/luz-camera-actions/luz-camera-actions/otimizai_agronota_app/otimizai_agronota_app/build/web/index.html'

print(os.system('ls -la'))

print(os.system('pwd'))

with open(index_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(r'href="/*', 'href="./', content)


with open(index_file_path, 'w', encoding='utf-8') as file:
    file.write(content)