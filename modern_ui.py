import customtkinter as ctk
from tkinter import filedialog, messagebox
from backend import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SplashScreen:
    def __init__(self):
        self.splash = ctk.CTk()
        self.splash.geometry("700x400")
        self.splash.title("PDF Xpert Loading")
        self.splash.configure(fg_color="#0f172a")
        self.splash.overrideredirect(True)

        width = 700
        height = 400
        screen_w = self.splash.winfo_screenwidth()
        screen_h = self.splash.winfo_screenheight()
        x = int((screen_w / 2) - (width / 2))
        y = int((screen_h / 2) - (height / 2))
        self.splash.geometry(f"{width}x{height}+{x}+{y}")

        title = ctk.CTkLabel(
            self.splash,
            text="PDF XPERT",
            font=("Arial", 42, "bold"),
            text_color="#ef4444"
        )
        title.pack(pady=100)

        subtitle = ctk.CTkLabel(
            self.splash,
            text="Professional PDF Toolkit",
            font=("Arial", 18),
            text_color="white"
        )
        subtitle.pack()

        self.progress = ctk.CTkProgressBar(
            self.splash,
            width=500,
            progress_color="#7f0000"
        )
        self.progress.pack(pady=50)
        self.progress.set(0)

        self.load()
        self.splash.mainloop()

    def load(self):
        for i in range(101):
            self.progress.set(i / 100)
            self.splash.update()
            self.splash.after(15)

        self.splash.destroy()
        PDFXpertApp()


class PDFXpertApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("PDF Xpert")
        self.root.state("zoomed")
        self.root.configure(fg_color="#050505")

        self.create_ui()
        self.root.mainloop()

    def create_ui(self):
        self.sidebar = ctk.CTkScrollableFrame(
            self.root,
            width=260,
            fg_color="#050505",
            corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        logo = ctk.CTkLabel(
            self.sidebar,
            text="PDF XPERT",
            font=("Arial", 28, "bold"),
            text_color="#ef4444"
        )
        logo.pack(pady=20)

        buttons = [
    ("🏠 Home", self.show_home),
    ("📄 Merge PDF", self.merge_pdf_ui),
    ("✂️ Split PDF", self.split_pdf_ui),
    ("🔄 Rotate PDF", self.rotate_pdf_ui),
    ("🔒 Protect PDF", self.protect_pdf_ui),
    ("🔓 Unlock PDF", self.unlock_pdf_ui),
    ("🔁 Reverse PDF", self.reverse_pdf_ui),
    ("🗑 Delete Pages", self.delete_pages_ui),
    ("🖼 PDF to Image", self.pdf_to_image_ui),
    ("📘 PDF to Word", self.pdf_to_word_ui),
    ("📕 Word to PDF", self.word_to_pdf_ui),
    ("ℹ About", self.about_app),
]

        for text, cmd in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=cmd,
                height=42,
                corner_radius=12,
                fg_color="#111111",
                hover_color="#7f0000",
                anchor="w",
                font=("Arial", 14, "bold")
            )
            btn.pack(pady=5, padx=12, fill="x")

        footer = ctk.CTkLabel(
            self.sidebar,
            text="Fast • Secure • Easy",
            font=("Arial", 12),
            text_color="gray"
        )
        footer.pack(pady=8)

        self.main = ctk.CTkFrame(self.root, fg_color="#050505")
        self.main.pack(side="right", fill="both", expand=True)

        self.show_home()

    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_main()

        heading_frame = ctk.CTkFrame(self.main, fg_color="transparent")
        heading_frame.pack(pady=15)

        welcome = ctk.CTkLabel(
            heading_frame,
            text="Welcome to ",
            font=("Arial", 30, "bold"),
            text_color="white"
        )
        welcome.pack(side="left")

        brand = ctk.CTkLabel(
            heading_frame,
            text="PDF Xpert",
            font=("Arial", 30, "bold"),
            text_color="#ef4444"
        )
        brand.pack(side="left")

        subtitle = ctk.CTkLabel(
            self.main,
            text="All your PDF tools in one premium dashboard",
            font=("Arial", 16),
            text_color="lightgray"
        )
        subtitle.pack(pady=5)

        grid = ctk.CTkScrollableFrame(
            self.main,
            fg_color="transparent",
            width=1100,
            height=650
        )
        grid.pack(pady=10, fill="both", expand=True)

        tools = [
            ("Merge PDF", self.merge_pdf_ui),
            ("Split PDF", self.split_pdf_ui),
            ("Rotate PDF", self.rotate_pdf_ui),
            ("Protect PDF", self.protect_pdf_ui),
            ("Unlock PDF", self.unlock_pdf_ui),
            ("Reverse PDF", self.reverse_pdf_ui),
            ("Delete Pages", self.delete_pages_ui),
            ("PDF to Image", self.pdf_to_image_ui),
            ("PDF to Word", self.pdf_to_word_ui),
            ("Word to PDF", self.word_to_pdf_ui),
        ]

        colors = [
    "#0f0000",
    "#160000",
    "#220000",
    "#0f0000",
    "#160000",
    "#220000",
    "#0f0000",
    "#160000",
    "#220000",
    "#0f0000"
]

        for i, (name, cmd) in enumerate(tools):
            card = ctk.CTkButton(
                grid,
                text=name,
                command=cmd,
                width=200,
                height=100,
                corner_radius=20,
                fg_color=colors[i],
                hover_color="#3a0000",
                font=("Arial", 16, "bold")
            )
            card.grid(row=i // 3, column=i % 3, padx=15, pady=15)

    def merge_pdf_ui(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if files:
            output = filedialog.asksaveasfilename(defaultextension=".pdf")
            if output:
                messagebox.showinfo("Result", merge_pdfs(files, output))

    def split_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            messagebox.showinfo("Result", split_pdf(file))

    def rotate_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            angle = ctk.CTkInputDialog(
                text="Enter angle (90,180,270):",
                title="Rotate PDF"
            ).get_input()

            if angle:
                messagebox.showinfo("Result", rotate_pdf(file, int(angle)))

    def protect_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            password = ctk.CTkInputDialog(
                text="Enter password:",
                title="Protect PDF"
            ).get_input()

            if password:
                messagebox.showinfo("Result", protect_pdf(file, password))

    def unlock_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            password = ctk.CTkInputDialog(
                text="Enter password:",
                title="Unlock PDF"
            ).get_input()

            if password:
                messagebox.showinfo("Result", unlock_pdf(file, password))

    def reverse_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            messagebox.showinfo("Result", reverse_pdf(file))

    def delete_pages_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if file:
            pages = ctk.CTkInputDialog(
                text="Enter pages like 1,3:",
                title="Delete Pages"
            ).get_input()

            if pages:
                confirm = messagebox.askyesno(
                    "Confirm Delete",
                    f"Are you sure you want to delete page(s): {pages}?"
                )

                if confirm:
                    messagebox.showinfo("Result", delete_pages(file, pages))

    

    def about_app(self):
        messagebox.showinfo(
            "About PDF Xpert",
            "PDF Xpert v1.0\n\n"
            "Professional PDF Toolkit\n\n"
            "Features:\n"
            "• Merge PDFs\n"
            "• Split PDFs\n"
            "• Rotate PDFs\n"
            "• Protect PDFs\n"
            "• Unlock PDFs\n"
            "• Reverse PDFs\n"
            "• Delete Pages\n"
            "• PDF to Image\n"
            "• PDF to Word\n"
            "• Word to PDF\n\n"
            "Created by Shiva 🚀"
        )

    def pdf_to_image_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            messagebox.showinfo("Result", pdf_to_image(file))

    def pdf_to_word_ui(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            messagebox.showinfo("Result", pdf_to_word(file))

    def word_to_pdf_ui(self):
        file = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
        if file:
            messagebox.showinfo("Result", word_to_pdf(file))


SplashScreen()