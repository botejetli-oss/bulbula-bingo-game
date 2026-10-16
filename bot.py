
import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    if not TOKEN:
        print("TELEGRAM_BOT_TOKEN hin kaa'amne.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    print("Botiin jalqabuuf qophaa'eera.")

    offset = None

    while True:
        try:
            response = requests.get(
                url,
                params={"timeout": 30, "offset": offset},
                timeout=35
            )
            response.raise_for_status()
            data = response.json()

            for update in data.get("result", []):
                offset = update["update_id"] + 1
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                text = message.get("text", "")

                if not chat_id:
                    continue

                if text == "/start":
                    reply = (
                        "Baga gara Bingo keenya dhuftan! 🎉\n\n"
                        "Taphni Bingo yeroo qophaa'u "
                        "asitti isin beeksifna."
                    )
                else:
                    reply = "Ergaa keessan fudhanne. /start barreessaa."

                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    json={"chat_id": chat_id, "text": reply},
                    timeout=15
                )

        except Exception as error:
            print("Dogoggora:", error)

if __name__ == "__main__":
    main()
