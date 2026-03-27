import tkinter as tk
from tkinter import messagebox
import mysql.connector

def extraer_numero_id(cadena):
    """Extrae el ID de una cadena formateada"""
    valores = cadena.split(',')
    for valor in valores:
        if "ID" in valor:
            numero_id = int(valor.split(':')[1].strip())
            return numero_id
    return None

class VideojuegosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Videojuegos")
        self.root.geometry("700x500")
        
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'user': 'root',
            'password': '',  # Cambiar por tu contraseña
            'host': 'localhost',
            'database': 'semana8'
        }
        
        # Crear conexión
        self.connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.connection.cursor()
        
        # === ELEMENTOS DE LA INTERFAZ GRÁFICA ===
        
        # Labels y Entries
        self.label_id = tk.Label(root, text="ID:")
        self.entry_id = tk.Entry(root)
        
        self.label_titulo = tk.Label(root, text="Título:")
        self.entry_titulo = tk.Entry(root)
        
        self.label_genero = tk.Label(root, text="Género:")
        self.entry_genero = tk.Entry(root)
        
        self.label_clasificacion = tk.Label(root, text="Clasificación:")
        self.entry_clasificacion = tk.Entry(root)
        
        self.label_plataforma = tk.Label(root, text="Plataforma:")
        self.entry_plataforma = tk.Entry(root)
        
        # Botones CRUD
        self.btn_agregar = tk.Button(root, text="Agregar Videojuego", 
                                     command=self.agregar_videojuego)
        self.btn_mostrar = tk.Button(root, text="Mostrar Videojuegos", 
                                     command=self.mostrar_videojuegos)
        self.btn_borrar = tk.Button(root, text="Borrar Videojuego", 
                                    command=self.borrar_videojuego)
        self.btn_actualizar = tk.Button(root, text="Actualizar Videojuego", 
                                        command=self.actualizar_videojuego)
        
        # Lista para mostrar videojuegos
        self.lista_videojuegos = tk.Listbox(root, selectmode=tk.SINGLE, width=80)
        self.lista_videojuegos.bind('<<ListboxSelect>>', self.cargar_datos_seleccionados)
        
        # === UBICACIÓN EN LA INTERFAZ (GRID) ===
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_titulo.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_genero.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_genero.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_clasificacion.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.entry_clasificacion.grid(row=3, column=1, padx=10, pady=5)
        
        self.label_plataforma.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.entry_plataforma.grid(row=4, column=1, padx=10, pady=5)
        
        self.lista_videojuegos.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.btn_agregar.grid(row=6, column=0, padx=5, pady=5)
        self.btn_mostrar.grid(row=6, column=1, padx=5, pady=5)
        self.btn_borrar.grid(row=7, column=0, padx=5, pady=5)
        self.btn_actualizar.grid(row=7, column=1, padx=5, pady=5)
    
    # === OPERACIÓN CREATE (CREAR) ===
    def agregar_videojuego(self):
        try:
            videojuego_id = self.entry_id.get()
            titulo = self.entry_titulo.get()
            genero = self.entry_genero.get()
            clasificacion = self.entry_clasificacion.get()
            plataforma = self.entry_plataforma.get()
            
            query = """INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) 
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (videojuego_id, titulo, genero, clasificacion, plataforma)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            messagebox.showinfo("Éxito", "Videojuego agregado correctamente")
            self.limpiar_campos()
            self.mostrar_videojuegos()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar videojuego: {str(e)}")
    
    # === OPERACIÓN READ (LEER) ===
    def mostrar_videojuegos(self):
        try:
            self.lista_videojuegos.delete(0, tk.END)
            
            query = "SELECT * FROM Videojuegos"
            self.cursor.execute(query)
            videojuegos = self.cursor.fetchall()
            
            for juego in videojuegos:
                self.lista_videojuegos.insert(tk.END, 
                    f"ID: {juego[0]}, Título: {juego[1]}, Género: {juego[2]}, "
                    f"Clasif: {juego[3]}, Plataforma: {juego[4]}")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Error al mostrar videojuegos: {str(e)}")
    
    # === OPERACIÓN DELETE (ELIMINAR) ===
    def borrar_videojuego(self):
        try:
            seleccion = self.lista_videojuegos.curselection()
            if seleccion:
                videojuego_seleccionado = self.lista_videojuegos.get(seleccion[0])
                videojuego_id = extraer_numero_id(videojuego_seleccionado)
                
                query = "DELETE FROM Videojuegos WHERE ID = %s"
                self.cursor.execute(query, (videojuego_id,))
                self.connection.commit()
                
                messagebox.showinfo("Éxito", f"Videojuego con ID {videojuego_id} borrado correctamente")
                self.mostrar_videojuegos()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Advertencia", "Por favor selecciona un videojuego de la lista")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al borrar videojuego: {str(e)}")
    
    # === OPERACIÓN UPDATE (ACTUALIZAR) ===
    def actualizar_videojuego(self):
        try:
            videojuego_id = self.entry_id.get()
            titulo = self.entry_titulo.get()
            genero = self.entry_genero.get()
            clasificacion = self.entry_clasificacion.get()
            plataforma = self.entry_plataforma.get()
            
            query = """UPDATE Videojuegos 
                       SET Titulo = %s, Genero = %s, Clasificacion = %s, Plataforma = %s 
                       WHERE ID = %s"""
            values = (titulo, genero, clasificacion, plataforma, videojuego_id)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            messagebox.showinfo("Éxito", f"Videojuego con ID {videojuego_id} actualizado correctamente")
            self.mostrar_videojuegos()
            self.limpiar_campos()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar videojuego: {str(e)}")
    
    # Cargar datos seleccionados en los campos
    def cargar_datos_seleccionados(self, event):
        seleccion = self.lista_videojuegos.curselection()
        if seleccion:
            videojuego_seleccionado = self.lista_videojuegos.get(seleccion[0])
            videojuego_id = extraer_numero_id(videojuego_seleccionado)
            
            query = "SELECT * FROM Videojuegos WHERE ID = %s"
            self.cursor.execute(query, (videojuego_id,))
            datos = self.cursor.fetchone()
            
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, datos[0])
            self.entry_titulo.delete(0, tk.END)
            self.entry_titulo.insert(0, datos[1])
            self.entry_genero.delete(0, tk.END)
            self.entry_genero.insert(0, datos[2])
            self.entry_clasificacion.delete(0, tk.END)
            self.entry_clasificacion.insert(0, datos[3])
            self.entry_plataforma.delete(0, tk.END)
            self.entry_plataforma.insert(0, datos[4])
    
    # Limpiar campos de entrada
    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_genero.delete(0, tk.END)
        self.entry_clasificacion.delete(0, tk.END)
        self.entry_plataforma.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideojuegosApp(root)
    root.mainloop()
    
    # Cierre de conexión al salir
    app.cursor.close()
    app.connection.close()