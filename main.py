import requests
from bs4 import BeautifulSoup
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Global değişkenler
url = 'https://www.bershka.com/tr/suni-y%C3%BCnl%C3%BC-astarl%C4%B1-uzun-denim-parka-c0p137423160.html?colorId=427'  # Bershka web sitesinin URL'sini buraya ekleyin
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
previous_price = None
TELEGRAM_TOKEN = 'TELEGRAM API'
TELEGRAM_CHAT_ID = 'CHAT ID'


def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)


def get_product_info():
    global previous_price

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ürün adını içeren etiketi bulma
        product_name_tag = soup.find('h1', {'data-qa-anchor': 'productDetailName', 'class': 'product-title'})

        if product_name_tag:
            product_name = product_name_tag.text.strip()
            print(f'Ürün Adı: {product_name}')
        else:
            print('Ürün adı etiketi bulunamadı.')

        # Ürün fiyatını içeren etiketi bulma
        product_price_tag = soup.find('span', {'data-qa-anchor': 'productItemPrice', 'class': 'current-price-elem'})

        if product_price_tag:
            current_price = product_price_tag.text.strip()
            print(f'Ürün Fiyatı: {current_price}')

            # Fiyat güncellendiyse eski ve yeni fiyatı karşılaştır
            if previous_price is not None and previous_price != current_price:
                print(f'Eski Fiyat: {previous_price}')
                print('Ürün Fiyatı Değişti!')

                # Telegram mesajı gönder
                message = f'Ürün Adı: {product_name}\nÜrün Fiyatı: {current_price}\nÜrün Linki: {url}'
                send_telegram_message(message)

            previous_price = current_price
        else:
            print('Ürün fiyatı etiketi bulunamadı.')
    else:
        print(f'Hata: {response.status_code}')


def main():
    while True:
        # Ürün bilgilerini al
        get_product_info()

        # Her 60 saniyede bir bekleyin
        time.sleep(60)

if __name__ == "__main__":
    main()