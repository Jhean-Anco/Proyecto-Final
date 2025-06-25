# ✅ Gestor de Tareas Universitarias - UCCI

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación de escritorio con interfaz gráfica, que permita a los estudiantes gestionar tareas académicas de forma ordenada, moderna y eficiente. El sistema está enfocado en la experiencia del estudiante universitario, usando buenas prácticas de programación, diseño modular, control de versiones y documentación técnica.

---

## 🧠 Funcionalidades Implementadas

- 🔐 Registro e inicio de sesión usando **DNI** (identificador único)
- 🧑‍🎓 Formulario completo de creación de usuario: nombre, contraseña, correo, celular y edad
- 📋 CRUD de tareas personales:
  - Crear / Editar / Eliminar / Marcar como completadas
  - Asociadas al DNI del estudiante
- 📅 Selección de fecha límite mediante calendario (`tkcalendar`)
- 🏷 Múltiples etiquetas por tarea (selección múltiple)
- 📂 Categorías predefinidas (Trabajo, Estudio, Personal)
- ⚠️ Detección visual de tareas vencidas
- 🖼 Diseño visual con logotipo institucional, fondo de campus y estilo amigable

---

## 🛠 Tecnologías Utilizadas

- Python 3.11+
- Tkinter (GUI)
- SQLite3 (Base de datos local)
- Pillow (carga y manejo de imágenes)
- tkcalendar (selector de fechas)
- Git + GitHub (control de versiones)

---

## 🚀 Instrucciones de Ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Jhean-Anco/Proyecto-Final.git
   cd Proyecto-Final
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el sistema:
   ```bash
   python -m src.main
   ```

> La base de datos `tasks.db` se crea automáticamente al ejecutar el sistema.

---

## 🗂 Estructura del Proyecto

```
ToDoList_Proyecto_Final/
├── assets/                  # Imágenes e íconos de interfaz
│   └── images/
├── docs/                    # Documentación técnica
│   ├── UML/
│   └── planificación/
├── src/
│   ├── controllers/         # Lógica y validaciones
│   ├── db/                  # Conexión SQLite
│   ├── gui/                 # Interfaces gráficas con Tkinter
│   ├── models/              # Clases base: User, Task
│   └── main.py              # Punto de entrada
├── tests/                   # Pruebas unitarias y de integración
├── requirements.txt         # Dependencias externas
├── .gitignore               # Archivos ignorados por Git
└── README.md                # Documentación general del proyecto
```

---

## 👥 Autores

- 👨‍💻 **Jhean Anco**
- 🏫 Universidad Continental
- 🧪 Curso: Construcción de Software – 2025-1

---

## 🗂 Estado del Proyecto

| Versión | Rama                    | Estado     |
|---------|-------------------------|------------|
| 1.0     | `main` / `v1_funcionalidad_basica` | ✅ Completa |
| 2.0     | `v2_repo_documentacion` | 🔄 En desarrollo |
| 3.0     | `v3_documentacion_modelado` | ⏳ Pendiente |
| 4.0     | `v4_testing_tdd`        | ⏳ Pendiente |
| 5.0     | `v5_mejoras_visuales`   | ⏳ Pendiente |

---

## 📌 Licencia

Uso académico. Proyecto de fin de asignatura desarrollado como evidencia de competencia del curso **Construcción de Software**.
