import os

def check_encoding(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.sql', '.yml', '.yaml', '.md')):
                path = os.path.join(root, file)
                try:
                    with open(path, encoding='utf-8') as f:
                        f.read()
                except UnicodeDecodeError:
                    print(f"Arquivo com problema de encoding: {path}")

check_encoding('models')
check_encoding('.')
