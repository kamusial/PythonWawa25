from datetime import datetime
from fpdf import FPDF
from pathlib import Path

from invoice_generator.model import load

pdf = FPDF()
pdf.add_page()

config = load("config.json")


# classic approach:
# arial_path = "/".join((__file__.split("\\")[:-1] + ["fonts", "Arial-Unicode.ttf"]))
# pathib.Path approach:
arial_path = Path(__file__).parent / "fonts" / "Arial-Unicode.ttf"
arial_italic_path = Path(__file__).parent / "fonts" / "Arial-Unicode.ttf"


pdf.add_font("arial", style="I", fname=arial_italic_path)
pdf.add_font("arial", style="", fname=arial_path)
pdf.set_font('arial', size=12)
pdf.cell(text="ORYGINAŁ", center=True)
pdf.ln(10)
pdf.set_font('arial', style="I", size=10)
pdf.cell(text="Sprzedawca/Podatnik: ")
pdf.set_font('arial', size=8)
pdf.cell(w=0, text=f"{config.company.city}, {datetime.today().strftime("%Y-%m-%d")}", align="R")
pdf.ln(5)
pdf.cell(text=config.company.name)
pdf.ln(5)
pdf.cell(text=config.company.address1)
pdf.ln(5)
pdf.cell(text=f"{config.company.postal_code}, {config.company.city}")
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="NIP: ")
pdf.set_font('arial', size=8)
pdf.cell(text=config.company.nip)
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="Bank: ")
pdf.set_font('arial', size=8)
pdf.cell(text=config.company.bank)
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="Konto: ")
pdf.set_font('arial', size=8)
pdf.cell(text=config.company.account)




pdf.output("hello_world.pdf")