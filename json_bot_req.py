import requests
import time

# Fungsi untuk mengirim permintaan ke API Bot Telegram
def send_telegram_request(method, data):
    token = "6803335035:AAEsIx4P874EfbjP0OP0w9XpUVPB_0tOuoo"
    url = f"https://api.telegram.org/bot{token}/{method}"
    response = requests.post(url, json=data)
    return response.json()

# Fungsi untuk memproses pesan
def process_message(message):
    chat_id = message["chat"]["id"]
    message_id = message["message_id"]
    text = message.get("text", "No text")
    print(f"Chat ID: {chat_id}\nMessage ID: {message_id}\nText: {text}")
    # Anda bisa menambahkan logika lain di sini sesuai kebutuhan aplikasi Anda

def main():
    # Token bot Telegram Anda
    offset = 0
    while True:
        try:
            response = send_telegram_request("getUpdates", {"offset": offset, "timeout": 30})
            if response["ok"]:
                for result in response["result"]:
                    process_message(result["message"])
                    offset = result["update_id"] + 1
            else:
                print("Failed to get updates:", response)
        except Exception as e:
            print("An error occurred:", e)
        time.sleep(1)

if __name__ == "__main__":
    main()
