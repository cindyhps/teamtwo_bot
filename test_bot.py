import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import serial
import time

# Inisialisasi bot Telegram
API_TOKEN = '6803335035:AAEsIx4P874EfbjP0OP0w9XpUVPB_0tOuoo'  # Ganti dengan token API bot Anda
bot = telepot.Bot(API_TOKEN)
CHAT_ID = "-1002065410971"
lampu = 1

ser = serial.Serial("", 9600)
ser.flush()

# Fungsi untuk menangani pesan yang diterima
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # Jika pesan berupa teks
    if content_type == 'text':
        # Mendapatkan teks pesan
        text = msg['text']
        
        # Memeriksa jika pesan adalah '/start'
        if text == '/start-tim-2':
            response = "Silahkan pilih kode dibawah";
            bot.sendMessage(chat_id, 'Halo! Selamat datang di bot ini.')
        	# Membuat inline keyboard
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Hidupkan Lampu', callback_data='option_1')],
                [InlineKeyboardButton(text='Cek Jarak', callback_data='option_2')],
            ])
            
            # Mengirim pesan bersama dengan inline keyboard
            bot.sendMessage(chat_id, response, reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    # Respon terhadap callback
    bot.answerCallbackQuery(query_id, text='Anda memilih: ' + query_data)

    # Menangani pemilihan pengguna berdasarkan query_data
    if query_data == 'option_1':
        bot.sendMessage(CHAT_ID, 'Anda memilih: Hidupkan Lampu')
        if lampu == 1:
            ser.write(b"1")
            lampu = 0
        else:
            ser.write(b"0")
            lampu = 1
    elif query_data == 'option_2':
        bot.sendMessage(CHAT_ID, 'Anda memilih: Cek Jarak')
        ser.write(b"jarak")

# Memulai loop untuk menangani pesan
MessageLoop(bot, {'chat': handle_message, 'callback_query': on_callback_query}).run_as_thread()

print('Bot sedang berjalan...')

# Biarkan program berjalan terus menerus
try:
    while True:
        if ser.in_waiting > 0:
                data = ser.readline()
                print(data.decode('utf-8'))
                time.sleep(1)
except KeyboardInterrupt:
	ser.close()
finally:
	ser.close()
