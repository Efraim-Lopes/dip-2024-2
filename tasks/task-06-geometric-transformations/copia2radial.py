import numpy as np

def apply_geometric_transformations(img: np.ndarray) -> dict:
    # YOUR IMPLEMENTATION HERE

    height, width = img.shape

    # 1. Translated Image (shift right and down)
    # Matriz de translação
    t_x, t_y = 20, 30  # Exemplo de deslocamento (20px à direita, 30px para baixo)
    translated = np.zeros_like(img)
    for y in range(height):
        for x in range(width):
            if 0 <= y + t_y < height and 0 <= x + t_x < width:
                translated[y + t_y, x + t_x] = img[y, x]

    # 2. Rotated Image (90 degrees clockwise)
    # Matriz de rotação (90 graus no sentido horário)
    rotated = np.rot90(img, -1)

    # 3. Horizontally Stretched Image (scale width by 1.5)
    # Matriz de escala
    scale_factor = 1.5
    new_width = int(width * scale_factor)
    stretched = np.zeros((height, new_width), dtype=img.dtype)
    for y in range(height):
        for x in range(new_width):
            orig_x = int(x / scale_factor)
            if orig_x < width:
                stretched[y, x] = img[y, orig_x]

    # 4. Horizontally Mirrored Image (flip along vertical axis)
    # Matriz de espelhamento
    mirrored = np.fliplr(img)

    # 5. Barrel Distorted Image (simple radial distortion)
    # Para distorção barrel, calculando manualmente a distorção radial
    distorted = np.zeros_like(img)
    center_y, center_x = height // 2, width // 2
    max_radius = min(center_x, center_y)
    for y in range(height):
        for x in range(width):
            dist_x = x - center_x
            dist_y = y - center_y
            dist = np.sqrt(dist_x**2 + dist_y**2)
            if dist < max_radius:
                factor = 1 - 0.005 * dist**2  # exemplo de distorção
                new_x = int(center_x + dist_x * factor)
                new_y = int(center_y + dist_y * factor)
                if 0 <= new_x < width and 0 <= new_y < height:
                    distorted[new_y, new_x] = img[y, x]

    return {
        "translated": translated,
        "rotated": rotated,
        "stretched": stretched,
        "mirrored": mirrored,
        "distorted": distorted
    }

import numpy as np
from PIL import Image  # Biblioteca Pillow para carregar imagens
import os

# Exemplo de uso:
if __name__ == "__main__":
    # Construir caminho da imagem corretamente
    img_path = "C:/Users/Efraim/Documents/EFRAIM/IC_-_UFAL/2024.2_PDI/dip-2024-2/img/baboon.png"

    img = Image.open(img_path).convert("L")  # "L" converte para escala de cinza
    img = np.array(img, dtype=np.uint8)  # Converte a imagem para um array NumPy

    # Aplicar as transformações
    result = apply_geometric_transformations(img)
    
    # Exibir as transformações com uma linha em branco entre elas
    for key, value in result.items():
        print(f"{key}:")
        print(value)
        print()  # Isso adiciona uma linha em branco entre as saídas

    # Criar a pasta results se não existir
    output_dir = os.path.join(os.path.dirname(__file__), "results")  # Cria dentro do diretório do script
    os.makedirs(output_dir, exist_ok=True)
    print(f"Salvando imagens em: {output_dir}")  # Teste para ver onde está salvando
    print(result.keys())  # Deve imprimir os nomes das transformações

    # Salvar as imagens transformadas
    for key, value in result.items():
        img_result = Image.fromarray(value)  # Converter array para imagem
        img_result.save(os.path.join(output_dir, f"result_{key}.png"))
    

""" 

# Exemplo de uso:
if __name__ == "__main__":
    # Carregar uma imagem em escala de cinza (usando np.random apenas como exemplo)
    img = np.random.randint(0, 255, (100, 100), dtype=np.uint8)

    # Aplicar as transformações
    result = apply_geometric_transformations(img)
    
    # Exibir as transformações com uma linha em branco entre elas
    for key, value in result.items():
        print(f"{key}:")
        print(value)
        print()  # Isso adiciona uma linha em branco entre as saídas"

"""
