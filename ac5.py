"""
AC5 
João Lucas Ferraz Meirelles / 202402116495

"""
#Exercício

import random

def main():
    # Inicializa o aventureiro e o monstro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    # Imprime os atributos iniciais
    print(f"Aventureiro: Vida = {vida_aventureiro}, Ataque = {ataque_aventureiro}, Defesa = {defesa_aventureiro}")
    print(f"Monstro: Vida = {vida_monstro}, Ataque = {ataque_monstro}, Defesa = 0")

    # Executa o loop até que um dos dois tenha vida igual ou inferior a zero
    round_num = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        # Turno do aventureiro
        print(f"RODADA {round_num}:")
        dano = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano
        print(f"O aventureiro ataca o monstro, causando {dano} de dano!")
        print(f"O monstro agora tem {vida_monstro} de vida.")

        if vida_monstro <= 0:
            print(f"O monstro morreu! O aventureiro venceu!")
            break

        # Turno do monstro
        dano = random.randint(1, ataque_monstro) - defesa_aventureiro
        if dano > 0:
            vida_aventureiro -= dano
            print(f"O monstro ataca o aventureiro, causando {dano} de dano!")
            print(f"O aventureiro agora tem {vida_aventureiro} de vida.")

            if vida_aventureiro <= 0:
                print(f"O aventureiro morreu! O monstro venceu!")

        round_num += 1

# Chama a função main
if __name__ == "__main__":
    main()
