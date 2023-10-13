import requests
from bs4 import BeautifulSoup
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Global değişkenler
url = 'https://www.bershka.com/tr/suni-y%C3%BCnl%C3%BC-astarl%C4%B1-uzun-denim-parka-c0p137423160.html?colorId=427'  # Bershka web sitesinin URL'sini buraya ekleyin
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
previous_price = '2.699 TL'
TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''


import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

async def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message , parse_mode= 'Markdown' )

async def get_product_info():
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
                #message = f'Ürünün Fiyatı Düştü Kaçırma!\n\nÜrün Adı: {product_name}\n💰Ürün Fiyatı: {current_price}\nÜrün Eski Fiyatı: {previous_price}\n🔗Ürün Linki: {url}'
                message = f'🚨*Ürünün Fiyatı Düştü Kaçırma!*\n🎉*İndirimli Fiyat: {current_price}*\n\n*Ürün Adı:* {product_name}\n*Eski Fiyat:* {previous_price}\n*Ürün Linki:* {url}'
                await send_telegram_message(message)

            previous_price = current_price
        else:
            print('Ürün fiyatı etiketi bulunamadı.')
    else:
        print(f'Hata: {response.status_code}')

async def main():
    while True:
        # Ürün bilgilerini al
        await get_product_info()

        # Her 10 saniyede bir bekleyin
        await asyncio.sleep(10)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
