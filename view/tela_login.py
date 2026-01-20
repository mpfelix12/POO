class TelaLogin:
    def login(self):
        print("=== LOGIN ===")
        email = input("Email: ")
        senha = input("Senha: ")

        if email == "admin@email.com" and senha == "123":
            print("Login realizado com sucesso!")
            return True
        else:
            print("Login inválido!")
            return False

    def logout(self):
        print("Logout realizado.")