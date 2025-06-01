# 24/05/2025
import tkinter as tk #importa el modulo tkinter y le asigna el alias(as) tk
from tkinter import simpledialog , messagebox #desde tkinter inporta los sub modulos simpledialog y messagebox

ventana = tk.Tk()
ventana.withdraw()
bienvenida = messagebox.askokcancel("Bienvenida", "Bienvenido al asistente para creacion de correos.")
if bienvenida:
    messagebox.showinfo("Inicio","Perfecto, comencemos!")
else:
    messagebox.showinfo("Cancelado", "Asistente cancelado, hasta luego")
    

nombre = simpledialog.askstring("Nombre", "Ingrese su nombre por favor:")
if nombre:
    nombre = nombre.strip().lower().replace(" ", "")
else:
    nombre=""

edad_str = simpledialog.askstring("Edad", "Ingrese su edad por favor: ")
try:
    edad =int(edad_str)
except (ValueError , TypeError):
    edad = 0
apodo = simpledialog.askstring("Apodo", "¿Tenés algún apodo que te guste?, ¿Cuál es?")
if apodo:
    apodo = apodo.strip().lower().replace(" ","")
else:
    apodo =""

opcion1= (f"{nombre}{apodo}{edad}@gmail.com")
opcion2= (f"{apodo}{nombre}{edad}@gmail.com")
opcion3= (f"{nombre}{edad}{apodo}@gmail.com")

mensaje_opciones =(
    f"Vamos a preparar tres opciones de correo con la información que nos proporcionaste:\n\n"
    f"1) {opcion1}\n"
    f"2) {opcion2}\n"
    f"3) {opcion3}\n\n"
    "¿Cuál te gusta más? (1, 2 o 3)"
)


eleccion = simpledialog.askstring("Elige tu correo", mensaje_opciones)

correos = {
    "1": opcion1,
    "2": opcion2,
    "3": opcion3
}

correo_elegido = correos.get(eleccion)

if correo_elegido:
    messagebox.showinfo("Correo elegido", f"Entonces tu correo será:\n{correo_elegido} 📧")
else:
    messagebox.showerror("Error", "Opción no válida. No se generó el correo.")

while True:
    contraseña = simpledialog.askstring("Contraseña", "Ingresa una contraseña:", show='*')
    if contraseña is None:
        # Usuario canceló
        messagebox.showwarning("Atención", "No ingresaste contraseña.")
        break

    contraseña_dos = simpledialog.askstring("Confirmar contraseña", "Ingresa nuevamente la contraseña:", show='*')
    if contraseña_dos is None:
        messagebox.showwarning("Atención", "No confirmaste la contraseña.")
        break

    if contraseña == contraseña_dos:
        messagebox.showinfo("Contraseña registrada", "La contraseña se registró con éxito. 🔑")
        break
    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden, vuelve a ingresarlas por favor 🔒")

messagebox.showinfo("Despedida", f"{nombre}, gracias por usar el creador de correos.\n****************************************")

ventana.destroy()
