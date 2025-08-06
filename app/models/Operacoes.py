class Operacoes:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a - b
    
    @staticmethod
    def mul(a,b):
        return a * b
    
    @staticmethod
    def div(a,b):
        try:
            if(b != 0):
                return (a/b)
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
    