from datetime import datetime, timedelta

from fpdf import FPDF

from invoice_generator import fonts
from invoice_generator.model import load, InvoiceConfig


def header(pdf: FPDF, config: InvoiceConfig):
    pdf.cell(text="ORYGINAŁ", center=True)
    pdf.ln(10)
    fonts.italic(pdf, 10)
    pdf.cell(text="Sprzedawca/Podatnik: ")
    fonts.normal(pdf, 8)
    pdf.cell(w=0, text=f"{config.company.city}, {datetime.today().strftime("%Y-%m-%d")}", align="R")
    pdf.ln(5)
    pdf.cell(text=config.company.name)
    pdf.ln(5)
    pdf.cell(text=config.company.address)
    pdf.ln(5)
    pdf.cell(text=f"{config.company.postal_code}, {config.company.city}")
    fonts.italic(pdf, size=6)
    pdf.ln(5)
    pdf.cell(text="NIP: ")
    fonts.normal(pdf, 8)
    pdf.cell(text=config.company.nip)
    pdf.ln(5)
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


def main():
    pdf = FPDF()
    pdf.add_page()
    config = load("config.json")
    fonts.create(pdf)

    fonts.normal(pdf, 12)
    header(pdf, config)
    buyer(pdf, config)

    pdf.output("invoice.pdf")


if __name__ == '__main__':
    main()