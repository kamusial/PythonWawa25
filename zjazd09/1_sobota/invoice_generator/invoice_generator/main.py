import json
from fpdf import FPDF
from pathlib import Path


pdf = FPDF()
pdf.add_page()

with open("config.json", encoding="UTF-8") as config_file:
    config = json.load(config_file)


# classic approach:
# arial_path = "/".join((__file__.split("\\")[:-1] + ["fonts", "Arial-Unicode.ttf"]))
# pathib.Path approach:
arial_path = Path(__file__).parent / "fonts" / "Arial-Unicode.ttf"
arial_italic_path = Path(__file__).parent / "fonts" / "Arial-Unicode.ttf"
pdf.add_font("arial", style="", fname=arial_path)
pdf.add_font("arial", style="I", fname=arial_italic_path)
pdf.set_font('arial', size=12)
pdf.cell(text="ORYGINAŁ", center=True)
pdf.ln(10)
pdf.set_font('arial', style="I", size=10)
pdf.cell(text="Sprzedawca/Podatnik: ")
pdf.set_font('arial', size=8)
pdf.cell(w=0, text=f"Warszawa, 24.05.2025", align="R")
pdf.ln(5)
pdf.cell(text=config["company"]["name"])
pdf.ln(5)
pdf.cell(text="address1")
pdf.ln(5)
pdf.cell(text=f"{config['company']['postal_code']}, {config['company']['city']}")
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="NIP: ")
pdf.set_font('arial', size=8)
pdf.cell(text="645651651")
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="Bank: ")
pdf.set_font('arial', size=8)
pdf.cell(text="Santander Bank Polska")
pdf.set_font('arial', style="I", size=10)
pdf.ln(5)
pdf.cell(text="Konto: ")
pdf.set_font('arial', size=8)
pdf.cell(text="561 615 156 156 615 156 156 156 156")


pdf.output("hello_world.pdf")