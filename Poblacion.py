import secrets
import Persona

poblacion = []
poblacion_cruzada_mutada = []
genes = []
personas_cruzadas_mutadas = []

# Método que genera una población con personas
def generar_poblacion(x):
    for _ in range(x):
        persona = Persona.persona(genes)
        persona.generar_genes()
        poblacion.append(persona)

# Método que cruza y muta a un grupo de personas según una probabilidad
def cruzar_mutar_personas(grupo_personas, probabilidad):

    if probabilidad < 0.5:
        print("La población se ha mutado")
    for persona in grupo_personas:
        aleatorio = secrets.randbelow(len(grupo_personas))
        punto = secrets.randbelow(10)
        persona_cruzada = persona.cruzar_punto(grupo_personas[aleatorio], punto)
        if probabilidad < 0.5:
            persona_mutada = persona_cruzada.mutar_persona(probabilidad)
            personas_cruzadas_mutadas.append(persona_mutada)
        else:
            personas_cruzadas_mutadas.append(persona_cruzada)
    return personas_cruzadas_mutadas

# Método que muestra una población de personas
def mostrar_poblacion(grupo_personas):
    for persona in grupo_personas:
        print(persona.genes)

#Genero una poblacion y despues esta sera cruzada y mutada
generar_poblacion(10)
print("Población inicial:")
mostrar_poblacion(poblacion)
print("\n")
print("Población cruzada y mutada: ")
mostrar_poblacion(cruzar_mutar_personas(poblacion, secrets.randbelow(2)))
