import pyautogui
from screeninfo import get_monitors

def print_screen_info():
    # Obtener información de todas las pantallas
    monitors = get_monitors()
    
    print("Información de las pantallas:")
    for i, monitor in enumerate(monitors):
        print(f"Pantalla {i + 1}:")
        print(f"  Resolución: {monitor.width}x{monitor.height}")
        print(f"  Posición: ({monitor.x}, {monitor.y})")
    
    # Obtener la posición actual del ratón
    mouse_x, mouse_y = pyautogui.position()
    print("\nPosición actual del ratón:")
    print(f"  ({mouse_x}, {mouse_y})")

if __name__ == "__main__":
    print_screen_info()
