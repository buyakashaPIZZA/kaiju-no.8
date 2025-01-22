import os
from dhooks import Webhook, Embed, File

image2_path = 'kaiju.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        color=0xF0B232
    )
    
    embed.set_image(url="attachment://kaiju.png")
    file = File(image2_path, name="kaiju.png")
    hook.send("@everyone 📢 Kaiju", embed=embed, file=file)
