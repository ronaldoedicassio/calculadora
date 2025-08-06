from app.models.Operacoes import Operacoes
from app.views.interface import obter_valores, mostrar_resultado, mostrar_erro

class CalculadoraController:
    def executar_operacao(self, escolha):
        try:
            a, b = obter_valores()

            if escolha == "1":
                resultado = Operacoes.somar(a, b)
            elif escolha == "2":
                resultado = Operacoes.subtrair(a, b)
            elif escolha == "3":
                resultado = Operacoes.multiplicar(a, b)
            elif escolha == "4":
                resultado = Operacoes.dividir(a, b)
            else:
                mostrar_erro("Operação inválida.")
                return
            mostrar_resultado(resultado)
        except Exception as e:
            mostrar_erro(str(e))


