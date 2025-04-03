import numpy as np
from PIL import Image
import os
from copia2resposta import apply_geometric_transformations  # Importe sua função

img_path = "C:/Users/Efraim/Documents/EFRAIM/IC_-_UFAL/2024.2_PDI/dip-2024-2/img/baboon.png"

img = Image.open(img_path).convert("L")  # "L" converte para escala de cinza
img = np.array(img, dtype=np.uint8)  # Converte a imagem para um array NumPy

# Aplicar as transformações
result = apply_geometric_transformations(img)

# Criar a pasta results se não existir
output_dir = os.path.join(os.path.dirname(__file__), "results")  # Cria results no mesmo local onde esta o codigo
os.makedirs(output_dir, exist_ok=True)
print(f"Salvando imagens em: {output_dir}")  # para ver onde está salvando
print(result.keys())  # imprimir os nomes das transformações

# Salvar as imagens transformadas
for key, value in result.items():
    output_path = os.path.join(output_dir, f"result_{key}.png")
    Image.fromarray(value).save(output_path)

# Exibir as transformações com uma linha em branco entre elas
for key, value in result.items():
    print(f"{key}:")
    print(value)
    print()  # Isso adiciona uma linha em branco entre as saídas

print("Test completed! Check the 'results' folder.")