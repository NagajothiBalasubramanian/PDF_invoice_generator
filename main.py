import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("*.xlsx")
print(filepaths)

for fp in filepaths:

    #Add invoice number and date
    Inv_name= Path(fp).stem
    Inv_number,Inv_date=Inv_name.split("-")
    pdf=FPDF(orientation='p',unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=20)
    pdf.cell(w=50, h=10, txt=f"Invoice nr:{Inv_number}",ln=1)
    pdf.set_font(family="Times",style="B",size=20)
    pdf.cell(w=50, h=10, txt=f"Date:{Inv_date}",ln=1)

    #Add table header
    df = pd.read_excel(fp, sheet_name="Sheet 1")
    columns = list(df.columns)
    columns =[item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times",size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=10,txt=columns[0],border=1)
    pdf.cell(w=50,h=10,txt=columns[1],border=1)
    pdf.cell(w=40,h=10,txt=columns[2],border=1)
    pdf.cell(w=30,h=10,txt=columns[3],border=1)
    pdf.cell(w=30,h=10,txt=columns[4],border=1,ln=1)

    #Add rows to table
    for index,row in df.iterrows():
        pdf.set_font(family="Times",size=10,)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30,h=10,txt=str(row["product_id"]),border=1,)
        pdf.cell(w=50,h=10,txt=str(row["product_name"]),border=1)
        pdf.cell(w=40,h=10,txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=10,txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30,h=10,txt=str(row["total_price"]),border=1,ln=1)

    #Add total value to table
    total_sum=df["total_price"].sum()
    pdf.set_font(family="Times", size=10, )
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=10, txt="", border=1,)
    pdf.cell(w=50, h=10, txt="", border=1)
    pdf.cell(w=40, h=10, txt="", border=1)
    pdf.cell(w=30, h=10, txt="", border=1)
    pdf.cell(w=30, h=10, txt=str(total_sum), border=1, ln=1)

    #Add total sentence below table
    pdf.set_font(family="Times", size=10,style="B" )
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=20, h=8, txt=f"The total amount of the products :{total_sum}",ln=1)

    #Add company name and logo
    pdf.set_font(family="Times", size=10,style="B" )
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=20, h=8, txt="pythonhow")
    pdf.image("pythonhow.png",w=10)

    pdf.output(f"PDF/{Inv_name}.pdf")