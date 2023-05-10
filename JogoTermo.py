import random

def cabecalho(titulo, titulo2, a="-"):
    print(a * 60)
    print(titulo)
    print(titulo2)
    print(a * 60)


lista = [
    "negro", "termo", "nobre", "algoz", "afeto", "plena", "pesar", "dengo",
    "digno", "sutil", "vigor", "fazer", "inato", "genro", "coser", "ardil",
    "corja", "prole", "poder", "moral", "torpe", "honra", "muito", "justo",
    "gozar", "anexo", "etnia", "sobre", "tange", "lapso", "expor", "haver",
    "amigo", "tempo", "dizer", "tenaz", "vitor"
]

def main():
  cabecalho("BEM VINDO AO TERMO!", "\nPara iniciar, digite uma palavra de cinco letras!")
  palavra_certa = random.choice(lista)
  for n in range(1, 7):
    print("\n(", n, "/6)", sep="", end="  ")
    teste = input("Digite uma palavra: ").lower()

    if palavra_certa == teste:
        print(teste)
        break
    else:
        print(teste)
        for i in range(5):
            if palavra_certa[i] == teste[i]:
                print("+", end="")
            elif teste[i] in list(palavra_certa):
                print("-", end="")
            else:
                print(" ", end="")
  if palavra_certa != teste:
    print("\nPerdeu! A palavra correta era:", palavra_certa)
  else:
    print("Acertou!!")
  
  
