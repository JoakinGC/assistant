from huggingface_hub import InferenceClient
from googletrans import Translator
from modulos.program_operations.program_operations import speak

class ChatAPI:
    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.2", token="your_api_key"):
        self.client = InferenceClient(model=model, token=token)
        self.translator = Translator()

    def translate(self, text, src, dest):
        try:
            translation = self.translator.translate(text, src=src, dest=dest)
            return translation.text
        except Exception as e:
            print(f"Error en la traducción: {e}")
            return text  

    def chat(self, messages):
        response = ""
        try:
            for message in self.client.chat_completion(messages=messages, max_tokens=500, stream=True):
                response += message.choices[0].delta.content
        except Exception as e:
            print(f"Error al generar la respuesta: {e}")
        return response

    def speak_response(self, messages):
        response = self.chat(messages)
        translated_response = self.translate(response, src='en', dest='es')
        speak(translated_response)
