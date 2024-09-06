import winreg

def get_installed_programs():
    programs = []
    # Define las rutas del registro donde se almacenan las entradas de los programas instalados
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for path in registry_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    programs.append(program_name)
                except FileNotFoundError:
                    pass
                finally:
                    subkey.Close()
            key.Close()
        except FileNotFoundError:
            pass

    return programs

if __name__ == "__main__":
    programs = get_installed_programs()
    for program in programs:
        print(program)
