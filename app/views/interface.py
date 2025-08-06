def mostrar_menu():
    print("\n🔢 Calculadora Python")
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def obter_valores():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b

def mostrar_resultado(resultado):
    print(f"✅ Resultado: {resultado}")

def mostrar_erro(msg):
    print(f"❌ Erro: {msg}")