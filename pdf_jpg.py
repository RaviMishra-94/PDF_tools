import fitz  # PyMuPDF
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFToImagesConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to Images Converter")

        self.pdf_file_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="PDF File Path:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.master, textvariable=self.pdf_file_path, width=50).grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        tk.Button(self.master, text="Browse", command=self.browse_pdf_file).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.master, text="Output Folder Path:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.master, textvariable=self.output_folder_path, width=50).grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        tk.Button(self.master, text="Browse", command=self.browse_output_folder).grid(row=1, column=3, padx=5, pady=5)

        tk.Button(self.master, text="Convert to Images", command=self.convert_to_images).grid(row=2, column=0, columnspan=4, pady=10)

    def browse_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_file_path.set(file_path)

    def browse_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder_path.set(folder_path)

    def convert_to_images(self):
        pdf_path = self.pdf_file_path.get()
        output_folder = self.output_folder_path.get()

        if pdf_path and output_folder:
            pdf_to_images(pdf_path, output_folder)
            messagebox.showinfo("Conversion Complete", "PDF to Images conversion complete!")

def pdf_to_images(pdf_path, output_folder):
    # Rest of your original code for PDF to images conversion
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        pixmap = page.get_pixmap()
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        image_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
        image.save(image_path, format='JPEG', quality=95)
        print(f"Page {page_number + 1} saved as {image_path}")

    pdf_document.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToImagesConverter(root)
    root.mainloop()
