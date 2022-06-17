from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader


# Crear nueva instancia de PDF
canvas = canvas.Canvas("example.pdf", pagesize=A4) # A4 = 210mm * 297mm
# Set font
canvas.setFont("Helvetica", 12)
# Poner texto coordenada x: desde la izquierda, coordenada y: desde abajo
canvas.drawString(20*mm, 280*mm, "Primer texto")
# Insertar imagen
logo = ImageReader("https://picsum.photos/500/500")
logo_width = 200
canvas.drawImage(logo, 20*mm, 100*mm, preserveAspectRatio=True)
# Guardar el pdf
canvas.save()