#Script to research the error, retrieve the results found on StackOverflow, and the first answer from the first result.
#Script para pesquisar o erro e retornar os resultados encontrados no StackOverflow e a primeira resposta do primeiro resultado.
from playwright.sync_api import sync_playwright
import time

#Função que vai ser integrada ao Script_A que retorna 2 imagens mostrando os resultados de pesquisa
#e a solução do primeiro resultado.
def solve_error(error):
    #Configurações de página e inicialização
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://stackoverflow.com/search?q=" + error.replace(" ", "+") + "+Python")
    if page.locator(".flex--item6").first.is_visible():
            page.locator(".flex--item6").first.click()
    if page.get_by_text("captcha").is_visible():
        input("A pagina necessita de verificação captcha, complete-a e pressione enter para continuar:")
    time.sleep(2)

    #Pegar uma lista de todos os resultados da pesquisa do erro.
    page.screenshot(path="Resultados.png", full_page=True)
    page.locator("a[href*='SearchResults']").first.click()
    time.sleep(5)

    #Pegar a primeira resposta do primeiro resultado da pesquisa.
    page.locator(".answercell").first.screenshot(path= "Solução_Erro.png")
    page.close()