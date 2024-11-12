import os 

def jugadores_registrados():
    cuentas_path = r"Jugadores/"
    numero_registros = 0

    for path in os.listdir(cuentas_path):
    # revisa si existen archivos en la carpeta
        if os.path.isfile(os.path.join(cuentas_path, path)):
            numero_registros += 1
    return numero_registros


