global enabled
enabled = False

global running
running = False

global selected
selected = 0

global version
version = 'v1.1.0'

global url
url = 'https://github.com/wyqydsyq/ezMoMacro'

global macros
macros = []

global macroList
macroList = []

import asyncio

global loop
loop = asyncio.new_event_loop()

global mainTask
mainTask = loop.create_task(asyncio.sleep(0))