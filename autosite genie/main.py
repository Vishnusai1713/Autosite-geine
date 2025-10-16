import os
import webbrowser
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def load_template(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def save_html(content, folder='output'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"site_{timestamp}.html"
    full_path = os.path.join(folder, filename)
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return full_path

def generate_site():
    topic = entry.get().strip()
    if not topic:
        messagebox.showwarning("Input Error", "Please enter a topic!")
        return

    title = f"{topic.title()} - AutoSite Genie"
    description = f"This is a simple website about {topic}."
    section1 = f"<h2>Introduction to {topic}</h2><p>{topic.title()} is an interesting topic that covers many aspects.</p>"
    section2 = f"<h2>Why {topic} Matters</h2><p>Learning about {topic} can benefit students, professionals, and enthusiasts alike.</p>"
    sections = section1 + section2

    template_path = os.path.join('templates', 'template.html')
    template = load_template(template_path)

    html_content = template.replace("{{title}}", title)\
                           .replace("{{description}}", description)\
                           .replace("{{sections}}", sections)

    output_file = save_html(html_content)

    status_label.config(text=f"Website saved: {output_file}")
    webbrowser.open(f"file://{os.path.abspath(output_file)}")

# Set up GUI window
root = tk.Tk()
root.title("AutoSite Genie - Website Generator")

# Window size
root.geometry("400x180")

# Label and Entry for topic input
tk.Label(root, text="Enter topic for your website:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack()

# Generate button
generate_btn = tk.Button(root, text="Generate Website", command=generate_site, font=("Arial", 12), bg="#007acc", fg="white")
generate_btn.pack(pady=15)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
status_label.pack()

root.mainloop()
