import tkinter as tk
from tkinter import ttk, messagebox
from analyzer import analyze_password
from wordlist_generator import generate_wordlist
from utils import export_wordlist

def run_gui():
    def analyze():
        pwd = password_entry.get()
        if not pwd:
            messagebox.showwarning("Missing Input", "Please enter a password.")
            return
        result = analyze_password(pwd)
        output_text.configure(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"🔒 Score: {result['score']}/4\n")
        output_text.insert(tk.END, f"📌 Feedback: {result['feedback']}\n")
        output_text.insert(tk.END, f"⏱️ Crack Time: {result['crack_times_display']}\n")
        output_text.configure(state='disabled')

    def generate():
        info = info_entry.get()
        if not info:
            messagebox.showwarning("Missing Input", "Please enter personal information.")
            return
        inputs = info.split()
        words = generate_wordlist(inputs)
        export_wordlist(words)
        output_text.configure(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"✅ Generated {len(words)} passwords.\n")
        output_text.insert(tk.END, "📂 Saved to: output/wordlist.txt")
        output_text.configure(state='disabled')

    # Main Window
    root = tk.Tk()
    root.title("🔐 Password Strength & Wordlist Tool")
    root.geometry("500x400")
    root.resizable(False, False)

    # Use ttk theme
    style = ttk.Style()
    style.theme_use('clam')

    # Layout Frame
    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Inputs
    ttk.Label(main_frame, text="🔑 Password:").grid(row=0, column=0, sticky="e", pady=5)
    password_entry = ttk.Entry(main_frame, width=40, show="*")
    password_entry.grid(row=0, column=1, pady=5)

    ttk.Label(main_frame, text="👤 Personal Info (name, pet, etc):").grid(row=1, column=0, sticky="e", pady=5)
    info_entry = ttk.Entry(main_frame, width=40)
    info_entry.grid(row=1, column=1, pady=5)

    # Buttons
    ttk.Button(main_frame, text="🔍 Analyze Password", command=analyze).grid(row=2, column=0, padx=5, pady=10)
    ttk.Button(main_frame, text="🛠️ Generate Wordlist", command=generate).grid(row=2, column=1, padx=5, pady=10)

    # Output Box
    output_text = tk.Text(main_frame, height=10, width=60, wrap="word", state='disabled')
    output_text.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
if __name__ == "__main__":
    run_gui()
