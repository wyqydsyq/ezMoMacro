wait_duration = 0.2 # how long to wait between attacks, setting this too short will cause the game to ignore input
charge_duration = 0.01 # how long to charge attacks for

import asyncio
import time

async def macro(app):
    await asyncio.sleep(0.2)
    app.press_mouse_input(button='left')
    time.sleep(0.1) # use non-async time for this as we don't want to potentially cancel before mouseup
    app.release_mouse_input(button='left')
