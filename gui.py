from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, Checkbutton, IntVar, messagebox
import pandas as pd
from comparer import Comparer

class ExcelCompareApp:
    def __init__(self, master):
        self.master = master
        master.title("Excel Compare App")

        self.file1_path = StringVar()
        self.file2_path = StringVar()
        self.comparison_options = {
            "item_number": IntVar(),
            "part_number": IntVar(),
            "item_name": IntVar(),
            "item_price": IntVar()
        }

        Label(master, text="Select Excel File 1:").grid(row=0, column=0)
        Button(master, text="Browse", command=self.load_file1).grid(row=0, column=1)

        Label(master, text="Select Excel File 2:").grid(row=1, column=0)
        Button(master, text="Browse", command=self.load_file2).grid(row=1, column=1)

        Label(master, text="Comparison Options:").grid(row=2, column=0, columnspan=2)

        Checkbutton(master, text="Item Number", variable=self.comparison_options["item_number"]).grid(row=3, column=0, sticky='w')
        Checkbutton(master, text="Part Number", variable=self.comparison_options["part_number"]).grid(row=4, column=0, sticky='w')
        Checkbutton(master, text="Item Name", variable=self.comparison_options["item_name"]).grid(row=5, column=0, sticky='w')
        Checkbutton(master, text="Item Price", variable=self.comparison_options["item_price"]).grid(row=6, column=0, sticky='w')

        Button(master, text="Compare", command=self.compare_files).grid(row=7, column=0, columnspan=2)

    def load_file1(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.file1_path.set(file_path)

    def load_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.file2_path.set(file_path)

    def compare_files(self):
        file1 = self.file1_path.get()
        file2 = self.file2_path.get()

        if not file1 or not file2:
            messagebox.showerror("Error", "Please select both files.")
            return

        options = {key: var.get() for key, var in self.comparison_options.items() if var.get()}

        if not options:
            messagebox.showerror("Error", "Please select at least one comparison option.")
            return

        comparer = Comparer(file1, file2, options)
        result_file = comparer.compare()
        messagebox.showinfo("Success", f"Comparison completed. Results saved to: {result_file}")

if __name__ == "__main__":
    root = Tk()
    app = ExcelCompareApp(root)
    root.mainloop()