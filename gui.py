import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "core"))
from checker import load_bloom, analyze

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")
        self.show_password = False
        print("Loading bloom filter...")
        self.bloom = load_bloom()
        print("Ready!")
        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(
            self.root,
            text="🔐 Password Strength Analyzer",
            font=("Helvetica", 16, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(pady=30)

        # Password Frame
        pass_frame = tk.Frame(self.root, bg="#1e1e2e")
        pass_frame.pack(pady=10)

        # Password Label
        tk.Label(
            pass_frame,
            text="Enter Password:",
            font=("Helvetica", 11),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).grid(row=0, column=0, columnspan=2, pady=5)

        # Password Entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            pass_frame,
            textvariable=self.password_var,
            show="•",
            font=("Helvetica", 12),
            width=25,
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            bd=5
        )
        self.password_entry.grid(row=1, column=0, padx=5)

        # Show/Hide Button
        self.toggle_btn = tk.Button(
            pass_frame,
            text="👁️",
            command=self.toggle_password,
            bg="#313244",
            fg="#cdd6f4",
            relief="flat",
            font=("Helvetica", 12),
            cursor="hand2"
        )
        self.toggle_btn.grid(row=1, column=1, padx=5)

        # Check Button
        tk.Button(
            self.root,
            text="CHECK PASSWORD",
            command=self.check_password,
            bg="#89b4fa",
            fg="#1e1e2e",
            font=("Helvetica", 12, "bold"),
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)

        # Results Frame
        self.result_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.result_frame.pack(pady=10, fill="x", padx=40)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="•")
            self.toggle_btn.config(text="👁️")
            self.show_password = False
        else:
            self.password_entry.config(show="")
            self.toggle_btn.config(text="🙈")
            self.show_password = True

    def check_password(self):
        password = self.password_var.get()

        if len(password) == 0:
            return

        results = analyze(password, self.bloom)

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if results['rating'] == "WEAK":
            color = "#f38ba8"
            emoji = "❌"
        elif results['rating'] == "FAIR":
            color = "#fab387"
            emoji = "⚠️"
        elif results['rating'] == "STRONG":
            color = "#a6e3a1"
            emoji = "💪"
        else:
            color = "#89b4fa"
            emoji = "🔥"

        tk.Label(
            self.result_frame,
            text=f"{emoji} {results['rating']}",
            font=("Helvetica", 20, "bold"),
            bg="#1e1e2e",
            fg=color
        ).pack(pady=10)

        details = [
            ("Length", f"{results['length']} characters"),
            ("Variety", f"{results['variety_score']}/4"),
            ("Entropy", f"{results['entropy']} bits"),
            ("Common Password", "YES ⚠️" if results['is_common'] else "NO ✅"),
        ]

        for label, value in details:
            row = tk.Frame(self.result_frame, bg="#313244")
            row.pack(fill="x", pady=3)

            tk.Label(
                row,
                text=label,
                font=("Helvetica", 10),
                bg="#313244",
                fg="#cdd6f4",
                width=20,
                anchor="w"
            ).pack(side="left", padx=10, pady=5)

            tk.Label(
                row,
                text=value,
                font=("Helvetica", 10, "bold"),
                bg="#313244",
                fg=color,
                anchor="e"
            ).pack(side="right", padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()