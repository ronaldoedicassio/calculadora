from app.controllers.calculadora_controller import CalculadoraController
from app.views.interface import mostrar_menu

def main():
    controller = CalculadoraController()
    while True:
        mostrar_menu()
        escolha = input("Digite a opção: ")
        if escolha == "0":
            print("👋 Encerrando o sistema. Até mais!")
            break
        controller.executar_operacao(escolha)

if __name__ == "__main__":
    main()