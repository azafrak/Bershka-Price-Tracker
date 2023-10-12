# Bershka Fiyat Takib Telegram Botu
Python ile yazılmış bu proje, bershka ürünlerinde ki fiyatı takip eder, fiyatı değiştiğinde ise Telegram üzerinden mesaj gönderir.

url = yazan yere, ürünün linki eklenecek.

TELEGRAM API = yazan yere telegram botunuzun API TOKEN 'ını yazılacak
CHAT ID = yazan yere telegramda ki kullanıcı CHAT ID'i yazılacak.

previous_price = '3000' -> yazan yere ürünün mevcut fiyat bilgisi yazılacak. Bu sayede ürünün şuan ki fiyatı düştüğünde burada yazılan fiyat ile karşılaştırılacak. Eğer, ürünün fiyat buraya yazılan fiyatın altına inerse telegram üzerinden mesaj gönderilecek.

Her 10 saniyede bir denetlemesi içinde kural eklendi.
await asyncio.sleep(10) burada ki 10 değerini istediğiniz süreyle değiştirebilirsiniz.

# Bershka Price Tracker Telegram Bot
This project, written in Python, tracks the prices of Bershka products and sends a message via Telegram when the price changes.

The link of the product will be added to the place where url = is written.

The API TOKEN of your telegram bot will be written where TELEGRAM API = is written.
The CHAT ID of the user in Telegram will be written where CHAT ID = is written.

previous_price = '3000' -> The current price information of the product will be written where it says. In this way, when the current price of the product drops, it will be compared with the price written here. If the price of the product falls below the price written here, a message will be sent via Telegram.

A rule has been added to check every 10 seconds.
await asyncio.sleep(10) You can change the value 10 here to any time you want.
