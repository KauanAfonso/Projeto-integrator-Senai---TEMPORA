import pandas as pd 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

caminho = "planilha_esteira.csv"

arquivo_csv = pd.read_csv(caminho)
print(arquivo_csv)

#Exportando para excel e json
arquivo_csv.to_excel("Esteira.xlsx", index=False)
arquivo_csv.to_json("Esteira.json", index=False)

#criando o pdf
x = 120
y = 720



canva = canvas.Canvas("esteiras.pdf", pagesize=letter)
canva.drawString(x=120, y=750, text="PDF DE PRODUTOS NA ESTEIRA DA TEMPORA PARA DESPACHE")
canva.drawString(x, y, text=f"-------------------------------------------------------------------")




for i in arquivo_csv.iterrows():

    largura, altura = letter  # Pega as dimensões da página

    # Adicionando uma borda ao redor da página
    espessura_borda = 2  
    # Desenhando a borda 
    canva.setStrokeColorRGB(0, 0, 0)  
    canva.setLineWidth(espessura_borda)  
    canva.rect(0, 0, largura, altura)  

    linha = i[1]
    esteira1 = linha.Esteira1
    esteira2 = linha.Esteira2
    esteira3 = linha.Esteira3
    data = linha.Data

    y-=20

    canva.drawString(x, y, text=f"O valor da esteira 1 é {esteira1} na data {data}")
    y-=20
    canva.drawString(x, y, text=f"O valor da esteira 2 é {esteira2} na data {data}")
    y-=20
    canva.drawString(x, y, text=f"O valor da esteira 3 é {esteira3} na data {data}")
    # x -=1
    y-=20

    canva.drawString(x, y, text=f"-------------------------------------------------------------------")

    y-=20

    if y <= 35:
        canva.showPage()
        y = 720
    
    

canva.save()