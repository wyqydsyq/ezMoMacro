walk_time = 3 # how long to walk in each direction

instructions = 'Holds W then S for '+str(walk_time)+'s each.'

import warnings
import time
import asyncio
warnings.filterwarnings("ignore")

async def macro(app):
    await asyncio.sleep(0.2)
    app.send_keystrokes('{w down}')
    time.sleep(walk_time)
    app.send_keystrokes('{w down}{w up}')
    await asyncio.sleep(0.2)
    app.send_keystrokes('{s down}')
    time.sleep(walk_time)
    app.send_keystrokes('{s down}{s up}')
