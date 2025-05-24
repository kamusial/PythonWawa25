from datetime import datetime, timedelta

from fpdf import FPDF

from invoice_generator import fonts
from invoice_generator.model import load, InvoiceConfig


def header(pdf: FPDF, config: InvoiceConfig):
    pdf.cell(text="ORYGINAŁ", center=True)
    pdf.ln(10)
    fonts.italic(pdf, 10)
    pdf.cell(text="Sprzedawca/Podatnik: ")
    fonts.normal(pdf, 6)
    pdf.cell(w=0, text=f"{config.company.city}, {datetime.today().strftime("%Y-%m-%d")}", align="R")
    pdf.ln(5)
    pdf.cell(text=config.company.name)
    pdf.ln(3)
    pdf.cell(text=config.company.address)
    pdf.ln(3)
    pdf.cell(text=f"{config.company.postal_code}, {config.company.city}")
    fonts.italic(pdf, size=6)
    pdf.ln(3)
    pdf.cell(text="NIP: ")
    fonts.normal(pdf, 6)
    pdf.cell(text=config.company.nip)
    pdf.ln(3)
    fonts.normal(pdf, 8)
    pdf.cell(w=0, text=f"Bank: {config.account.bank_name}", align="R")
    pdf.ln(5)
    pdf.cell(w=0, text=f"Konto: {config.account.number} {config.account.currency}", align="R")
    pdf.ln(12)
    pdf.cell(w=0, text="_" * 135)
    pdf.ln(10)


def buyer_asset(pdf: FPDF, key: str, value: str):
    fonts.italic(pdf)
    pdf.cell(w=20, text=key)
    fonts.normal(pdf, size=6)
    pdf.cell(text=value)
    pdf.ln(3)


def buyer(pdf: FPDF, config: InvoiceConfig):
    buyer_asset(pdf, "Nabywca: ", config.invoice.company.name)
    buyer_asset(pdf, "NIP: ", config.invoice.company.nip)
    buyer_asset(pdf, "REGON: ", config.invoice.company.regon)
    buyer_asset(pdf, "Sposób zapłaty: ", config.invoice.payment_method)
    paid_until = datetime.today() + timedelta(days=config.invoice.payment_period)
    buyer_asset(pdf, "Płatne do dnia: ", paid_until.strftime("%Y-%m-%d"))
    pdf.ln(10)


def table_cell(pdf: FPDF, w: int, text: str, new_x="RIGHT", new_y="LAST"):
    pdf.multi_cell(w=w, border=1, padding=2, align="C", new_x=new_x, new_y=new_y, text=text)
    pdf.y -= 2

def items(pdf: FPDF, config: InvoiceConfig):
    fonts.normal(pdf, size=8)
    table_cell(pdf, 100, "Nazwa")
    table_cell(pdf, 20, "% VAT")
    table_cell(pdf, 30, "Cena NETTO")
    table_cell(pdf, 30, "Cena BRUTTO", new_x="LMARGIN", new_y="NEXT")
    pdf.y += 2

    total = 0
    for item in config.items:
        table_cell(pdf, 100, item.name)
        table_cell(pdf, 20, str(item.tax))
        table_cell(pdf, 30, f"{'%.2f' % item.net} {config.account.currency}")
        gross = item.net * (1 + item.tax / 100)
        total += gross
        table_cell(pdf, 30, f"{"%.2f" % round(gross, 2)} {config.account.currency}",  new_x="LMARGIN", new_y="NEXT")
        pdf.y += 2

    pdf.ln(10)
    fonts.bold(pdf, size=15)
    pdf.cell(text=f"Do zapłaty: {"%.2f" % round(total, 2)} {config.account.currency}")


def main():
    pdf = FPDF()
    pdf.add_page()
    config = load("config.json")
    fonts.create(pdf)

    fonts.normal(pdf, 12)
    header(pdf, config)
    buyer(pdf, config)
    items(pdf, config)

    pdf.output("invoice.pdf")


if __name__ == '__main__':
    main()