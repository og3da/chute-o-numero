from random import randint
print("--- CHUTE O NÚMERO ---")
numero=randint(1,1000)
def jogo():
    stop=1
    while stop==1:
        try:
            chute=int(input("Chute o número gerado: "))
            if (numero>chute):
                    print("Numero maior")
            elif (numero<chute):
                    print("Numero menor")
            elif chute==numero:
                    print("Parabéns você acertou!!!")
                    stop=2
        except ValueError:
            print("Digite um número!!!")
jogo()