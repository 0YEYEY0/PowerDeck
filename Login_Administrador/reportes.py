import os
import json

#Funcion conseguir total de jugadores registrados
def jugadores_registrados():
    cuentas_path = r"Jugadores/"
    numero_registros = 0

    for path in os.listdir(cuentas_path):
    # revisa si existen archivos en la carpeta
        if os.path.isfile(os.path.join(cuentas_path, path)) and path != "correos.json":
            numero_registros += 1
    return numero_registros

#Funcion conseguir cuantas veces una carta fuera usadas
def uso_carta(carta_usada, es_principal=True):
    cuentas_path = r"Jugadores/"
    nom_principal=[]
    nom_variante = []
    
    for cuentas in os.listdir(cuentas_path):  
        if not "correos.json" in cuentas:
            cuentas = r"Jugadores/"+str(cuentas)
            
            with open(cuentas, "r") as archivo:
                datos = json.load(archivo)

                if datos["nombre_usuario"]:
                    if "mazos" in datos.keys():
                        for cartas in datos["mazos"]:
                            for usadas in cartas["cartas"]:
                                if True == usadas["es_principal"]:
                                    nom_principal.append(usadas["nombre"])
                                else:
                                    nom_variante.append(usadas["nombre"])
                    else:
                        pass
                        
    if es_principal:
        return nom_principal.count(carta_usada)
    else:
        return nom_variante.count(carta_usada)
    
    
                            

