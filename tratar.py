import json

# Caminho para o arquivo JSON original e para o novo arquivo com as chaves em letras maiúsculas
jsonFilePath = 'caminho_para_seu_arquivo.json'
newJsonFilePath = 'caminho_para_seu_novo_arquivo.json'

# Ler o arquivo JSON
with open(jsonFilePath, 'r', encoding='utf-8') as jsonf:
    data = json.load(jsonf)

# Converter as chaves para maiúsculas
data_uppercase = {key : value.upper() for key, value in data.items()}

# Escrever o arquivo JSON com as chaves em letras maiúsculas
with open(newJsonFilePath, 'w', encoding='utf-8') as jsonf:
    json.dump(data_uppercase, jsonf, indent=4, ensure_ascii=False)
