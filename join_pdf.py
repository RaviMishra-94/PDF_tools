from tkinter import Tk, Label, Button, filedialog
from PyPDF2 import PdfReader, PdfWriter

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")

        self.label1 = Label(root, text="First PDF:")
        self.label1.grid(row=0, column=0)

        self.label2 = Label(root, text="Second PDF:")
        self.label2.grid(row=1, column=0)

        self.first_pdf_path = ""
        self.second_pdf_path = ""

        self.button1 = Button(root, text="Browse", command=self.browse_first_pdf)
        self.button1.grid(row=0, column=1)

        self.button2 = Button(root, text="Browse", command=self.browse_second_pdf)
        self.button2.grid(row=1, column=1)

        self.merge_button = Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.grid(row=2, column=0, columnspan=2, pady=10)

    def browse_first_pdf(self):
        self.first_pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    def browse_second_pdf(self):
        self.second_pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    def merge_pdfs(self):
        if self.first_pdf_path and self.second_pdf_path:
            output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

            try:
                pdf_reader1 = PdfReader(self.first_pdf_path)
                pdf_reader2 = PdfReader(self.second_pdf_path)
                pdf_writer = PdfWriter()

                for reader in [pdf_reader1, pdf_reader2]:
                    for page_number in range(len(reader.pages)):
                        page = reader.pages[page_number]
                        pdf_writer.add_page(page)

                with open(output_pdf_path, 'wb') as output_file:
                    pdf_writer.write(output_file)

                Label(self.root, text="PDFs merged successfully!").grid(row=3, column=0, columnspan=2)

            except Exception as e:
                Label(self.root, text=f"An error occurred: {e}").grid(row=3, column=0, columnspan=2)
        else:
            Label(self.root, text="Please select both PDFs.").grid(row=3, column=0, columnspan=2)

if __name__ == "__main__":
    root = Tk()
    app = PDFMergerApp(root)
    root.mainloop()