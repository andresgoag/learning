from fpdf import FPDF

WIDTH = 210
HEIGHT = 297


pdf = FPDF(orientation='P', unit='mm', format='A4') # A4 = 210mm x 297mm


pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Hello World!')


pdf.image("./img/fig1.png", x=10, y =10, w=WIDTH-20)



pdf.output('tuto1.pdf', 'F')