import tkinter as tk
from tkinter import messagebox

def registrar_libro():
    """Función para registrar el libro y mostrar información en terminal"""
    # Obtener valores de los campos
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    genero = var_genero.get()
    categoria_novela = var_novela.get()
    categoria_ciencia = var_ciencia.get()
    categoria_historia = var_historia.get()
    estado = var_estado.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = var_idioma.get()
    
    # Crear lista de categorías seleccionadas
    categorias = []
    if categoria_novela:
        categorias.append("Novela")
    if categoria_ciencia:
        categorias.append("Ciencia")
    if categoria_historia:
        categorias.append("Historia")
    
    # Mostrar en terminal (consola)
    print("=" * 50)
    print("REGISTRO DE LIBRO - BIBLIOTECA SABERX")
    print("=" * 50)
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año de Publicación: {anio}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias) if categorias else 'Ninguna'}")
    print(f"Estado: {estado}")
    print(f"Número de Copias: {copias}")
    print(f"Idioma: {idioma}")
    print(f"Resumen: {resumen}")
    print("=" * 50)
    
    # Mostrar mensaje de confirmación
    mensaje = f"Libro registrado exitosamente:\n\nTítulo: {titulo}\nAutor: {autor}\nAño: {anio}\nGénero: {genero}\nEstado: {estado}"
    messagebox.showinfo("Registro Exitoso", mensaje)

def limpiar_formulario():
    """Función para limpiar todos los campos del formulario"""
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    
    # Resetear variables
    var_genero.set(None)
    var_novela.set(0)
    var_ciencia.set(0)
    var_historia.set(0)
    var_estado.set(None)
    var_idioma.set("Español")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca SaberX - Registro de Libros")
ventana.geometry("600x700")
ventana.resizable(True, True)

# ==========================================
# FRAME 1: DETALLES DEL LIBRO
# ==========================================
frame_detalles = tk.LabelFrame(ventana, text="Detalles del Libro", padx=10, pady=10)
frame_detalles.pack(padx=10, pady=10, fill="x")

# Título
label_titulo = tk.Label(frame_detalles, text="Título:")
label_titulo.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_titulo = tk.Entry(frame_detalles, width=50)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

# Autor
label_autor = tk.Label(frame_detalles, text="Autor:")
label_autor.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_autor = tk.Entry(frame_detalles, width=50)
entry_autor.grid(row=1, column=1, padx=5, pady=5)

# Año de publicación
label_anio = tk.Label(frame_detalles, text="Año de Publicación:")
label_anio.grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_anio = tk.Entry(frame_detalles, width=50)
entry_anio.grid(row=2, column=1, padx=5, pady=5)

# ==========================================
# FRAME 2: GÉNERO Y CATEGORÍA
# ==========================================
frame_genero_categoria = tk.LabelFrame(ventana, text="Género y Categoría", padx=10, pady=10)
frame_genero_categoria.pack(padx=10, pady=10, fill="x")

# Género (Radiobuttons)
label_genero = tk.Label(frame_genero_categoria, text="Género:")
label_genero.grid(row=0, column=0, sticky="w", padx=5, pady=5)

var_genero = tk.StringVar()
radio_ficcion = tk.Radiobutton(frame_genero_categoria, text="Ficción", variable=var_genero, value="Ficción")
radio_ficcion.grid(row=0, column=1, padx=5, pady=5)
radio_no_ficcion = tk.Radiobutton(frame_genero_categoria, text="No Ficción", variable=var_genero, value="No Ficción")
radio_no_ficcion.grid(row=0, column=2, padx=5, pady=5)

# Categoría (Checkbuttons)
label_categoria = tk.Label(frame_genero_categoria, text="Categorías:")
label_categoria.grid(row=1, column=0, sticky="w", padx=5, pady=5)

var_novela = tk.IntVar()
var_ciencia = tk.IntVar()
var_historia = tk.IntVar()

check_novela = tk.Checkbutton(frame_genero_categoria, text="Novela", variable=var_novela)
check_novela.grid(row=1, column=1, padx=5, pady=5)
check_ciencia = tk.Checkbutton(frame_genero_categoria, text="Ciencia", variable=var_ciencia)
check_ciencia.grid(row=1, column=2, padx=5, pady=5)
check_historia = tk.Checkbutton(frame_genero_categoria, text="Historia", variable=var_historia)
check_historia.grid(row=1, column=3, padx=5, pady=5)

# ==========================================
# FRAME 3: ESTADO DE DISPONIBILIDAD
# ==========================================
frame_estado = tk.LabelFrame(ventana, text="Estado de Disponibilidad", padx=10, pady=10)
frame_estado.pack(padx=10, pady=10, fill="x")

var_estado = tk.StringVar()
radio_disponible = tk.Radiobutton(frame_estado, text="Disponible", variable=var_estado, value="Disponible")
radio_disponible.pack(side="left", padx=20, pady=5)
radio_prestado = tk.Radiobutton(frame_estado, text="Prestado", variable=var_estado, value="Prestado")
radio_prestado.pack(side="left", padx=20, pady=5)

# ==========================================
# FRAME 4: NÚMERO DE COPIAS
# ==========================================
frame_copias = tk.LabelFrame(ventana, text="Número de Copias", padx=10, pady=10)
frame_copias.pack(padx=10, pady=10, fill="x")

label_copias = tk.Label(frame_copias, text="Copias disponibles:")
label_copias.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_copias = tk.Entry(frame_copias, width=20)
entry_copias.grid(row=0, column=1, padx=5, pady=5)

# ==========================================
# FRAME 5: RESUMEN DEL LIBRO
# ==========================================
frame_resumen = tk.LabelFrame(ventana, text="Resumen del Libro", padx=10, pady=10)
frame_resumen.pack(padx=10, pady=10, fill="x")

label_resumen = tk.Label(frame_resumen, text="Resumen:")
label_resumen.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
text_resumen = tk.Text(frame_resumen, height=4, width=50)
text_resumen.grid(row=0, column=1, padx=5, pady=5)

# ==========================================
# FRAME 6: MENÚ DESPLEGABLE PARA IDIOMA
# ==========================================
frame_idioma = tk.LabelFrame(ventana, text="Idioma", padx=10, pady=10)
frame_idioma.pack(padx=10, pady=10, fill="x")

label_idioma = tk.Label(frame_idioma, text="Seleccione idioma:")
label_idioma.grid(row=0, column=0, sticky="w", padx=5, pady=5)

idiomas = ["Español", "Inglés", "Francés", "Portugués", "Alemán"]
var_idioma = tk.StringVar()
var_idioma.set(idiomas[0])  # Valor por defecto

menu_idioma = tk.OptionMenu(frame_idioma, var_idioma, *idiomas)
menu_idioma.grid(row=0, column=1, padx=5, pady=5)

# ==========================================
# FRAME 7: BOTONES DE ACCIÓN
# ==========================================
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

btn_registrar = tk.Button(frame_botones, text="Registrar Libro", command=registrar_libro, bg="#4CAF50", fg="white", width=15)
btn_registrar.pack(side="left", padx=10)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario, bg="#f44336", fg="white", width=15)
btn_limpiar.pack(side="left", padx=10)

# Iniciar bucle principal
ventana.mainloop()
