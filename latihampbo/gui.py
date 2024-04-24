import tkinter as tk
from tkinter import filedialog

class TextEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Text Editor")
        self.master.geometry("800x800")
        self.master.minsize(800, 800)
        
        self.create_widgets()
    
    def create_widgets(self):
        self.text_area = tk.Text(self.master)
        self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        frame = tk.Frame(self.master)
        frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.open_button = tk.Button(frame, text="Open", command=self.open_file)
        self.open_button.pack(fill=tk.X)
        
        self.save_button = tk.Button(frame, text="Save", command=self.save_file)
        self.save_button.pack(fill=tk.X)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                text_content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, text_content)
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                text_content = self.text_area.get(1.0, tk.END)
                file.write(text_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
