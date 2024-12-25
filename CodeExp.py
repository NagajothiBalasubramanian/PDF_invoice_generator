import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text/*.txt")
pdf=FPDF(orientation="p",unit="mm",format="A4")

for fp in filepaths:
    pdf.add_page()

    #Add title
    filename = Path(fp).stem
    name=filename.title()
    pdf.set_font(family="Times",style="B",size=20)
    pdf.cell(w=20,h=10,txt=name,ln=1)

    #Add Content
    with open(fp,"r") as file:
        content=file.read()
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0,h=10,txt=content)

pdf.output("Output.pdf")