from pathlib import Path

from fpdf import FPDF
from fpdf.enums import TextEmphasis


def create(pdf: FPDF):
    # classic approach:
    # arial_path = "/".join((__file__.split("\\")[:-1] + ["fonts", "Arial-Unicode.ttf"]))
    # pathib.Path approach:
    arial_path = Path(__file__).parent / "fonts" / "ARIAL.ttf"
    arial_italic_path = Path(__file__).parent / "fonts" / "ARIALI.TTF"
    arial_bold_path = Path(__file__).parent / "fonts" / "ARIALBD.TTF"

    pdf.core_fonts_encoding = "utf-8"
    pdf.add_font("arial", style="I", fname=arial_italic_path)
    pdf.add_font("arial", style="", fname=arial_path)
    pdf.add_font("arial", style="B", fname=arial_bold_path)


def normal(pdf: FPDF, size: int = 6):
    pdf.set_font('arial', size=size)


def bold(pdf: FPDF, size: int = 6):
    pdf.set_font('arial', style="B", size=size)



def italic(pdf: FPDF, size: int = 6):
    pdf.set_font("arial", style="I", size=size)
