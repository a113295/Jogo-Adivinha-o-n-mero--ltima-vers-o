import random


def jogo_adivinha():
  print("=== JOGO: ADIVINHA O NÚMERO ===")
  print("Escolhe a modalidade:")
  print("1 - O computador pensa num número e tu adivinhas")
  print("2 - Tu pensas num número e o computador adivinha")

  opcao = input("Introduz a modalidade (1 ou 2): ")


  if opcao == "1":
    numero_secreto = random.randint(0, 100)
    tentativas = 0

    print("\nO computador já pensou num número entre 0 e 100. Tenta adivinhar!")

    while True:
      tentativa_utilizador = int(input("Qual é o teu palpite? "))
      tentativas += 1

      if tentativa_utilizador == numero_secreto:
        print(f"Acertou! Descobriste o número em {tentativas} tentativas.")
        break
      elif tentativa_utilizador < numero_secreto:
        print("O número que pensei é Maior")
      else:
        print("O número que pensei é Menor")


  elif opcao == "2":
    print(
        "\nPensa num número entre 0 e 100. O computador vai tentar adivinhá-lo."
    )
    input("Pressiona [Enter] quando já estiveres a pensar no número...")

    minimo = 0
    maximo = 100
    tentativas = 0

    while True:
     
      palpite_computador = (minimo + maximo) // 2
      tentativas += 1

      print(f"\nO computador acha que o número é: {palpite_computador}")
      resposta = input(
          "Como respondes? ('Acertou', 'Maior' ou 'Menor'): "
      ).strip()

      if resposta.lower() == "acertou":
        print(f"O computador acertou em {tentativas} tentativas!")
        break
      elif resposta.lower() == "maior":
       
        minimo = palpite_computador + 1
      elif resposta.lower() == "menor":
        
        maximo = palpite_computador - 1
      else:
        print("Resposta inválida. Usa apenas 'Acertou', 'Maior' ou 'Menor'.")
        tentativas -= 1  

  else:
    print("Opção inválida! Reinicia o programa e escolhe 1 ou 2.")



if __name__ == "__main__":
  jogo_adivinha()
