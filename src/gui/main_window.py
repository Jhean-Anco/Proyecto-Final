import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.gui.styles import *
from src.db.database import Database
from src.controllers.task_controller import TaskController
from src.gui.task_form import TaskForm
from datetime import date

class MainWindow:
    def __init__(self, root, user_dni):
        self.root = root
        self.root.title("Gestor de Tareas - UCCI")
        self.root.geometry("800x600")
        self.root.configure(bg=BACKGROUND_COLOR)

        self.user_dni = user_dni
        self.db = Database()
        self.controller = TaskController(self.db)

        self._load_images()
        self._build_interface()
        self._populate_tasks()

    def _load_images(self):
        logo_img = Image.open("assets/images/logo_ucci.jpg").resize((150, 75))
        self.logo = ImageTk.PhotoImage(logo_img)
        bg_img = Image.open("assets/images/campus.jpg").resize((800, 600))
        self.background = ImageTk.PhotoImage(bg_img)

    def _build_interface(self):
        bg_label = tk.Label(self.root, image=self.background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        logo_label = tk.Label(self.root, image=self.logo, bg=BACKGROUND_COLOR)
        logo_label.pack(pady=10)

        title_label = tk.Label(self.root, text="Gestor de Tareas", font=FONT_TITLE,
                               bg=BACKGROUND_COLOR, fg=PRIMARY_COLOR)
        title_label.pack()

        self.add_button = tk.Button(self.root, text="Agregar Tarea", font=FONT_MAIN,
                                    bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                    command=self._show_add_task_form)
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, font=FONT_MAIN, width=90, height=15)
        self.task_listbox.pack(pady=20)

        btn_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        btn_frame.pack()

        self.complete_button = tk.Button(btn_frame, text="Marcar como Completada",
                                         font=FONT_MAIN, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                         command=self._mark_completed)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(btn_frame, text="Editar",
                                     font=FONT_MAIN, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                     command=self._show_edit_task_form)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar",
                                       font=FONT_MAIN, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                       command=self._delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

    
    def _populate_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = self.controller.get_all_tasks(user_dni=self.user_dni)

        for task in self.tasks:
            status = "✅" if task.completed else "❌"
            vencido = ""
            if task.deadline:
                try:
                    task_date = date.fromisoformat(task.deadline)
                    if not task.completed and task_date < date.today():
                        vencido = "⚠️ Vencida"
                except:
                    pass

            display = f"{status} {task.title}"
            if vencido:
                display += f" [{vencido}]"
            elif task.category:
                display += f" - {task.category}"

            if task.deadline:
                display += f" ({task.deadline})"

            self.task_listbox.insert(tk.END, display)

    def _get_selected_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            return self.tasks[selected[0]]
        return None

    def _mark_completed(self):
        task = self._get_selected_task()
        if task:
            task.completed = True
            self.controller.update_task(task)
            self._populate_tasks()

    def _delete_task(self):
        task = self._get_selected_task()
        if task:
            confirm = messagebox.askyesno("Eliminar", f"¿Eliminar tarea: {task.title}?")
            if confirm:
                self.controller.delete_task(task.id)
                self._populate_tasks()

    def _show_add_task_form(self):
        TaskForm(self.root, on_submit=lambda title, desc, deadline, category, tags:
                 self._add_task(title, desc, deadline, category, tags))

    def _add_task(self, title, description, deadline, category, tags):
        self.controller.add_task(title, description, user_dni=self.user_dni,
                                 deadline=deadline, category=category, tags=tags)
        self._populate_tasks()

    def _show_edit_task_form(self):
        task = self._get_selected_task()
        if task:
            TaskForm(self.root,
                     on_submit=lambda title, desc, deadline, category, tags:
                     self._edit_task(task, title, desc, deadline, category, tags),
                     task=task)

    def _edit_task(self, task, title, description, deadline, category, tags):
        task.title = title
        task.description = description
        task.deadline = deadline
        task.category = category
        task.tags = tags
        self.controller.update_task(task)
        self._populate_tasks()
