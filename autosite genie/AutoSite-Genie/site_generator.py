import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
from templates_config import PROFESSIONS, DEFAULT_THEME
from html_templates import generate_html

# Create output folder if not exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

def generate_website(profession, name=""):
    """Generate a professional website for the given profession"""
    profession = profession.strip().lower()
    theme = PROFESSIONS.get(profession, DEFAULT_THEME)
    
    # Generate HTML content
    html_content = generate_html(profession, name, theme)
    
    # Create filename with timestamp
    filename = f"site_{profession}_{datetime.now().strftime('%Y%m%d%H%M%S')}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    messagebox.showinfo(
        "Success!",
        f"Website created for {profession.capitalize()}!\n\nFile saved to:\n{filepath}"
    )

def start_gui():
    """Launch the GUI application"""
    root = tk.Tk()
    root.title("AutoSite Genie - Professional Site Generator")
    root.geometry("500x400")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")
    
    # Title
    title_label = tk.Label(
        root,
        text="AutoSite Genie",
        font=("Arial", 20, "bold"),
        bg="#f0f0f0",
        fg="#2c3e50"
    )
    title_label.pack(pady=15)
    
    # Subtitle
    subtitle_label = tk.Label(
        root,
        text="Professional Website Generator",
        font=("Arial", 10),
        bg="#f0f0f0",
        fg="#7f8c8d"
    )
    subtitle_label.pack()
    
    # Profession selection
    profession_label = tk.Label(
        root,
        text="Select Profession:",
        font=("Arial", 11, "bold"),
        bg="#f0f0f0"
    )
    profession_label.pack(pady=(20, 5))
    
    # Dropdown for professions
    professions_list = list(PROFESSIONS.keys())
    profession_var = tk.StringVar(value=professions_list[0])
    
    profession_dropdown = ttk.Combobox(
        root,
        textvariable=profession_var,
        values=professions_list,
        state="readonly",
        width=40,
        font=("Arial", 10)
    )
    profession_dropdown.pack(pady=5)
    
    # Name input
    name_label = tk.Label(
        root,
        text="Your Name (Optional):",
        font=("Arial", 11, "bold"),
        bg="#f0f0f0"
    )
    name_label.pack(pady=(15, 5))
    
    name_entry = tk.Entry(root, font=("Arial", 11), width=40)
    name_entry.pack(pady=5)
    
    # Available professions info
    info_text = tk.Label(
        root,
        text=f"Available: {', '.join(professions_list)}",
        font=("Arial", 8),
        bg="#f0f0f0",
        fg="#95a5a6",
        wraplength=450,
        justify=tk.CENTER
    )
    info_text.pack(pady=10)
    
    def on_generate():
        profession = profession_var.get()
        name = name_entry.get().strip()
        if not profession:
            messagebox.showerror("Error", "Please select a profession.")
        else:
            generate_website(profession, name)
    
    # Generate button
    generate_btn = tk.Button(
        root,
        text="Generate Website",
        command=on_generate,
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        padx=20,
        pady=10,
        relief=tk.RAISED,
        cursor="hand2"
    )
    generate_btn.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    start_gui()
