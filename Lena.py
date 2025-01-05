import numpy as np
from PIL import Image

def converter_para_cinza_numpy(imagem):
    """
    Converte uma imagem colorida para tons de cinza usando NumPy.

    Args:
        imagem (str): Caminho para a imagem.

    Returns:
        np.ndarray: Imagem em tons de cinza como um array NumPy.
    """

    # Carregar a imagem usando PIL
    img = Image.open(imagem).convert('RGB')
    # Converter para um array NumPy
    img_array = np.array(img)

    # Calcular a média ponderada dos canais RGB para obter o valor em tons de cinza
    # Pesos comuns: 0.299, 0.587, 0.114
    img_gray = 0.299 * img_array[:, :, 0] + 0.587 * img_array[:, :, 1] + 0.114 * img_array[:, :, 2]

    return img_gray

# Exemplo de uso
imagem = "lena.jpg"
img_cinza = converter_para_cinza_numpy(imagem)

# Salvar a imagem em tons de cinza (opcional)
img_cinza = Image.fromarray(img_cinza).convert('L')
img_cinza.save("lena_cinza.jpg")
