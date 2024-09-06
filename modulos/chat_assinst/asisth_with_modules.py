import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from modulos.api_huggi.api import ChatAPI

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente de Chat")
        
       
        self.root.geometry("400x500")
        
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        
        self.chat_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)  
        
        
        self.entry_message = tk.Entry(main_frame, font=("Arial", 14))
        self.entry_message.pack(fill="x", padx=10, pady=10)
        self.entry_message.bind("<Return>", self.send_message)
        
        
        send_button = tk.Button(main_frame, text="Enviar", command=self.send_message)
        send_button.pack(pady=5)

        self.chat_api = ChatAPI()

     
        self.display_message("Asistente", "Hola, ¿cómo puedo ayudarte hoy?")

    def display_message(self, sender, message):
        
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)  

    def send_message(self, event=None):
        
        user_message = self.entry_message.get()
        if user_message.strip() != "":
            
            self.display_message("Tú", user_message)
            self.entry_message.delete(0, tk.END)  
            
            Thread(target=self.process_message, args=(user_message,)).start()

    def process_message(self, user_message):
        
        messages = [{"role": "user", "content": user_message}]
        response = self.chat_api.speak_response(messages)
        
       
        assistant_message = response['content'] if response else "Lo siento, no puedo procesar esa solicitud en este momento."
        self.display_message("Asistente", assistant_message)


