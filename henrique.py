resposta = input("quer jogar: ")

if resposta == "sim":
   resposta = input("quer continuar jogando?")

   if resposta == "sim":
     print("resposta certa")
   else:
      print("resposta erada")
elif resposta == "nao":
   print("voce nunca mais vai jogar")