import time
import keyboard
import pywinauto
from parameters import toggle_key, action_key, action_duration, rest_interval, cycle_length, rest_key

global enabled
enabled = False
version = 'v1.0.0'
url = 'https://github.com/wyqydsyq/ezMoMacro'


def run():
    global enabled
    app = pywinauto.Desktop(backend="win32").MortalOnline2
    while enabled:
        i = 0
        while i < cycle_length:
            if not enabled:
                break
            app.send_keystrokes(action_key)
            time.sleep(action_duration)
            i += 1

        if not enabled:
            break

        if rest_interval > 0:
            app.send_keystrokes(rest_key)
            time.sleep(rest_interval)


def toggle():
    global enabled
    enabled = not enabled
    print('Macro Status: ' + ("Disabled", "Enabled")[enabled])


print("ezMoMacro " + version + "\n" + url + "\n\n" +
      "Started, press " + toggle_key + " to toggle macro")
keyboard.add_hotkey(toggle_key, lambda: toggle())

while True:
    if enabled:
        run()
    else:
        keyboard.wait(toggle_key)
