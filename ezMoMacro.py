import glob
import importlib
from os.path import dirname, basename, isfile, join
import asyncio
import os

import keyboard
import pywintypes
import pywinauto
from blessed import Terminal

from parameters import toggle_key, reload_key, quit_key
import globals


tasks = []


def toggle():
    globals.enabled = not globals.enabled
    if not globals.enabled:
        globals.running = False
        for task in tasks:
            task.cancel()


def next():
    if globals.selected == len(globals.macroList) - 1:
        globals.selected = 0
    else:
        globals.selected += 1


def prev():
    if globals.selected == 0:
        globals.selected = len(globals.macroList) - 1
    else:
        globals.selected -= 1


def loadMacros():
    moduleList = glob.glob(join(dirname(__file__), "macros/*.py"))
    macroList = [basename(f)[:-3] for f in moduleList if isfile(f)
                 and not f.endswith('__init__.py')]
    globals.macros = list(
        map(lambda m: importlib.import_module('macros.' + m), macroList))

    return macroList


def reload(t):
    globals.running = False
    for task in tasks:
        task.cancel()

    print(t.home + t.white_on_black + t.clear)
    globals.macroList = loadMacros()


async def run(app):
    if not globals.running:
        globals.running = True
        await globals.macros[globals.selected].macro(app)
        globals.running = False


async def main(app, t):
    with t.cbreak(), t.fullscreen(), t.hidden_cursor():
        print(t.home + t.white_on_black + t.clear)

        while True:
            with t.location(0, 0):
                print(t.black_on_white(
                    t.center("ezMoMacro " + globals.version)), end='', flush=True)

            for i, macro in enumerate(globals.macroList):
                if i is globals.selected:
                    with t.location(2, 2 + i):
                        print(t.black_on_white(macro))
                else:
                    with t.location(2, 2 + i):
                        print(t.white_on_black(macro))

            with t.location(0, t.height - 1):
                statusStr = (' Disabled ', ' Enabled ')[globals.enabled]
                if (globals.enabled):
                    status = t.white_on_green(statusStr)
                else:
                    status = t.white_on_red(statusStr)

                currentMacro = ' ' + globals.macroList[globals.selected] + ' '

                print(t.white_on_gray6(
                    status + t.black_on_white(currentMacro) + t.center(
                        'QUIT=' + quit_key + ' ' +
                        'RELOAD=' + reload_key + ' ' +
                        'TOGGLE=' + toggle_key + ' ' +
                        'SELECT=up/down',
                        width=t.width - len(statusStr) - len(currentMacro)
                    )),
                    end='', flush=True)

            if globals.enabled:
                task = asyncio.create_task(run(app))
                tasks.append(task)
                try:
                    await task
                except asyncio.CancelledError:
                    continue
            else:
                await asyncio.sleep(0.1)

t = Terminal()
keyboard.add_hotkey(toggle_key, lambda: toggle())
keyboard.add_hotkey(quit_key, lambda: os._exit(0))
keyboard.add_hotkey(reload_key, lambda: reload(t))
keyboard.add_hotkey('up', lambda: prev())
keyboard.add_hotkey('down', lambda: next())

app = pywinauto.Desktop(backend="win32").MortalOnline2
globals.macroList = loadMacros()
asyncio.run(main(app, t))
