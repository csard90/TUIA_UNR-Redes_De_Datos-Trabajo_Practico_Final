import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import requests
import json


# Dirección IP y puerto del servidor FastAPI
server_ip = "127.0.0.1"       #IP DEL SERVIDOR, POR DEFAULT LOOPBACK

server_port = 8000

inicio = f"http://{server_ip}:{server_port}/libreria_entera"
requests.get(inicio)

# Variable para almacenar el endpoint
endpoint = ""

# Función para manejar los botones
def button_handler(endpoint_arg):
    global endpoint
    endpoint = endpoint_arg
    execute_action()

# Función para obtener la biblioteca completa
def get_libreria_entera():
    try:
        # Construir la URL completa con el endpoint seleccionado
        complete_url = f"http://{server_ip}:{server_port}{endpoint}"

        response = requests.get(complete_url)
        if response.status_code == 200:
            json_data = json.loads(response.json())

            # Limpiar el contenido actual del widget Text
            result_text.delete(1.0, tk.END)

            # Convertir los datos JSON a una cadena legible
            formatted_output = ""
            for item in json_data:
                for key, value in item.items():
                    formatted_output += f"{key}: {value}\n"
                formatted_output += "\n"

            # Insertar la cadena formateada en el widget Text
            result_text.insert(tk.END, formatted_output)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error en la solicitud: " + str(response.status_code))
    except requests.exceptions.RequestException:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error en la solicitud")

def buscar_libro():
    parameter = simpledialog.askstring("Buscar libro", "Ingrese el parámetro a buscar (author, country, language, title o year)")
    value = simpledialog.askstring("Buscar libro", "Ingrese una parte del valor del parámetro")
   
    if parameter and value:
        try:
            # Construir la URL completa con el endpoint seleccionado y los parámetros
            complete_url = f"http://{server_ip}:{server_port}{endpoint}?columna={parameter}&patron_busqueda={value}"

            response = requests.get(complete_url)
            if response.status_code == 200:
                json_data = json.loads(response.json())

                # Limpiar el contenido actual del widget Text
                result_text.delete(1.0, tk.END)

                # Convertir los datos JSON a una cadena legible
                formatted_output = ""
                for item in json_data:
                    for key, value in item.items():
                        formatted_output += f"{key}: {value}\n"
                    formatted_output += "\n"

                # Insertar la cadena formateada en el widget Text
                result_text.insert(tk.END, formatted_output)
            else:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Error en la solicitud: " + str(response.status_code))
        except requests.exceptions.RequestException:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error en la solicitud")

# Función para agregar un libro
def agregar_libro():
    autor = simpledialog.askstring("Agregar libro", "Ingrese el autor:")
    pais = simpledialog.askstring("Agregar libro", "Ingrese el país:")
    link_imagen = simpledialog.askstring("Agregar libro", "Ingrese el enlace de la imagen:")
    idioma = simpledialog.askstring("Agregar libro", "Ingrese el idioma:")
    link = simpledialog.askstring("Agregar libro", "Ingrese el enlace:")
    paginas = simpledialog.askstring("Agregar libro", "Ingrese el número de páginas:")
    titulo = simpledialog.askstring("Agregar libro", "Ingrese el título:")
    anio = simpledialog.askstring("Agregar libro", "Ingrese el año:")

    try:
        complete_url = f"http://{server_ip}:{server_port}{endpoint}?autor={autor}&pais={pais}&link_imagen={link_imagen}&idioma={idioma}&link={link}&paginas={paginas}&titulo={titulo}&a%C3%B1o={anio}"

        response = requests.post(complete_url)
        if response.status_code == 200:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Libro agregado exitosamente")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error en la solicitud: " + str(response.status_code))
    except requests.exceptions.RequestException:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error en la solicitud")

# Función para modificar un libro
def modificar_libro():
    titulo_cambiar = simpledialog.askstring("Modificar libro", "Ingrese el título del libro a modificar:")
    autor = simpledialog.askstring("Modificar libro", "Ingrese el autor:")
    pais = simpledialog.askstring("Modificar libro", "Ingrese el país:")
    link_imagen = simpledialog.askstring("Modificar libro", "Ingrese el enlace de la imagen:")
    idioma = simpledialog.askstring("Modificar libro", "Ingrese el idioma:")
    link = simpledialog.askstring("Modificar libro", "Ingrese el enlace:")
    paginas = simpledialog.askstring("Modificar libro", "Ingrese el número de páginas:")
    titulo = simpledialog.askstring("Modificar libro", "Ingrese el título:")
    anio = simpledialog.askstring("Modificar libro", "Ingrese el año:")

    try:
        complete_url = f"http://{server_ip}:{server_port}{endpoint}?eleccion={titulo_cambiar}&autor={autor}&pais={pais}&link_imagen={link_imagen}&idioma={idioma}&link={link}&paginas={paginas}&titulo={titulo}&a%C3%B1o={anio}"

        response = requests.put(complete_url)
        if response.status_code == 200:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Libro modificado exitosamente")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error en la solicitud: " + str(response.status_code))
    except requests.exceptions.RequestException:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error en la solicitud")

# Función para eliminar un libro
def eliminar_libro():
    titulo_eliminar = simpledialog.askstring("Eliminar libro", "Ingrese el título del libro a eliminar:")
    try:
        complete_url = f"http://{server_ip}:{server_port}{endpoint}?eleccion={titulo_eliminar}"

        response = requests.delete(complete_url)
        if response.status_code == 200:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Libro eliminado exitosamente")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error en la solicitud: " + str(response.status_code))
    except requests.exceptions.RequestException:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error en la solicitud")

# Función para ejecutar la acción correspondiente al botón presionado
def execute_action():
    if endpoint == "/libreria_entera":
        get_libreria_entera()
    elif endpoint == "/buscar_libro":
        buscar_libro()
    elif endpoint == "/agregar_libro":
        agregar_libro()
    elif endpoint == "/modificar_libro":
        modificar_libro()
    elif endpoint == "/eliminar_libro":
        eliminar_libro()

# Crear la ventana
window = tk.Tk()
window.title("BIBLIOTECA")

# Crear los botones
buttons = [
    {"text": "LIBRERIA ENTERA", "endpoint": "/libreria_entera"},
    {"text": "BUSCAR LIBRO", "endpoint": "/buscar_libro"},
    {"text": "AGREGAR LIBRO", "endpoint": "/agregar_libro"},
    {"text": "MODIFICAR LIBRO", "endpoint": "/modificar_libro"},
    {"text": "ELIMINAR LIBRO", "endpoint": "/eliminar_libro"},
]

for button_info in buttons:
    button = tk.Button(window, text=button_info["text"], command=lambda endpoint=button_info["endpoint"]: button_handler(endpoint))
    button.pack(pady=10)

# Crear el widget Text con deslizador
result_text = scrolledtext.ScrolledText(window, width=60, height=20)
result_text.pack()

# Ejecutar el bucle principal de la ventana
window.mainloop()
