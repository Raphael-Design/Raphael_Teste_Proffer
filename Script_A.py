#Script that integrates that runs Script_B, catches it's error and research it using Script_C.
#Script que integra e roda o Script_B, captura seu erro e pesquisa-o utilizando o Script_c.
from Script_C import solve_error

#Ler Script B -> Caso tenha erro -> Pesquisar erro utilizando Script C e retornar 2 prints da pesquisa.
with open("Script_B.py") as script:
    try:
        exec(script.read())
    except Exception as error:
        print("Erro encontrado:")
        print("    " + error.__class__.__name__)
        print("    " + str(error))
        print("Procurando solução. .. .")
        solve_error(error.__class__.__name__ + " " + str(error))
        