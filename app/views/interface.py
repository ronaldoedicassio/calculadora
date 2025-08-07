def mostrar_menu():
    print("\n🔢 Calculadora Python")
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Ver Histórico")
    print("0 - Sair")

def obter_valores():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

def mostrar_resultado(resultado):
    print(f"✅ Resultado: {resultado}")

def mostrar_erro(msg):
    print(f"❌ Erro: {msg}")

def mostrar_historico(historico):
    print("\n📜 Histórico de operações:")
    if not historico:
        print("Nenhuma operação realizada ainda.")
    else:
        for i, item in enumerate(historico):
            print(f"{i+1}. {item['tipo']} {item['a']} e {item['b']} = {item['resultado']}")