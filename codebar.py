from reportlab.graphics import renderPDF  # generer le fichier pdf
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen.canvas import Canvas
import random

# develop app
def eanbc_demo(barcode_values):
    mycanvas = Canvas(f'barcode{random.randint(000,100)}.pdf')
    # draw the eanbc8 code (dessiner le code barre avec 8 chiffres)
    barcode_eanbc8 = eanbc.Ean8BarcodeWidget(12345678)
    bounds = barcode_eanbc8.getBounds()
    d_ = Drawing(10, 10)
    d_.add(barcode_eanbc8)
    renderPDF.draw(d_, mycanvas, 15, 555)
    mycanvas.setFont('Helvetica', 19)  # choisi
    mycanvas.setFillColor('aqua')  # ajouter une couleur de fond
    mycanvas.setStrokeColorRGB(255, 0.5, 0.5, alpha=0.5)  # ajouter une couleur dans la ligne
    mycanvas.setAuthor('Beneche Nelson')  # ajouter une auteur pour le document
    mycanvas.drawString(200, 750, 'Barcode')
    mycanvas.setCreator('barcode de Beneche Nelson')
    mycanvas.save()

if __name__ == '__main__':
    eanbc_demo(12345678)



