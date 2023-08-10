import aritmetica
import trigonometria

class CalculadoraCientifica:
    def __init__(self) -> None:
        self.operacoes_basicas = aritmetica.OperacoesBasicas()
        self.operacoes_trigonometricas = trigonometria.OperacoesTrigonometricas()

    def mostrar_menu(self) -> None:
        print('--- Mini Calculadora ---')
        print("Menu de Opções:")
        print('1 - Operações básicas')
        print('2 - Operacoes trigonométricas')
        print('S - SAIR')

    def executar(self) -> None: 
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.operacoes_basicas.executar()
            elif opcao.lower() == 's':
                break
            else:
                print("Opção inválida")
            
            continuar = input("Deseja continuar? (S/N): ")
            if continuar.lower() != 's':
                break

calculadora = CalculadoraCientifica()
calculadora.executar()