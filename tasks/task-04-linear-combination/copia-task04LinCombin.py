import cv2
import os

# Função para tentar carregar a imagem com várias extensões
def load_image_by_name(image_name):
    extensions = ['.jpg', '.jpeg', '.png', '.bmp']  # Lista de extensões suportadas
    for ext in extensions:
        file_name = image_name + ext
        if os.path.exists(file_name):  # Verifica se o arquivo existe
            img = cv2.imread(file_name)
            if img is not None:
                return img, file_name  # Retorna a imagem carregada e o nome do arquivo
    return None, None  # Se nenhuma imagem foi encontrada

# Tentar carregar as duas imagens
img1, img1_path = load_image_by_name('image1')
img2, img2_path = load_image_by_name('image2')

# Verificar se as imagens foram carregadas corretamente
if img1 is None or img2 is None:
    print("Erro ao carregar as imagens. Verifique se 'image1' e 'image2' estão presentes no diretório.")
else:
    # Redimensionar img2 para ter o mesmo tamanho de img1
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Combinação linear das imagens
    alpha = 0.5  # Peso da primeira imagem
    beta = 1 - alpha  # Peso da segunda imagem
    result = cv2.addWeighted(img1, alpha, img2, beta, 0)

    # Determinar o tipo de imagem baseado na extensão da primeira imagem carregada
    img_type = img1_path.split('.')[-1]  # Extrai o tipo da imagem pela extensão do arquivo

    # Salvar a imagem resultante com o mesmo formato da primeira imagem
    output_path = f'result.{img_type}'
    cv2.imwrite(output_path, result)

    # Exibir a imagem resultante
    cv2.imshow('Linear Combination', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
