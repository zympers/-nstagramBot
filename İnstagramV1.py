import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def main():
    while True:
        # Proxy adresini kullanıcıdan al
        ip_port = input("Hoşgeldin Dostum Scripti Kullanmaya Başlamadan Önce Proxy Gir: ")
        print("Sağlam Bir Proxy Girdiğinden Emin Ol! Aksi Takdirde Çalışmayacaktır!")
        # Proxy ayarlarını yapılandır
        proxy = ip_port
        options = Options()
        options.add_argument(f'--proxy-server={proxy}')
        options.add_argument("--incognito")  # Gizli mod ekleniyor

        # Rastgele kullanıcı adı oluştur
        def generate_random_username(length=10):
            letters = string.ascii_lowercase + string.digits
            return ''.join(random.choice(letters) for i in range(length))

        # Rastgele şifre oluştur
        def generate_random_password(length=12):
            chars = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(chars) for i in range(length))

        # Bilgileri kaydet
        def save_credentials(email, username, password, index):
            with open("bilgiler.txt", "a") as file:
                file.write(f"{index}. Email: {email}\n")
                file.write(f"   Username: {username}\n")
                file.write(f"   Password: {password}\n")
                file.write("\n")

        # WebDriver'ı başlat (Proxy ve Gizli mod ayarları ile birlikte)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Tempail web sitesini aç
        driver.get("https://tempail.com/")

        # Biraz bekle ki sayfa yüklensin
        time.sleep(5)

        # Geçici e-postayı bul
        email_element = driver.find_element(By.CLASS_NAME, "adres-input")
        temp_email = email_element.get_attribute("value")
        print(f"Geçici e-posta: {temp_email}")

        # Instagram kayıt sayfasını aç
        driver.get("https://www.instagram.com/accounts/emailsignup/")

        # Biraz bekle ki sayfa yüklensin
        time.sleep(5)

        # Alınan geçici e-posta ve diğer bilgileri doldur
        email_input = driver.find_element(By.NAME, "emailOrPhone")
        email_input.send_keys(temp_email)

        full_name_input = driver.find_element(By.NAME, "fullName")
        full_name_input.send_keys("Test User")

        random_username = generate_random_username()
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(random_username)
        print(f"Kullanıcı adı: {random_username}")

        random_password = generate_random_password()
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(random_password)

        # Bilgileri kaydet
        save_credentials(temp_email, random_username, random_password, 1)  # 1. sıraya kaydedildi

        # Doğum yılı seç
        dob_dropdown = driver.find_element(By.CSS_SELECTOR, "._aau-._ap32")
        dob_dropdown.click()

        # 2003 yılını seç
        dob_year_2003 = driver.find_element(By.XPATH, "//option[@title='2003']")
        dob_year_2003.click()

        # Kayıt ol butonuna tıkla
        signup_button = driver.find_element(By.CSS_SELECTOR, "._acan._acap._acaq._acas._aj1-._ap30")
        signup_button.click()

        # Biraz bekle ki işlem tamamlansın
        time.sleep(5)

        # WebDriver'ı kapat
        driver.quit()

if __name__ == "__main__":
    main()
