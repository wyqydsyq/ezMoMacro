# ezMoMacro
This is a simple and configurable macro runner written in Python3 that can be used to macro various actions in Mortal Online 2.

![ezMoMacro](https://i.imgur.com/wsQNyst.png)

# Features
  - Fully configurable
  - Easy toggle on/off hotkey
  - Does not require keeping MO2 focused

## Requirements
  - Install [Python 3](https://www.python.org/downloads/windows/)
  - Clone or download & extract files from this repository somewhere on your computer
  - Install dependencies by running `install-requirements.bat` or `pip3 install -r requirements.txt` in the `ezMoMacro` folder

## Usage
 - Run `ezMoMacro.py`, on Windows you should be able to just double-click it. Otherwise in a command prompt run: `python3 ezMoMacro.py`.
 - Select the macro you want to run, press the toggle hotkey to enable/disable it.

## Customization
 - Edit any paramaters defined at the top of a macro file to suit your needs
    
    e.g. if you want to use autocast for levelling magic skills, set the keys to match your keybindings and `action_duration` to match the duration it takes to cast the spell (most spells take ~25% longer to complete cast animation than their "cast time" listed ingame) you're currently using.
 - You can make changes to a macro and reload it with `ctrl+r`

## Macros
### Autowalk
Useful for levelling armor training, combat maneuvering, and footspeed skills.

### Autoattack
Useful for pickaxe sieging, levelling strength, dexterity, melee combat, aggressive stance and endurance skills. Stand in front of a training dummy or a friend you want to stat up before starting. If using it to stat up on a friend make sure you enable "thrust as default attack" in the game settings before starting.

### Autocast
Useful for levelling intelligence, psyche, resting and basically all mage skills.

You can configure the hotkeys used for chanelling a spell, self-casting it and resting by changing the variables at the top of the script. By default it will press "E" to self-cast, "0" to rest.

#### Parameters
  - `action_key` - key to use for macro action, generally will be E for self-casting, Q for target-casting and LMB for swinging
  - `action_duration` - how long to wait between triggering each action (should be roughly the time it takes to perform the action ingame)
  - `cycle_length` - amount of times to repeat action each cycle
  - `rest_key` - key to use for resting, this should be whatever hotkey you bind rest to ingame
  - `rest_duration` - amount of seconds to rest for between each action cycle, set to 0 to disable resting

## Writing macros
Macros are just simple python scripts of the pattern:
```py
instructions = 'Instructions on how to use the macro'
async def macro(app):
```

`app` is an instance of a [pywinauto window](https://pywinauto.readthedocs.io/en/latest/code/pywinauto.controls.hwndwrapper.html) connected to the game window, you can use methods like `press_mouse_input()` and `send_keystrokes()` to send input commands to the game window.

`instructions` is an optional string you can specify that will be displayed on the right hand pane of ezMoMacro when the macro is selected.

Use `asyncio.sleep()` instead of `time.sleep()` for places where your macro should be interruptable (via toggle key). Generally this means always use `asyncio.sleep()` except for cases where you are manually simulating keydown/keyup, for those you will want to use `time.sleep()` so the macro doesn't get interrupted before they key is released (otherwise the key will be stuck held ingame until it's manually pressed again)

You can use any other Python libraries you like to expand functionality of your macros e.g. you can use `app.capture_as_image()` to take a screenshot of the game window and pass that into [ImageAI](https://github.com/OlafenwaMoses/ImageAI#-image-classification) to do things like detecting objects and then base your macro behaviour on what was detected.
