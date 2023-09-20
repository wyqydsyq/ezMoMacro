wait_duration = 0.2 # how long to wait between attacks, setting this too short will cause the game to ignore input
charge_duration = 0.01 # how long to charge attacks for

instructions = 'Spams attacks every '+str(wait_duration)+'s with a '+str(charge_duration)+'s charge up.'

import asyncio
import time

async def macro(app):
    await asyncio.sleep(wait_duration)
    app.press_mouse_input(button='left')
    time.sleep(charge_duration) # use non-async time for this as we don't want to potentially cancel before mouseup
    app.release_mouse_input(button='left')
