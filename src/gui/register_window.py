import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.controllers.auth_controller import AuthController
from src.db.database import Database
from src.gui.styles import *

class RegisterWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registro de Usuario")
        self.geometry("420x620")
        self.configure(bg=BACKGROUND_COLOR)

        self.db = Database()
        self.auth = AuthController(self.db)

        self._build_interface()

    def _build_interface(self):
        self.entries = {}

        # Imagen decorativa
        img = Image.open("assets/images/icons/user_icon.jpg").resize((80, 80))
        self.user_icon = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.user_icon, bg=BACKGROUND_COLOR).pack(pady=10)

        # Título visual
        tk.Label(self, text="Crear Cuenta", font=FONT_TITLE, bg=BACKGROUND_COLOR, fg=PRIMARY_COLOR).pack(pady=10)

        campos = [
            ("DNI:", "dni", False),
            ("Usuario:", "username", False),
            ("Contraseña:", "password", True),
            ("Correo electrónico:", "email", False),
            ("Celular:", "phone", False),
            ("Edad:", "age", False)
        ]

        for label_text, key, is_password in campos:
            tk.Label(self, text=label_text, font=FONT_MAIN, bg=BACKGROUND_COLOR).pack(pady=(8, 0))
            entry = tk.Entry(self, font=FONT_MAIN, show="*" if is_password else "")
            entry.pack()
            self.entries[key] = entry

        # Botón registrar
        tk.Button(self, text="Registrar", font=FONT_MAIN,
                  bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                  command=self._submit_register).pack(pady=20)

    def _submit_register(self):
        dni = self.entries["dni"].get().strip()
        username = self.entries["username"].get().strip()
        password = self.entries["password"].get().strip()
        email = self.entries["email"].get().strip()
        phone = self.entries["phone"].get().strip()
        age = self.entries["age"].get().strip()

        # Validaciones
        if not dni.isdigit() or len(dni) != 8:
            messagebox.showwarning("DNI inválido", "El DNI debe tener 8 dígitos.")
            return
        if not username or not password:
            messagebox.showwarning("Campos requeridos", "Usuario y contraseña son obligatorios.")
            return
        if not phone.isdigit() or len(phone) != 9:
            messagebox.showwarning("Celular inválido", "El número debe tener 9 dígitos.")
            return
        if not age.isdigit() or not (1 <= int(age) <= 120):
            messagebox.showwarning("Edad inválida", "Edad debe ser un número entre 1 y 120.")
            return
        if "@" not in email or "." not in email:
            messagebox.showwarning("Correo inválido", "Correo electrónico no válido.")
            return

        success = self.auth.register_user(dni, username, password, email, phone, int(age))
        if success:
            messagebox.showinfo("Registrado", "Usuario registrado con éxito.")
            self.destroy()
        else:
            messagebox.showerror("Error", "El DNI ya está registrado.")
