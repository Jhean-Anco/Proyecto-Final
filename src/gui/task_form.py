import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.gui.styles import *

class TaskForm(tk.Toplevel):
    def __init__(self, master, on_submit, task=None):
        super().__init__(master)
        self.title("Formulario de Tarea")
        self.geometry("400x400")
        self.configure(bg=BACKGROUND_COLOR)
        self.on_submit = on_submit
        self.task = task

        self._build_form()

    def _build_form(self):
        self.entries = {}

        # Título
        tk.Label(self, text="Título:", bg=BACKGROUND_COLOR, font=FONT_MAIN).pack(pady=(10, 0))
        self.entries["title"] = tk.Entry(self, font=FONT_MAIN)
        self.entries["title"].pack()

        # Descripción
        tk.Label(self, text="Descripción:", bg=BACKGROUND_COLOR, font=FONT_MAIN).pack(pady=(10, 0))
        self.entries["description"] = tk.Entry(self, font=FONT_MAIN)
        self.entries["description"].pack()

        # Fecha límite con calendario
        tk.Label(self, text="Fecha límite:", bg=BACKGROUND_COLOR, font=FONT_MAIN).pack(pady=(10, 0))
        self.entries["deadline"] = DateEntry(self, date_pattern="yyyy-mm-dd", font=FONT_MAIN)
        self.entries["deadline"].pack()

        # Categoría (menú desplegable)
        tk.Label(self, text="Categoría:", bg=BACKGROUND_COLOR, font=FONT_MAIN).pack(pady=(10, 0))
        self.entries["category"] = ttk.Combobox(self, values=["Trabajo", "Estudio", "Personal"], font=FONT_MAIN)
        self.entries["category"].pack()

        # Etiquetas con selección múltiple
        tk.Label(self, text="Etiquetas:", bg=BACKGROUND_COLOR, font=FONT_MAIN).pack(pady=(10, 0))
        self.entries["tags"] = tk.Listbox(self, selectmode=tk.MULTIPLE, height=5, font=FONT_MAIN)
        for tag in ["Urgente", "Importante", "Casa", "Examen", "Proyecto"]:
            self.entries["tags"].insert(tk.END, tag)
        self.entries["tags"].pack()

        # Botón de acción
        button_text = "Actualizar" if self.task else "Crear"
        tk.Button(self, text=f"{button_text} Tarea", font=FONT_MAIN,
                  bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                  command=self._submit).pack(pady=20)

        # Si es edición, rellenar campos
        if self.task:
            self.entries["title"].insert(0, self.task.title)
            self.entries["description"].insert(0, self.task.description)
            if self.task.deadline:
                self.entries["deadline"].set_date(self.task.deadline)
            if self.task.category:
                self.entries["category"].set(self.task.category)
            if self.task.tags:
                tags = self.task.tags.split(",")
                for i, tag in enumerate(["Urgente", "Importante", "Casa", "Examen", "Proyecto"]):
                    if tag.strip() in tags:
                        self.entries["tags"].selection_set(i)

    def _submit(self):
        title = self.entries["title"].get().strip()
        description = self.entries["description"].get().strip()
        deadline = self.entries["deadline"].get()
        category = self.entries["category"].get()
        selected_indices = self.entries["tags"].curselection()
        tags = ",".join([self.entries["tags"].get(i) for i in selected_indices])

        if not title:
            messagebox.showwarning("Falta título", "La tarea debe tener un título.")
            return

        self.on_submit(title, description, deadline, category, tags)
        self.destroy()
