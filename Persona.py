import secrets
class persona:

    genes = []
    #Método que genera los valores para los genes
    def generarGenes(self):
        for i in range(10):
            aleatorio = secrets.randbelow(2)
            self.genes.append(aleatorio)

    #Método constructor de la clase persona que recoge una lista de genes
    def init(self, genes):
        self.genes = genes

    #Método que mezcla a dos personas y generar una persona nueva indicando el punto de cruce
    def cruzarPunto(self, persona2, punto):
        genesCruzados = []
        #print("Punto de cruce: " + str(punto))
        for i in range(10):
            if i < punto:
                genesCruzados.append(self.genes[i])
            else:
                genesCruzados.append(persona2.genes[i])
        return persona(genesCruzados)

    #Método que muta los genes de una persona
    def mutarPersona(self, probabilidad):
        genesMutados = []

        for i in range(10):
            aleatorio = secrets.randbelow(2)
            if aleatorio <= probabilidad:
                #print("Gen mutado: " + str(i))
                if self.genes[i] == 0:
                    genesMutados.append(1)
                else:
                    genesMutados.append(0)
            else:
                genesMutados.append(self.genes[i])
        return persona(genesMutados)
