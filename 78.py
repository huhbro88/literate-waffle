import asyncio
import random
from telegram import Bot

TOKEN = "8892876567:AAHtcxqEoIeWA2GiaVjdpltwz5whwkjycUc"
CHAT_ID = -1002309817095
MESSAGE_ID = 79

texts = [
    "78",
    "7 8",
    "семьдесят восемь",
    "7емьде,sятт 8осемь",
    "777ixty 888ight",
    "39+39",
    "78 78 78 78 78 78 78",
    "7878787878787878",
    "с м ь   т        в  е ь"
]

bot = Bot(token=TOKEN)

async def main():
    last_text = None

    while True:
        try:
            text = random.choice(texts)

            # чтобы не повторялся подряд один и тот же текст
            while text == last_text:
                text = random.choice(texts)

            await bot.edit_message_text(
                chat_id=CHAT_ID,
                message_id=MESSAGE_ID,
                text=text
            )

            last_text = text

        except Exception as e:
            print(e)

        await asyncio.sleep(3)

asyncio.run(main())