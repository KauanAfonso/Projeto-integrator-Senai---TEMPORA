import pandas as pd 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

caminho = "planilha_esteira.csv" #caminho do arquivp

arquivo_csv = pd.read_csv(caminho)
print(arquivo_csv)

#Exportando para excel e json
arquivo_csv.to_excel("Esteira.xlsx", index=False)
arquivo_csv.to_json("Esteira.json", index=False)

#criando o pdf
canva = canvas.Canvas("esteiras.pdf", pagesize=letter)

#desenhando o pdf(capa)
canva.drawString(x=240, y=700, text="SENAI ROBERTO MANGE")
canva.drawString(x=240, y=680, text="KAUAN AFONSO DA SILVA")
canva.drawString(x=125, y=421, text="PDF DE PRODUTOS NA ESTEIRA DA TEMPORA PARA DESPACHE")

canva.drawString(x=270, y=135, text="CAMPINAS")
canva.drawString(x=290, y=115, text="2024")
canva.showPage()

#definindo coordenadas para iteração
x = 120
y = 720


for i in arquivo_csv.iterrows():

    #------------------------- bordas--------------------------
    largura, altura = letter  

    # Adicionando uma borda ao redor da página
    espessura_borda = 2  

    canva.setStrokeColorRGB(0, 0, 0)  
    canva.setLineWidth(espessura_borda)  
    canva.rect(0, 0, largura, altura)  
    #------------------------Fim das bordas--------------------------


    #Conteudo do csv para a planilha
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
    y-=20

    canva.drawString(x, y, text=f"-------------------------------------------------------------------")

    y-=20

    if y <= 35:
        canva.showPage()
        y = 720
    
canva.save()