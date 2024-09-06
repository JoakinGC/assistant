# buscar.py
import webbrowser
import sys

def buscar(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        buscar(" ".join(sys.argv[1:]))
    else:
        print("Por favor, proporciona una consulta de búsqueda.")
