from app.models.Operacoes import Operacoes
from app.views.interface import obter_valores, mostrar_resultado, mostrar_erro, mostrar_historico

class CalculadoraController:

    def __init__(self):
        self.historico = []  # Lista para armazenar operações

    def executar_operacao(self, escolha):
        if escolha == "5":
            mostrar_historico(self.historico)
            return

        try:
            a, b = obter_valores()
            if escolha == "1":
                resultado = Operacoes.somar(a, b)
                tipo = "soma"
            elif escolha == "2":
                resultado = Operacoes.subtrair(a, b)
                tipo = "subtração"
            elif escolha == "3":
                resultado = Operacoes.multiplicar(a, b)
                tipo = "multiplicação"
            elif escolha == "4":
                resultado = Operacoes.dividir(a, b)
                tipo = "divisão"
            else:
                mostrar_erro("Operação inválida.")
                return
            
            # Criando dicionário com os dados da operação
            operacao = {
                "tipo": tipo,
                "a": a,
                "b": b,
                "resultado": resultado
            }

            # Adicionando à lista de histórico
            self.historico.append(operacao)

            mostrar_resultado(resultado)

        except Exception as e:
            mostrar_erro(str(e))
