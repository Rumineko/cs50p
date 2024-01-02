from fpdf import FPDF

class Convert:
    def __init__(self, name):
        name = self.name

    @classmethod
    def convert(cls, name):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_margin(0)
        pdf.add_page()
        pdf.set_font('Times', 'B', 30)
        pdf.cell(h=60, text="CS50 Shirtificate", align="C", center=True)
        pdf.image("shirtificate.png", x="C", y=60, w=180, h=180)
        pdf.set_text_color(r=255, g=255, b=255)
        pdf.set_font('Times', 'B', 20)
        pdf.cell(h=220, text=f"{name} took CS50", align="C", center=True)
        pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    Convert.convert(name)


if __name__ == "__main__":
    main()
