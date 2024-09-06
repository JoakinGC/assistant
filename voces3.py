import tkinter as tk
from gtts import gTTS
import os
from tkinter import filedialog

def convertir_a_voz():
    texto = texto_entrada.get("1.0", tk.END).strip()
    if not texto:
        resultado_label.config(text="Por favor, ingrese algún texto.")
        return

    lang = "es"
    speech = gTTS(text=texto, lang=lang, slow=True)
    archivo = "output.mp3"
    speech.save(archivo)

    # Reproducir el archivo
    os.system(f"start {archivo}")

    resultado_label.config(text="Texto convertido a voz y archivo guardado como 'output.mp3'.")

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, "r") as f:
            contenido = f.read().replace("\n", " ")
            texto_entrada.delete("1.0", tk.END)
            texto_entrada.insert(tk.END, contenido)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversión de Texto a Voz")

# Configuración de widgets
texto_entrada = tk.Text(ventana, height=10, width=50)
texto_entrada.pack(pady=10)

convertir_boton = tk.Button(ventana, text="Convertir a Voz", command=convertir_a_voz)
convertir_boton.pack(pady=10)

cargar_boton = tk.Button(ventana, text="Cargar Archivo de Texto", command=seleccionar_archivo)
cargar_boton.pack(pady=10)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
