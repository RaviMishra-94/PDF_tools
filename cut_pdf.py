import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox

def cut_pdf(input_path, output_path, start_page, end_page):
    pdf_document = fitz.open(input_path)
    pdf_writer = fitz.open()

    for page_num in range(start_page - 1, min(end_page, pdf_document.page_count)):
        pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    pdf_writer.save(output_path)
    pdf_writer.close()

class PDFCutterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Cutter")

        self.input_path_label = tk.Label(root, text="Input PDF:")
        self.input_path_label.grid(row=0, column=0, sticky=tk.E)

        self.input_path_entry = tk.Entry(root, width=30)
        self.input_path_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.start_page_label = tk.Label(root, text="Start Page:")
        self.start_page_label.grid(row=1, column=0, sticky=tk.E)

        self.start_page_entry = tk.Entry(root, width=5)
        self.start_page_entry.grid(row=1, column=1, padx=5, pady=5)

        self.end_page_label = tk.Label(root, text="End Page:")
        self.end_page_label.grid(row=1, column=2, sticky=tk.E)

        self.end_page_entry = tk.Entry(root, width=5)
        self.end_page_entry.grid(row=1, column=3, padx=5, pady=5)

        self.cut_button = tk.Button(root, text="Cut PDF", command=self.cut_pdf)
        self.cut_button.grid(row=2, column=1, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, file_path)

    def cut_pdf(self):
        input_path = self.input_path_entry.get()
        start_page = int(self.start_page_entry.get())
        end_page = int(self.end_page_entry.get())
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        try:
            cut_pdf(input_path, output_path, start_page, end_page)
            messagebox.showinfo("Success", "PDF pages cut successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCutterApp(root)
    root.mainloop()
