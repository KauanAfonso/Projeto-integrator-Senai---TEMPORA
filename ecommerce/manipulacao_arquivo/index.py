import pandas as p
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#caminho onde está o arquivo
caminho = "planilha_esteira.csv"

df = p.read_csv(caminho)
print(df)