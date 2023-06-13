from django.test import TestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from galeria.forms import Perfilform
from galeria.selPath import SELENIUM_DIRS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class filma(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(SELENIUM_DIRS, options=chrome_options)

        driver.get("http://127.0.0.1:8000/")

        self.run_tests(driver)

    def tela_login(self,driver):
        sair_home = driver.find_element(By.ID, "login_btn")
        sair_home.click()
        time.sleep(2)

    def register(self, driver):
        #Saindo da home page


        register = driver.find_element(By.ID,"signUp")
        register.click()
        time.sleep(2)

        username_register = driver.find_element(By.NAME,"username")
        username_register.send_keys("teste")

        email_register = driver.find_element(By.NAME,"email")
        email_register.send_keys("mago@gmail.com")

        password_register = driver.find_element(By.NAME,"password1")
        password_register.send_keys("pcmagodefds")

        confirm_register = driver.find_element(By.NAME,"password2")
        confirm_register.send_keys("pcmagodefds")

        login = driver.find_element(By.ID,"Sign Up")
        login.click()

    def login(self, driver):
        wait = WebDriverWait(driver, 10)

        escrever_username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        escrever_username.send_keys("teste")

        password_login = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_login.send_keys("pcmagodefds")

        botao_login = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button")))
        botao_login.click()
        #time.sleep(2)

    def filtros(self, driver):
        wait = WebDriverWait(driver, 10)

        botao_filtro_1 = wait.until(EC.element_to_be_clickable((By.NAME, "top_views")))
        botao_filtro_1.click()
        time.sleep(2)

        btn_home = wait.until(EC.element_to_be_clickable((By.ID, "home_btn")))
        btn_home.click()
        time.sleep(2)

        botao_filtro_2 = wait.until(EC.element_to_be_clickable((By.NAME, "top_estrelas")))
        botao_filtro_2.click()
        time.sleep(2)

        btn_home = wait.until(EC.element_to_be_clickable((By.ID, "home_btn")))
        btn_home.click()
        time.sleep(2)

        botao_filtro_3 = wait.until(EC.element_to_be_clickable((By.NAME, "top_views")))
        botao_filtro_3.click()
        time.sleep(2)

        btn_home = wait.until(EC.element_to_be_clickable((By.ID, "home_btn")))
        btn_home.click()
        time.sleep(2)

    def busca_filme_existente(self, driver):
        busca = driver.find_element(By.CLASS_NAME,"busca__input")
        busca.send_keys("corra")
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")        
        btn_busca.click()
        #time.sleep(2)

        busca = driver.find_element(By.CLASS_NAME,"busca__input")
        busca.clear()
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")
        btn_busca.click()
        #time.sleep(2)

    def busca_filme_inexistente(self, driver):
        busca = driver.find_element(By.CLASS_NAME,"busca__input")
        busca.send_keys("Hari Poter")
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")
        btn_busca.click()
        #time.sleep(2)

        busca = driver.find_element(By.CLASS_NAME,"busca__input")
        busca.clear()
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")
        btn_busca.click()
        #time.sleep(2)

    def fav_home(self, driver):

        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        favoritar = wait.until(EC.visibility_of_element_located((By.ID, "fav_unfilled")))
        driver.execute_script("arguments[0].scrollIntoView();", favoritar)
        time.sleep(1)
        
        actions = ActionChains(driver)
        actions.move_to_element(favoritar).perform()
        time.sleep(1)
        
        favoritar.click()
        time.sleep(2)

        Desfavoritar = wait.until(EC.visibility_of_element_located((By.ID, "fav_filled")))
        driver.execute_script("arguments[0].scrollIntoView();", Desfavoritar)
        time.sleep(1)

        actions = ActionChains(driver)
        actions.move_to_element(Desfavoritar).perform()
        time.sleep(1)

        Desfavoritar.click()
        time.sleep(2)

    def detalhes_filmes(self, driver):
        first_movie = driver.find_element(By.CLASS_NAME, "card__imagem")
        first_movie.click()
        #time.sleep(2)
        
        favoritar = driver.find_element(By.NAME, "fav_img")
        favoritar.click()
        #time.sleep(2)

        desfavoritar = driver.find_element(By.NAME, "unfav_img")
        desfavoritar.click()
        #time.sleep(2)

        por_wl = driver.find_element(By.NAME, "wl")
        por_wl.click()
        #time.sleep(2)

        tirar_wl = driver.find_element(By.NAME, "un_wl")
        tirar_wl.click()

        #time.sleep(2)

    def avaliar(self, driver):
        star1 = driver.find_element(By.ID, "star1")
        star1.click()
        #time.sleep(2)

        star2 = driver.find_element(By.ID, "star2")
        star2.click()
        #time.sleep(2)

        star3 = driver.find_element(By.ID, "star3")
        star3.click()
        #time.sleep(2)

        star4 = driver.find_element(By.ID, "star4")
        star4.click()
        #time.sleep(2)

        star5 = driver.find_element(By.ID, "star5")
        star5.click()

        #time.sleep(2)

        btn_avaliar = driver.find_element(By.ID, "enviar-avaliacao")
        btn_avaliar.click()
        #time.sleep(2)
        
    def comentar(self, driver):
        wait = WebDriverWait(driver, 10)
        btn_comentar = wait.until(EC.visibility_of_element_located((By.ID, "comentar")))

        # Scroll into view of the element
        driver.execute_script("arguments[0].scrollIntoView();", btn_comentar)
        time.sleep(1)

        actions = ActionChains(driver)
        actions.move_to_element(btn_comentar).perform()
        time.sleep(1)

        btn_comentar.click()
        time.sleep(2)

        nome_comment = driver.find_element(By.NAME, "name")
        nome_comment.send_keys("teste")
        #time.sleep(2)

        txt_comment = driver.find_element(By.NAME, "body")
        txt_comment.send_keys("Filme muito ruim, eu nao gosto de nada!")
        #time.sleep(2)

        btn_comment = driver.find_element(By.ID, "btn_comentario")
        btn_comment.click()
        time.sleep(2)
    
    def apagar_comentario(self, driver):
        wait = WebDriverWait(driver, 10)
        btn_apagar = wait.until(EC.visibility_of_element_located((By.NAME, "Apagar_coment")))

        driver.execute_script("arguments[0].scrollIntoView();", btn_apagar)
        time.sleep(1)

        actions = ActionChains(driver)
        actions.move_to_element(btn_apagar).perform()
        time.sleep(1)

        btn_apagar.click()
        time.sleep(2)

    def verificar_lista(self, driver):
        #tem que esta vazia
        lista_vazia = driver.find_element(By.ID, "lista_btn")
        lista_vazia.click()

        #time.sleep(3)

    def adicionar_lista(self, driver):
        busca_filme1 = driver.find_element(By.CLASS_NAME,"busca__input")
        busca_filme1.send_keys("corra")
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")        
        btn_busca.click()

        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        favoritar = wait.until(EC.visibility_of_element_located((By.ID, "fav_unfilled")))
        driver.execute_script("arguments[0].scrollIntoView();", favoritar)
        time.sleep(1)
        
        actions = ActionChains(driver)
        actions.move_to_element(favoritar).perform()
        time.sleep(1)
        
        favoritar.click()
        time.sleep(2)

        

        busca_filme2 = driver.find_element(By.CLASS_NAME,"busca__input")
        busca_filme2.send_keys("truque de mestre")
        btn_busca = driver.find_element(By.CLASS_NAME,"busca__icone")        
        btn_busca.click()
        time.sleep(2)
        
        entrar_filme = driver.find_element(By.CLASS_NAME, "card__imagem")
        entrar_filme.click()
        time.sleep(2)

        por_na_wl = driver.find_element(By.NAME, "wl")
        por_na_wl.click()
        time.sleep(2)

    def lista(self, driver):
        #Corra em favorito e Truques de mestre na WatchList

        lista_cheia = driver.find_element(By.ID, "lista_btn")
        lista_cheia.click()

        time.sleep(3)

    def voltar_home(self, driver):
        voltar_home = driver.find_element(By.ID, "home_btn")
        voltar_home.click()

    def logout(self, driver):
        perfil = driver.find_element(By.ID, "perfil_btn")
        perfil.click
        time.sleep(2)
        logout= driver.find_element(By.ID,"log-out")
        logout.click()
        time.sleep(2)
    
    def sair(self, driver):
        driver.quit()

    def run_tests(self, driver):
        self.tela_login(driver)
        self.register(driver)
        self.login(driver)
        self.filtros(driver)
        self.busca_filme_existente(driver)
        self.busca_filme_inexistente(driver)
        self.fav_home(driver)
        self.detalhes_filmes(driver)
        self.avaliar(driver)
        self.comentar(driver)
        self.apagar_comentario(driver)
        self.verificar_lista(driver)
        self.adicionar_lista(driver)
        self.lista(driver)
        self.voltar_home(driver)
        #self.logout(driver)
        self.sair(driver)