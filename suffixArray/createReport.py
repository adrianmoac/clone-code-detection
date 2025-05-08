from reportlab.pdfgen import canvas 

def getReport(maxLcps, similarity):
  """
  Create the report with similarity percentage and similar lines of code.
  """

  fileName = 'reportSuffixArray.pdf'
  documentTitle = 'Similarities Scan Report'
  title = 'Similarities Scan Report'
  subTitle = f'%{similarity}'

  # Create canvas
  pdf = canvas.Canvas(fileName)
  pdf.setTitle(documentTitle)

  pdf.setFont("Courier-Bold", 28)
  pdf.drawCentredString(300, 770, title)

  pdf.setFont("Courier", 24)
  pdf.drawCentredString(290, 720, subTitle)
  pdf.line(30, 710, 550, 710)

  y = 680 
  line_height = 18 

  pdf.setFont("Courier-Bold", 8)
  pdf.drawString(40, 700, 'Similarities in both codes:')
  pdf.setFont("Courier", 8)
  
  # For each line, verify if the position is inside the pdf page, if not, add it to a new page
  for line in maxLcps:
    if y < 40:
      pdf.showPage()
      y = 800
      pdf.setFont("Courier", 8)

    pdf.drawString(40, y, line)
    y -= line_height

  print('Report created in ./reportSuffixArray.pdf')
  pdf.save()
