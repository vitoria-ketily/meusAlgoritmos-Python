nascenca=int(input("Digite o ano que nasceu:"))
atual=int(input("Digite o ano atual:"))
if(atual-nascenca)<=16:
    print("Você não pode votar.")
else:
        print("Você pode votar.")
        print("Você poderá votar daqui a:"), 16-(atual-nascenca),"anos"