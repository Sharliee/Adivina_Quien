# Carlos Andres Riveramelo Del Toro
# Sistemas Expertos
# Practica 2: Adiivina Quien

Personajes = [
    {
    "Personaje":    "Jazmin",
    "Genero":       "Mujer",
    "Ocupacion":    "Princesa",
    "Cabello":      "Negro",
    "Piel":         "Morena",
    "Vestimenta":   "Verde"
    },
    
    {
    "Personaje":    "Blancanieves",
    "Genero":       "Mujer",
    "Ocupacion":    "Princesa",
    "Cabello":      "Negro",
    "Piel":         "Blanca",
    "Vestimenta":   "Amarillo"
    },
    
    {
    "Personaje":    "Mulan",
    "Genero":       "Mujer",
    "Ocupacion":    "Guerrera",
    "Cabello":      "Negro",
    "Piel":         "Amarilla",
    "Vestimenta":   "Verde"
    },
    
    {
    "Personaje":    "Aurora",
    "Genero":       "Mujer",
    "Ocupacion":    "Princesa",
    "Cabello":      "Rubio",
    "Piel":         "Blanca",
    "Vestimenta":   "Rosa"
    },
    
    {
    "Personaje":    "Cenicienta",
    "Genero":       "Mujer",
    "Ocupacion":    "Princesa",
    "Cabello":      "Rubio",
    "Piel":         "Blanca",
    "Vestimenta":   "Azul"
    },
    
    {
    "Personaje":    "Pocahontas",
    "Genero":       "Mujer",
    "Ocupacion":    "Guerrera",
    "Cabello":      "Negro",
    "Piel":         "Morena",
    "Vestimenta":   "Cafe"
    },
    
    {
    "Personaje":    "Bella",
    "Genero":       "Mujer",
    "Ocupacion":    "Princesa",
    "Cabello":      "Castaño",
    "Piel":         "Blanca",
    "Vestimenta":   "Amarillo"
    },
    
    {
    "Personaje":    "Ariel",
    "Genero":       "Mujer",
    "Ocupacion":    "Sirena",
    "Cabello":      "Pelirrojo",
    "Piel":         "Blanca",
    "Vestimenta":   "Rosa"
    },
    
    {
    "Personaje":    "Aladdín",
    "Genero":       "Hombre",
    "Ocupacion":    "Ladron",
    "Cabello":      "Negro",
    "Piel":         "Morena",
    "Vestimenta":   "Morado"
    },
    
    {
    "Personaje":    "Hércules",
    "Genero":       "Hombre",
    "Ocupacion":    "Guerrero",
    "Cabello":      "Castaño",
    "Piel":         "Blanco",
    "Vestimenta":   "Cafe"
    },
    
    {
    "Personaje":    "Eric",
    "Genero":       "Hombre",
    "Ocupacion":    "Principe",
    "Cabello":      "Negro",
    "Piel":         "Blanca",
    "Vestimenta":   "Blanco"
    },
    
    {
    "Personaje":    "Felipe",
    "Genero":       "Hombre",
    "Ocupacion":    "Principe",
    "Cabello":      "Pelirrojo",
    "Piel":         "Blanca",
    "Vestimenta":   "Turquesa"
    },
    
    {
    "Personaje":    "Adam",
    "Genero":       "Hombre",
    "Ocupacion":    "Principe",
    "Cabello":      "Castaño",
    "Piel":         "Blanca",
    "Vestimenta":   "Azul"
    },
    
    {
    "Personaje":    "Flynn",
    "Genero":       "Hombre",
    "Ocupacion":    "Leñador",
    "Cabello":      "Negro",
    "Piel":         "Blanca",
    "Vestimenta":   "Verde"
    },
    ]

jugar = input("¿Iniciar juego? (sí/no): ").strip().lower()

def adivina_personaje():
    if(jugar == "si"):
        print(" ")
        print("Bienvenido al juego de Adivina Quién con personajes de Disney.")
        print(" ")
        
        caracteristicas = {
            "Genero":       None,
            "Ocupacion":    None,
            "Cabello":      None,
            "Piel":         None,
            "Vestimenta":   None,
            }
        
        # Pregunta por el genero y lo guarda en la variable
        Generos = ["Hombre", "Mujer"]
        for Genero in Generos:
            if caracteristicas["Genero"] is not None:
                break
            respuesta = input(f"¿Tu personaje es {Genero}? (si/no): ").strip().lower()
            print(" ")
            if respuesta == "si":
                caracteristicas["Genero"] = Genero
        
        # Pregunta por la ocupacion y lo guarda en la variable
        Ocupaciones = ["Princesa", "Guerrera", "Sirena", "Ladron", "Guerrero", "Principe", "Leñador"]
        for Ocupacion in Ocupaciones:
            if caracteristicas["Ocupacion"] is not None:
                break
            respuesta = input(f"¿Tu personaje es {Ocupacion}? (si/no): ").strip().lower()
            print(" ")
            if respuesta == "si":
                caracteristicas["Ocupacion"] = Ocupacion
        
        # Pregunta por el color de cabello y lo guarda en la variable
        Cabellera = ["Negro", "Rubio", "Castaño", "Pellirrojo"]
        for Cabello in Cabellera:
            if caracteristicas["Cabello"] is not None:
                break
            respuesta = input(f"¿Tu personaje tiene el cabello {Cabello}? (si/no): ").strip().lower()
            print(" ")
            if respuesta == "si":
                caracteristicas["Cabello"] = Cabello
        
        # Pregunta por la piel y lo guarda en la variable
        Pieles = ["Morena", "Blanca", "Amarilla"]
        for Piel in Pieles:
            if caracteristicas["Piel"] is not None:
                break
            respuesta = input(f"¿Tu personaje es de piel {Piel}? (si/no): ").strip().lower()
            print(" ")
            if respuesta == "si":
                caracteristicas["Piel"] = Piel
        
        # Pregunta por la vestimenta y lo guarda en la variable
        Vestimentas = ["Verde", "Amarillo", "Rosa", "Azul", "Cafe", "Morado", "Blanco", "Turquesa"]
        for Vestimenta in Vestimentas:
            if caracteristicas["Vestimenta"] is not None:
                break
            respuesta = input(f"¿Tu personaje tiene una vestimenta {Vestimenta}? (si/no): ").strip().lower()
            print(" ")
            if respuesta == "si":
                caracteristicas["Vestimenta"] = Vestimenta
        
        for caracteristicas in Personajes:
            if [caracteristicas[key] is None or (Personajes[key] == caracteristicas[key]) for key in caracteristicas.keys()]:
                print("Tu personaje es {Personaje}")
            else:
                print("No pude adivinar tu personaje")
                break
                
adivina_personaje()