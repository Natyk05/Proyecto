import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


__window_size = "450x400+400+200"

#________________________________________________________________________________________________#

# # MENU SCREEN
# menu_screen = tk.Tk()
# menu_screen.title("Data Entry Form")

# etiqueta = tk.Label(menu_screen, text="Mi Restaurante",
#                     font=("Arial", 18), pady=10)
# etiqueta.pack()
# frame = tk.Frame(menu_screen)
# frame.pack()

# user_info_frame = tk.LabelFrame(frame, text="Bienvenido",
#                     font=("Arial", 14), pady=10)
# user_info_frame.grid(row=0, column=0, padx=10, pady=10)

# boton_gestion_platos = tk.Button(user_info_frame, text="Gestión platos",#,command=gestion_platos_screen,
#                     font=("Arial", 12), pady=10)

# boton_gestion_platos.grid(row=1, column=0, sticky="news", padx=100, pady=10)

# boton_gestion_mesas = tk.Button(user_info_frame, text="Gestión mesas",
#                     font=("Arial", 12), pady=10)

# boton_gestion_mesas.grid(row=2, column=0, sticky="news", padx=100, pady=10)

# boton_gestion_pedidos = tk.Button(user_info_frame, text="Gestión pedidos",
#                     font=("Arial", 12), pady=10)

# boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)

# boton_cerrar_sesion = tk.Button(user_info_frame, text="Cerrar sesión",
#                     font=("Arial", 12), pady=10)

# boton_cerrar_sesion.grid(row=4, column=0, sticky="news", padx=100, pady=10)
# #menu_screen.withdraw()

# menu_screen.geometry(__window_size)
# menu_screen.mainloop()
#________________________________________________________________________________________________#
#Agregar platos

# matriz = []
# def imprimir_matriz():
#     for plato in matriz:
#         print(plato)


# def agregar_plato():
#     nombre = name__entry.get()
#     precio = precio_entry.get()
#     descripcion = descripcion_entry.get()
#     disponibilidad = disponibilidad_entry.get()

#     # Validación del campo nombre
#     if not nombre:
#         messagebox.showerror("Error", "El campo nombre es obligatorio")
#         return

#     # Validación del campo precio
#     if not precio.isdigit() or int(precio) <= 0:
#         messagebox.showerror("Error", "El campo precio debe ser un número mayor a 0")
#         return

#     # Validación del campo descripción
#     if len(descripcion) > 100:
#         messagebox.showerror("Error", "El campo descripción no puede tener más de 100 caracteres")
#         return

#     # Validación del campo disponibilidad
#     if disponibilidad.lower() not in ["si", "no"]:
#         messagebox.showerror("Error", "El campo disponibilidad solo puede ser 'si' o 'no'")
#         return

#     plato = [nombre, precio, descripcion, disponibilidad]
#     matriz.append(plato)

#     messagebox.showinfo("Información", "Plato agregado correctamente")

#     # Limpiar los campos de texto
#     name__entry.delete(0, tk.END)
#     precio_entry.delete(0, tk.END)
#     descripcion_entry.delete(0, tk.END)
#     disponibilidad_entry.delete(0, tk.END)

# agregar_platos = tk.Tk()
# agregar_platos.title("Data Entry Form")

# etiqueta = tk.Label(agregar_platos, text="Mi Restaurante",
#                     font=("Arial", 18), pady=10)
# etiqueta.pack()
# frame = tk.Frame(agregar_platos)
# frame.pack()

# agregar_platos_frame = tk.LabelFrame(frame, text="Agregar platos",
#                                  font=("Arial", 14), pady=10)

# agregar_platos_frame.grid(row=0, column=0, padx=100, pady=10)

# espacio_label = tk.Label(agregar_platos_frame, text="")
# espacio_label.grid(row=0, column=0)
# espacio_label = tk.Label(agregar_platos_frame, text="")
# espacio_label.grid(row=0, column=1)

# name_label = tk.Label(agregar_platos_frame, text="Nombre",
#                                  font=("Arial", 12), pady=10)
# name_label.grid(row=1, column=0)
# precio_label = tk.Label(agregar_platos_frame, text="Precio",
#                                  font=("Arial", 12), pady=10)
# precio_label.grid(row=1, column=2)

# name__entry = tk.Entry(agregar_platos_frame)
# precio_entry = tk.Entry(agregar_platos_frame)
# name__entry.grid(row=2, column=0)
# precio_entry.grid(row=2, column=2)

# espacio_label = tk.Label(agregar_platos_frame, text="")
# espacio_label.grid(row=3, column=0)
# espacio_label = tk.Label(agregar_platos_frame, text="")
# espacio_label.grid(row=3, column=1)

# descripcion_label = tk.Label(agregar_platos_frame, text="Descripción",
#                                  font=("Arial", 12), pady=10)

# descripcion_label.grid(row=4, column=0)
# disponibilidad_label = tk.Label(agregar_platos_frame, text="Disponibilidad",
#                                  font=("Arial", 12), pady=10)

# disponibilidad_label.grid(row=4, column=2)

# descripcion_entry = tk.Entry(agregar_platos_frame)
# disponibilidad_entry = tk.Entry(agregar_platos_frame)
# descripcion_entry.grid(row=5, column=0)
# disponibilidad_entry.grid(row=5, column=2)

# boton_agregar_platos = tk.Button(frame ,text="Agregar", command=agregar_plato,
#                                  font=("Arial", 12), pady=10)

# boton_agregar_platos.grid(row=6, column=0, sticky="news", padx=30, pady=10)

# boton_imprimir = tk.Button(frame, text="Imprimir", command=imprimir_matriz)
# boton_imprimir.grid(row=7, column=0, sticky="news", padx=30, pady=10)

# agregar_platos.geometry(__window_size)

# agregar_platos_frame.mainloop()

#________________________________________________________________________________________________#'

# # GESTION DE PLATOS
# gestion_platos = tk.Tk()
# gestion_platos.title("Gestion platos")

# etiqueta = tk.Label(gestion_platos, text="Mi Restaurante",
#                     font=("Arial", 18), pady=10)
# etiqueta.pack()
# frame = tk.Frame(gestion_platos)
# frame.pack()

# user_info_frame = tk.LabelFrame(frame, text="Gestion de platos",
#                                 font=("Arial", 14), pady=20)

# user_info_frame.grid(row=0, column=0, padx=10, pady=10)

# # Botones
# boton_gestion_platos = tk.Button(user_info_frame, text="Agregar",
#                                  font=("Arial", 10), pady=10)

# boton_gestion_platos.grid(row=1, column=0, sticky="news", padx=100, pady=10)

# boton_gestion_mesas = tk.Button(user_info_frame, text="Eliminar",
#                                 font=("Arial", 10), pady=10)

# boton_gestion_mesas.grid(row=2, column=0, sticky="news", padx=100, pady=10)

# boton_gestion_pedidos = tk.Button(user_info_frame, text="Actualizar",
#                                   font=("Arial", 10), pady=10)

# boton_gestion_pedidos.grid(row=3, column=0, sticky="news", padx=100, pady=10)


# #gestion_platos.withdraw()
# gestion_platos.geometry(__window_size)
# gestion_platos.mainloop()

#________________________________________________________________________________________________#