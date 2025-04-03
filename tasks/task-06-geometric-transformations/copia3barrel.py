import numpy as np

def barrel_distortion(img: np.ndarray, k: float = 0.1) -> np.ndarray:
    """
    Aplica a distorção barrel (em barril) a uma imagem.
    
    Parâmetros:
        img: np.ndarray - Imagem em escala de cinza como um array NumPy.
        k: float - Coeficiente de distorção (valores positivos aumentam a distorção).

    Retorna:
        np.ndarray - Imagem distorcida.
    """
    height, width = img.shape
    center_y, center_x = height // 2, width // 2
    
    # Criar uma nova imagem preta (mesmo tamanho)
    distorted = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            # Coordenadas em relação ao centro
            norm_x = (x - center_x) / center_x
            norm_y = (y - center_y) / center_y
            r = np.sqrt(norm_x**2 + norm_y**2)

            # Aplicar distorção radial
            factor = 1 + k * r**2  

            # Transformar de volta para coordenadas originais
            src_x = int(center_x + norm_x * factor * center_x)
            src_y = int(center_y + norm_y * factor * center_y)

            # Verificar se a posição original está dentro dos limites
            if 0 <= src_x < width and 0 <= src_y < height:
                distorted[y, x] = img[src_y, src_x]

    return distorted

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

    # 5. Barrel Distorted Image
    distorted = barrel_distortion(img)

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
