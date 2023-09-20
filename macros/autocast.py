action_key = 'e'  # key to use for macro action, generally will be E for self-casting, Q for target-casting and LMB for swinging
action_duration = 6.5  # how long to wait between triggering each action, should be roughly the time it takes to perform the action ingame. Add an extra .5 to the cast time of a spell
cycle_length = 10  # amount of times to repeat action each cycle
rest_key = '0'  # key to use for resting, this should be whatever hotkey you bind rest to ingame
rest_duration = 25 # amount of seconds to rest for between each action cycle, set to 0 to disable resting

instructions = 'Presses '+action_key+' every '+str(action_duration) +\
    's with a rest for '+str(rest_duration)+'s after every ' + \
    str(cycle_length)+' repetitions.'

import asyncio

async def macro(app):
    i = 1
    while i <= cycle_length:
        i += 1
        app.send_keystrokes(action_key)
        await asyncio.sleep(action_duration)

    if rest_duration > 0:
        await asyncio.sleep(0.5)  # wait to avoid blocking input
        app.send_keystrokes(rest_key)
        await asyncio.sleep(rest_duration)
