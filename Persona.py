import secrets
class persona:

    genes = []
    #Método que genera los valores para los genes
    def generar_genes(self):
        for _ in range(10):
            aleatorio = secrets.randbelow(2)
            self.genes.append(aleatorio)

    #Método constructor de la clase persona que recoge una lista de genes
    def init(self, genes):
        self.genes = genes

    #Método que mezcla a dos personas y generar una persona nueva indicando el punto de cruce
    def cruzar_punto(self, persona2, punto):
        genes_cruzados = []
        #print("Punto de cruce: " + str(punto))
        for _ in range(10):
            if _ < punto:
                genes_cruzados.append(self.genes[_])
            else:
                genes_cruzados.append(persona2.genes[_])
        return persona(genes_cruzados)

    #Método que muta los genes de una persona
    def mutar_persona(self, probabilidad):
        genes_mutados = []
        for _ in range(10):
            aleatorio = secrets.randbelow(2)
            if aleatorio <= probabilidad:
                #print("Gen mutado: " + str(i))
                if self.genes[_] == 0:
                    genes_mutados.append(1)
                else:
                    genes_mutados.append(0)
            else:
                genes_mutados.append(self.genes[_])
        return persona(genes_mutados)
