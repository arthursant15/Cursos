class imc: 
    def __init__ (self,nome = '',idade = 0,peso = 0,altura = 0):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def imcPergunta(self):
        self.nome = input("Qual o seu nome? ")
        self.idade = int(input("Qual a sua idade? "))
        self.peso = float(input("Qual o seu peso? "))
        self.altura = float(input("Qual a sua altura? "))

    def imcCondicao(self): 
        self.imc = self.peso/(self.altura*self.altura)
        if (self.imc <= 18.5):
            return ("O paciente", self.nome ," está Abaixo do peso normal")
        if (self.imc <= 25):
            return ("Peso normal")
        if (self.imc <= 30 ):
            return ("Acima do peso normal")
        if (self.imc > 30 ):
            return ("Obesidade")
    
pessoa = imc()
pessoa.imcPergunta()
print(pessoa.imcCondicao())
    