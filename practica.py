import json
import requests
import os
#esto va a ser una api para descubrir distintos rasgos de distintas razas con las que se puede jugar a dragones y mazmorras.
try: 
    def datospordefecto():
        api_address="http://dnd5eapi.co/api/races/"
        url=api_address + raza
        resp = requests.get(url)
        if resp.status_code==200:
            datos=json.loads(resp.content)
        return datos

    def generardatosnuevos(raza):
        api_address="http://dnd5eapi.co/api/races/"
        url=api_address + raza
        resp = requests.get(url)
        if resp.status_code==200:
            datos=json.loads(resp.content)
            return datos
        elif resp.status_code==404: 
            return 0

    def consultaralineacion():
        print("Alineacion:",datos['alignment'])
        input("Pulse cualquier tecla para continuar")

    def consultarrasgosfisicos():
        print("Velocidad:",datos['speed'])
        print("Tamano:",datos['size'])
        print("Edad:",datos['age'])
        input("Pulse cualquier tecla para continuar")

    def consultarinicio():
        inicio=datos['starting_proficiencies']
        if len(inicio)!=0:
            for elemento in datos['starting_proficiencies']:
                print(elemento['name'])
        else:
            print("Esta raza no tiene ningunas abilidades o armas al iniciar la partida.")
        input("Pulse cualquier tecla para continuar")
    
    def consultarsubrazas():
        subrazas=datos['subraces']
        if len(subrazas)==0:
            print("Esta raza no tiene ninguna subraza conocida.")
        else:
            for elemento in datos['subraces']:
                print(elemento['name'])
        input("Pulse cualquier tecla para continuar")

    raza="elf"
    datos=datospordefecto()
    opcion=0
    while opcion!=6:
        os.system("cls")
        print("Bienvenido al menu de informacion sobre las distintas razas de los personajes de Dragones y Mazmorras.")
        print("1. Elegir raza a consultar, escrita en ingles. Raza actual: %s"%raza)
        print("2. Consultar la alineacion de %s"%raza)
        print("3. Consultar los rasgos fisicos de %s"%raza)
        print("4. Consultar las abilidades/armas de %s al iniciar la partida"%raza)
        print("5. Consultar las subrazas de %s"%raza)
        print("6. Salir del programa.")
        opcion=int(input("Seleccione una opcion: "))

        if opcion==1:
            print("Que raza desea consultar?")
            raza=input("")
            datos=generardatosnuevos(raza)
            if datos!=0: 
                print("A continuacion, podra consultar los datos de %s"%raza)    
            else:
                print("No existe la raza que esta buscando") 

            input("Pulse cualquier tecla para continuar ...")

        elif opcion==2:
            consultaralineacion()

        elif opcion==3:
            consultarrasgosfisicos()

        elif opcion==4:
            consultarinicio()

        elif opcion==5:
            consultarsubrazas()

        elif opcion==6:
            break
    
        else:
            print("Por favor, seleccione una opcion valida.")
except:
    print("Error.")