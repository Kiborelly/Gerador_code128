from barcode import Code128
from barcode.writer import ImageWriter
import datetime
import os

texto_para_codificar = "Digite o texto aqui!"

caminho = "/storage/emulated/0/Documents/Pydroid3"
contador = 1
lista_arquivos = os.listdir(caminho)
data_hora = datetime.date.today()
nome_arquivo = f"{texto_para_codificar}_{data_hora.strftime('%d-%m-%Y')}.png"

def gerador_code128(texto_codificar, arquivo):
  code128 = Code128(texto_codificar, writer=ImageWriter())
  code128_image = code128.render()
  with open(arquivo, 'wb') as f:
    code128_image.save(f)

for arquivo in lista_arquivos:
    if arquivo == nome_arquivo:
    	contador += 1
    	nome_arquivo =  f"{texto_para_codificar}_{data_hora.strftime('%d-%m-%Y')} v{contador}.png"

gerador_code128(texto_para_codificar, nome_arquivo)

print(f"Codigo {nome_arquivo} gerado com sucesso")
