import secrets
import Persona

poblacion = []
poblacionCruzadaMutada = []
genes = []
personasCruzadasMutadas = []
punto = secrets.randbelow(10)

# Método que genera una población con personas
def generarPoblacion(x):
    for i in range(x):
        persona = Persona.persona(genes)
        persona.generarGenes()
        poblacion.append(persona)

# Método que cruza y muta a un grupo de personas según una probabilidad
def cruzarMutarPersonas(grupoPersonas, probabilidad):

    if probabilidad < 0.5:
        print("La población se ha mutado")
    for persona in grupoPersonas:
        aleatorio = secrets.randbelow(len(grupoPersonas))
        personaCruzada = persona.cruzarPunto(grupoPersonas[aleatorio], punto)
        if probabilidad < 0.5:
            personaMutada = personaCruzada.mutar(probabilidad)
            personasCruzadasMutadas.append(personaMutada)
        else:
            personasCruzadasMutadas.append(personaCruzada)
    return personasCruzadasMutadas

# Método que muestra una población de personas
def mostrarPoblacion(grupoPersonas):
    for persona in grupoPersonas:
        print(persona.genes)

#Genero una poblacion y despues esta sera cruzada y mutada
generarPoblacion(10)
print("Población inicial:")
mostrarPoblacion(poblacion)
print("\n")
print("Población cruzada y mutada: ")
mostrarPoblacion(cruzarMutarPersonas(poblacion, secrets.randbelow(2)))
