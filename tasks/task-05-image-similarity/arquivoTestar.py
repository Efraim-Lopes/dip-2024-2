import numpy as np
from image_similarity_exercise import compare_images

##########################
# criar imagens de teste #
##########################

#imagens normais

np.random.seed(42)  # pra garantir reprodutibilidade
# Criar imagem base com valores entre 0 e 1
img1 = np.random.rand(100, 100)
# Criar imagem parecida, com pequeno ruído
noise = np.random.normal(loc=0.0, scale=0.01, size=(100, 100))  # ruído pequeno
img2 = np.clip(img1 + noise, 0, 1)  # somar ruído e manter entre 0 e 1


#imagens invertidas

# np.random.seed(22210867)  # garante reprodutibilidade
# # Imagem aleatória normalizada entre 0 e 1
# img1 = np.random.rand(64, 64)
# # Inversão dos pixels (valores altos viram baixos e vice-versa)
# img2 = 1.0 - img1

#Chamar a função
result = compare_images(img1, img2)

#Exibir os resultados
print("Resultados da comparação:")
for key, value in result.items():
    print(f"{key}: {value}")

