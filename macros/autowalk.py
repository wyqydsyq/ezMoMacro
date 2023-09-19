import asyncio
import time
import warnings
warnings.filterwarnings("ignore")

async def macro(app):
    await asyncio.sleep(0.2)
    app.send_keystrokes('{w down}')
    time.sleep(3)
    app.send_keystrokes('{w down}{w up}')
    await asyncio.sleep(0.2)
    app.send_keystrokes('{s down}')
    time.sleep(3)
    app.send_keystrokes('{s down}{s up}')
