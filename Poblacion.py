import secrets
import Persona

poblacion = []
poblacionCruzadaMutada = []
genes = []
personasCruzadasMutadas = []

# Método que genera una población con personas
def generar_Poblacion(x):
    for _ in range(x):
        persona = Persona.persona(genes)
        persona.generar_Genes()
        poblacion.append(persona)

# Método que cruza y muta a un grupo de personas según una probabilidad
def cruzar_Mutar_Personas(grupoPersonas, probabilidad):

    if probabilidad < 0.5:
        print("La población se ha mutado")
    for persona in grupoPersonas:
        aleatorio = secrets.randbelow(len(grupoPersonas))
        punto = secrets.randbelow(10)
        personaCruzada = persona.cruzar_Punto(grupoPersonas[aleatorio], punto)
        if probabilidad < 0.5:
            personaMutada = personaCruzada.mutar_Persona(probabilidad)
            personasCruzadasMutadas.append(personaMutada)
        else:
            personasCruzadasMutadas.append(personaCruzada)
    return personasCruzadasMutadas

# Método que muestra una población de personas
def mostrar_Poblacion(grupoPersonas):
    for persona in grupoPersonas:
        print(persona.genes)

#Genero una poblacion y despues esta sera cruzada y mutada
generar_Poblacion(10)
print("Población inicial:")
mostrar_Poblacion(poblacion)
print("\n")
print("Población cruzada y mutada: ")
mostrar_Poblacion(cruzar_Mutar_Personas(poblacion, secrets.randbelow(2)))
