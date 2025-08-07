class Operacoes:
    
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
            raise ValueError("Divisão por zero não é permitida.")


