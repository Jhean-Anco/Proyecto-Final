import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.controllers.auth_controller import AuthController
from src.db.database import Database
from src.gui.main_window import MainWindow
from src.gui.register_window import RegisterWindow
from src.gui.styles import *

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión - Gestor de Tareas")
        self.root.geometry("400x500")
        self.root.configure(bg=BACKGROUND_COLOR)

        self.db = Database()
        self.auth = AuthController(self.db)

        self._build_interface()

    def _build_interface(self):
        # Imagen decorativa
        img = Image.open("assets/images/icons/user_icon.jpg").resize((80, 80))
        self.user_icon = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.user_icon, bg=BACKGROUND_COLOR).pack(pady=20)

        # Título
        tk.Label(self.root, text="Iniciar Sesión", font=FONT_TITLE,
                 bg=BACKGROUND_COLOR, fg=PRIMARY_COLOR).pack(pady=(0, 10))

        # DNI
        tk.Label(self.root, text="DNI:", font=FONT_MAIN, bg=BACKGROUND_COLOR).pack()
        self.dni_entry = tk.Entry(self.root, font=FONT_MAIN)
        self.dni_entry.pack(pady=5)

        # Contraseña
        tk.Label(self.root, text="Contraseña:", font=FONT_MAIN, bg=BACKGROUND_COLOR).pack()
        self.password_entry = tk.Entry(self.root, show="*", font=FONT_MAIN)
        self.password_entry.pack(pady=5)

        # Botón Iniciar Sesión
        tk.Button(self.root, text="Iniciar Sesión", font=FONT_MAIN,
                  bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                  command=self._login).pack(pady=20)

        # Botón Registrarse
        tk.Button(self.root, text="Registrarse", font=FONT_MAIN,
                  bg=SECONDARY_COLOR, fg=BUTTON_TEXT_COLOR,
                  command=self._open_register_window).pack()

    def _login(self):
        dni = self.dni_entry.get().strip()
        password = self.password_entry.get().strip()

        if not dni or not password:
            messagebox.showwarning("Campos vacíos", "Por favor, ingresa tu DNI y contraseña.")
            return

        user = self.auth.login_user(dni, password)
        if user:
            messagebox.showinfo("Éxito", f"Bienvenido {user.username}")
            self.root.destroy()
            import tkinter as tk
            root = tk.Tk()
            app = MainWindow(root, user_dni=user.dni)
            root.mainloop()
        else:
            messagebox.showerror("Error", "DNI o contraseña incorrectos.")

    def _open_register_window(self):
        RegisterWindow(self.root)
