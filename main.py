from view.tela_login import TelaLogin
from view.tela_menu import TelaMenu
from view.tela_canal import TelaCanal
from view.tela_quadro import TelaQuadro
from view.tela_video import TelaVideo

login = TelaLogin()

if login.login():
    menu = TelaMenu()

    while True:
        opcao = menu.mostrar_menu()

        if opcao == "1":
            TelaCanal().abrir()
        elif opcao == "2":
            TelaQuadro().abrir()
        elif opcao == "3":
            TelaVideo().abrir()
        elif opcao == "0":
            login.logout()
            break
        else:
            print("Opção inválida.")