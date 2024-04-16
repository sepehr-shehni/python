import requests

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("پیام با موفقیت ارسال شد!")
    else:
        print("مشکلی در ارسال پیام به وجود آمد. کد خطا:", response.status_code)

# ورودی های مورد نیاز
token =  "6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I"
chat_id = "87085659"

# متن پیام
message_text = "سلام! این یک پیام تست است."

# ارسال پیام
send_message(token, chat_id, message_text)