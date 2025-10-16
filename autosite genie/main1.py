import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Create output folder if not exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Themes dictionary
themes = {
    "gamer": {
        "bg_color": "#0f0f0f",
        "text_color": "#39ff14",
        "font": "'Press Start 2P', cursive",
        "image": "https://images.unsplash.com/photo-1610391428420-f74d3fe2ff61?auto=format&fit=crop&w=800&q=80",
        "extra_js": "console.log('Level Up Gamer!');"
    },
    "programmer": {
        "bg_color": "#1e1e2f",
        "text_color": "#00ffd5",
        "font": "'Fira Code', monospace",
        "image": "https://images.unsplash.com/photo-1581091012184-3eec24db2766?auto=format&fit=crop&w=800&q=80",
        "extra_js": "console.log('Hello, World!');"
    },
    "photographer": {
        "bg_color": "#ffffff",
        "text_color": "#333333",
        "font": "'Playfair Display', serif",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "extra_js": "console.log('Capturing Moments...');"
    }
}

# Default theme
default_theme = {
    "bg_color": "#ffffff",
    "text_color": "#000000",
    "font": "sans-serif",
    "image": "https://via.placeholder.com/800x400?text=Welcome+to+AutoSite+Genie",
    "extra_js": "console.log('Welcome to AutoSite Genie');"
}

# Website generation logic
def generate_website(user_type):
    user_type = user_type.strip().lower()
    theme = themes.get(user_type, default_theme)
    title = f"Portfolio for {user_type.capitalize()} - AutoSite Genie"

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Playfair+Display&family=Press+Start+2P&display=swap" rel="stylesheet">
        <style>
            body {{
                background-color: {theme['bg_color']};
                color: {theme['text_color']};
                font-family: {theme['font']};
                padding: 2rem;
                text-align: center;
            }}
            img {{
                width: 80%;
                max-width: 700px;
                margin-top: 20px;
                border-radius: 20px;
            }}
            h1 {{
                font-size: 2.5rem;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <p>This is a personalized portfolio site made just for a {user_type}!</p>
        <img src="{theme['image']}" alt="Theme image for {user_type}">
        <p>Generated with ❤️ by AutoSite Genie</p>
        <script>
            {theme['extra_js']}
        </script>
    </body>
    </html>
    """

    filename = f"site_{datetime.now().strftime('%Y%m%d%H%M%S')}.html"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_template)

    messagebox.showinfo("Success!", f"✅ Website created for '{user_type}'!\n📄 File saved to: {filepath}")

# GUI setup
def start_gui():
    root = tk.Tk()
    root.title("AutoSite Genie")

    root.geometry("400x200")
    root.resizable(False, False)
    root.configure(bg="#eeeeee")

    tk.Label(root, text="Enter user type (e.g., gamer, photographer, etc):", bg="#eeeeee", font=("Arial", 10)).pack(pady=10)

    user_entry = tk.Entry(root, font=("Arial", 12), width=30)
    user_entry.pack()

    def on_generate():
        user_type = user_entry.get()
        if not user_type:
            messagebox.showerror("Error", "Please enter a user type.")
        else:
            generate_website(user_type)

    tk.Button(root, text="Generate Website", command=on_generate, font=("Arial", 12), bg="#007acc", fg="white", padx=10, pady=5).pack(pady=20)

    root.mainloop()

# Run GUI
if __name__ == "__main__":
    start_gui()
