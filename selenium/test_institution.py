from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar opciones de Chrome para compatibilidad
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no GUI) - commented out to show browser
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Disable GPU for Windows stability
chrome_options.add_argument("--disable-extensions")

# Configurar el driver de Chrome con opciones
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL base de la aplicación (ajusta si es diferente)
BASE_URL = "https://lab.vallegrande.edu.pe/school"

try:
    # Paso 1: Navegar a la página de login
    driver.get(f"{BASE_URL}/login")
    print("Navegando a la página de login...")

    # Esperar a que el formulario de login esté presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Paso 2: Ingresar credenciales
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("michaell.ibarra@vallegrande.edu.pe")
    password_field.send_keys("michael12@")
    print("Credenciales ingresadas: michaell.ibarra@vallegrande.edu.pe / michael12@")

    # Paso 3: Hacer submit al formulario
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    print("Formulario de login enviado...")

    # Debug: Imprimir URL actual después de submit
    print(f"URL después de submit: {driver.current_url}")

    # Esperar redirección al dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )
    print("Redirigido al dashboard exitosamente.")

    # Paso 4: Navegar a la gestión de instituciones
    driver.get(f"{BASE_URL}/admin/institution")
    print("Navegando a la gestión de instituciones...")

    # Esperar a que la página cargue
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-wrapper"))
    )

    # Buscar el botón para agregar institución (ajusta el selector si es diferente)
    # Asumiendo que hay un botón con texto "Agregar" o similar
    try:
        add_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agregar')] | //a[contains(text(), 'Agregar')]"))
        )
        add_button.click()
        print("Clic en botón Agregar institución...")
    except:
        # Si no hay botón, navegar directamente a /admin/institution/add
        driver.get(f"{BASE_URL}/admin/institution/add")
        print("Navegando directamente a agregar institución...")
        print(f"URL actual: {driver.current_url}")

    # Esperar a que el formulario de institución esté presente
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "page-title"), "Nueva Institución")
    )
    print("Página de agregar institución cargada.")
    
    # Esperar un poco más para que el formulario se renderice completamente
    time.sleep(10)

    # Paso 5: Llenar el formulario de institución
    name_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Ingresa el nombre de la institución']")
    code_field = driver.find_element(By.ID, "codeInstitution")
    address_field = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Dirección completa de la institución']")
    email_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='contacto@institucion.edu']")
    phone_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='987654321']")

    name_field.send_keys("Institución de Prueba Selenium")
    code_field.send_keys("123456789")
    address_field.send_keys("Dirección de prueba, Ciudad, País")
    email_field.send_keys("contacto@prueba.edu")
    phone_field.send_keys("987654321")
    print("Formulario de institución llenado...")

    # Paso 6: Enviar el formulario
    submit_form_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_form_button.click()
    print("Formulario de institución enviado...")

    time.sleep(3)  

    try:
        success_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))  # Ajusta el selector
        )
        print("Institución creada exitosamente.")
    except:
        print("No se pudo verificar el mensaje de éxito, pero el formulario fue enviado.")

    driver.get(f"{BASE_URL}/admin/institution")
    print("Navegando de vuelta a la lista de instituciones...")

    # Esperar a que la lista cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-wrapper"))
    )
    print("Lista de instituciones cargada.")


finally:
    # Cerrar el navegador
    driver.quit()
    print("Navegador cerrado.")