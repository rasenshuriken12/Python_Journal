# Tkinter GUI Framework

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

class TkinterDemo:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Python GUI Demo")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Variables
        self.counter = 0
        self.text_var = tk.StringVar()
        self.check_var = tk.BooleanVar()
        self.radio_var = tk.StringVar(value="Option 1")
        self.listbox_var = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create notebook (tabbed interface)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_basic_tab(notebook)
        self.create_form_tab(notebook)
        self.create_list_tab(notebook)
        self.create_canvas_tab(notebook)
        
        # Status bar
        self.status_bar = tk.Label(
            self.root, 
            text="Ready", 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_basic_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Basic Widgets")
        
        # Label
        label = tk.Label(tab, text="Welcome to Tkinter Demo!", font=("Arial", 14))
        label.pack(pady=10)
        
        # Button with counter
        self.counter_label = tk.Label(tab, text="Counter: 0")
        self.counter_label.pack()
        
        btn_frame = tk.Frame(tab)
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Increase", command=self.increase_counter).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Decrease", command=self.decrease_counter).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_counter).pack(side=tk.LEFT, padx=5)
        
        # Entry and validation
        entry_frame = tk.LabelFrame(tab, text="Text Input", padx=10, pady=10)
        entry_frame.pack(pady=10, padx=10, fill='x')
        
        tk.Label(entry_frame, text="Enter text:").pack(side=tk.LEFT)
        entry = tk.Entry(entry_frame, textvariable=self.text_var)
        entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        tk.Button(entry_frame, text="Show", command=self.show_text).pack(side=tk.LEFT)
        
        # Checkbutton
        check = tk.Checkbutton(
            tab, 
            text="Enable feature", 
            variable=self.check_var,
            command=self.check_changed
        )
        check.pack(pady=5)
        
        # Radiobuttons
        radio_frame = tk.LabelFrame(tab, text="Choose Option", padx=10, pady=10)
        radio_frame.pack(pady=10)
        
        for i in range(1, 4):
            tk.Radiobutton(
                radio_frame,
                text=f"Option {i}",
                variable=self.radio_var,
                value=f"Option {i}",
                command=self.radio_changed
            ).pack(anchor=tk.W)
    
    def create_form_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Form")
        
        # Create form
        form_frame = tk.LabelFrame(tab, text="User Information", padx=20, pady=20)
        form_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Form fields
        fields = ["Name", "Email", "Phone", "Age"]
        self.entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(form_frame, text=f"{field}:").grid(row=i, column=0, sticky='e', pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry
        
        # Gender (combobox)
        tk.Label(form_frame, text="Gender:").grid(row=4, column=0, sticky='e', pady=5)
        self.gender_combo = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], state="readonly")
        self.gender_combo.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.gender_combo.set("Male")
        
        # Submit button
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="Submit", command=self.submit_form, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_form).pack(side=tk.LEFT, padx=5)
    
    def create_list_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Lists")
        
        # Listbox with scrollbar
        list_frame = tk.LabelFrame(tab, text="Listbox", padx=10, pady=10)
        list_frame.pack(side=tk.LEFT, padx=10, pady=10, fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=10)
        self.listbox.pack(side=tk.LEFT, fill='both', expand=True)
        
        scrollbar.config(command=self.listbox.yview)
        
        # Add items to listbox
        for i in range(1, 21):
            self.listbox.insert(tk.END, f"Item {i}")
        
        # Combobox
        combo_frame = tk.LabelFrame(tab, text="Combobox", padx=10, pady=10)
        combo_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill='both', expand=True)
        
        tk.Label(combo_frame, text="Select an option:").pack()
        self.combobox = ttk.Combobox(
            combo_frame, 
            values=["Option A", "Option B", "Option C", "Option D"],
            textvariable=self.listbox_var
        )
        self.combobox.pack(pady=5)
        
        tk.Button(combo_frame, text="Show Selection", command=self.show_selection).pack(pady=5)
        
        # Display selected value
        self.selection_label = tk.Label(combo_frame, text="Selected: None")
        self.selection_label.pack(pady=5)
    
    def create_canvas_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Canvas")
        
        # Canvas for drawing
        self.canvas = tk.Canvas(tab, bg='white', width=400, height=200)
        self.canvas.pack(pady=10)
        
        # Draw shapes
        self.canvas.create_rectangle(50, 50, 150, 150, fill='blue', outline='black', width=2)
        self.canvas.create_oval(200, 50, 300, 150, fill='red', outline='black', width=2)
        self.canvas.create_line(350, 50, 400, 150, fill='green', width=3)
        
        # Animation button
        self.oval = self.canvas.create_oval(50, 200, 100, 250, fill='yellow')
        
        btn_frame = tk.Frame(tab)
        btn_frame.pack()
        
        tk.Button(btn_frame, text="Move Left", command=self.move_left).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Move Right", command=self.move_right).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Random Color", command=self.random_color).pack(side=tk.LEFT, padx=5)
    
    def increase_counter(self):
        self.counter += 1
        self.counter_label.config(text=f"Counter: {self.counter}")
        self.update_status(f"Counter increased to {self.counter}")
    
    def decrease_counter(self):
        self.counter -= 1
        self.counter_label.config(text=f"Counter: {self.counter}")
        self.update_status(f"Counter decreased to {self.counter}")
    
    def reset_counter(self):
        self.counter = 0
        self.counter_label.config(text=f"Counter: {self.counter}")
        self.update_status("Counter reset")
    
    def show_text(self):
        text = self.text_var.get()
        if text:
            messagebox.showinfo("Text Input", f"You entered: {text}")
            self.update_status(f"Text shown: {text}")
        else:
            messagebox.showwarning("Warning", "No text entered!")
    
    def check_changed(self):
        state = "enabled" if self.check_var.get() else "disabled"
        self.update_status(f"Feature {state}")
    
    def radio_changed(self):
        self.update_status(f"Selected: {self.radio_var.get()}")
    
    def submit_form(self):
        data = {}
        for field, entry in self.entries.items():
            data[field] = entry.get()
        data["Gender"] = self.gender_combo.get()
        
        messagebox.showinfo("Form Data", f"Submitted: {data}")
        self.update_status("Form submitted")
    
    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.gender_combo.set("Male")
        self.update_status("Form cleared")
    
    def show_selection(self):
        selection = self.listbox_var.get()
        self.selection_label.config(text=f"Selected: {selection}")
        self.update_status(f"Selected: {selection}")
    
    def move_left(self):
        self.canvas.move(self.oval, -10, 0)
    
    def move_right(self):
        self.canvas.move(self.oval, 10, 0)
    
    def move_up(self):
        self.canvas.move(self.oval, 0, -10)
    
    def move_down(self):
        self.canvas.move(self.oval, 0, 10)
    
    def random_color(self):
        colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
        self.canvas.itemconfig(self.oval, fill=random.choice(colors))
    
    def update_status(self, message):
        self.status_bar.config(text=f"Status: {message}")
    
    def run(self):
        self.root.mainloop()


# Run the application
if __name__ == "__main__":
    app = TkinterDemo()
    app.run()
