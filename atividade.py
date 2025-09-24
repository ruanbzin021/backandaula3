# Atributos de classe (rodas) são compartilhados por todos os objetos.
class Carro:
    rodas = 4
    
    # Atributos de instância (marca, ano) são únicos de cada objeto.
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    # Método de instância usa self e trabalha com dados do objeto.
    def ligar(self):
        print(f"O carro {self.marca} ({self.ano}) está ligado.")
    
    # Método de classe usa cls e pode alterar dados da classe.    
    @classmethod
    def mudar_numero_rodas(cls, novas_rodas):
        cls.rodas = novas_rodas
        print(f"Agora todos os carros tem {cls.rodas} rodas.")
    
    # Método estático não acessa o objeto nem a classe, apenas executa uma função relacionada ao contexto da classe.    
    @staticmethod
    def calcular_idade(ano_fabricacao, ano_atual):
        return ano_atual - ano_fabricacao                
    
    