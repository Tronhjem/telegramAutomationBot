import asyncio
import os
import sys

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def send_message(text: str):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)
    print(f"Sent to {CHAT_ID}: {text}")


def main():
    if len(sys.argv) < 2:
        text = input("Message: ")
    else:
        text = " ".join(sys.argv[1:])
    asyncio.run(send_message(text))


if __name__ == "__main__":
    main()
