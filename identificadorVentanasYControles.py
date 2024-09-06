from pywinauto import Desktop
import pyautogui
import cv2
import numpy as np
import os

def get_window_info():
    # Conectar a todas las ventanas visibles en el escritorio
    windows = Desktop(backend="uia").windows()

    print("Información de las ventanas:")
    for window in windows:
        print(f"Título: {window.window_text()}")
        rect = window.rectangle()
        print(f"  Posición: ({rect.left}, {rect.top})")
        print(f"  Tamaño: ({rect.width()}x{rect.height()})")

def capture_screen():
    # Capturar la pantalla
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    return screenshot_cv

def find_image_on_screen(image_path, screenshot):
    if not os.path.exists(image_path):
        print(f"Error: La imagen '{image_path}' no existe.")
        return

    # Cargar la imagen a buscar
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if template is None:
        print(f"Error: No se pudo leer la imagen '{image_path}'.")
        return

    if screenshot.shape[2] != template.shape[2]:
        print("Error: Las imágenes tienen un número diferente de canales.")
        return

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    # Umbral de coincidencia
    threshold = 0.8
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenshot, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    cv2.imshow('Detected', screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_detailed_window_info():
    # Conectar a todas las ventanas visibles en el escritorio
    windows = Desktop(backend="uia").windows()

    print("Información detallada de las ventanas y sus controles:")
    for window in windows:
        try:
            print(f"\nVentana: {window.window_text()}")
            rect = window.rectangle()
            print(f"  Posición: ({rect.left}, {rect.top})")
            print(f"  Tamaño: ({rect.width()}x{rect.height()})")

            # Enumerar los controles dentro de la ventana
            controls = window.descendants()
            for control in controls:
                print(f"    Control: {control.window_text()}")
                control_rect = control.rectangle()
                print(f"      Posición: ({control_rect.left}, {control_rect.top})")
                print(f"      Tamaño: ({control_rect.width()}x{control_rect.height()})")
        except Exception as e:
            print(f"  No se pudo obtener la información de la ventana: {e}")


    


if __name__ == "__main__":
    # Obtener información de las ventanas
    get_window_info()

    # Capturar la pantalla
    screenshot = capture_screen()

    # Buscar una imagen específica en la pantalla (por ejemplo, un icono)
    # Reemplaza 'icon.png' con la ruta a la imagen que deseas buscar
    find_image_on_screen('icon.png', screenshot)
    get_detailed_window_info()
