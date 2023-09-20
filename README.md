# ezMoMacro
This is a simple and configurable script that can be used to macro various actions in Mortal Online 2.

# Features
  - Fully configurable
  - Easy toggle on/off hotkey
  - Does not require keeping MO2 focused

## Requirements
  - Install [Python 3](https://www.python.org/downloads/windows/)
  - Clone or download & extract files from this repository somewhere on your computer
  - Install dependencies by running `install-requirements.bat` or `pip3 install -r requirements.txt` in the `ezMoMacro` folder

## Usage
 - Edit any paramaters at the top of the macro you want to suit your needs e.g. if you want to use autocast for levelling magic skills, set the keys to match your keybindings and `action_duration` to match the duration it takes to cast the spell (most spells take ~25% longer to complete cast animation than their "cast time" listed ingame).
 - Run `ezMoMacro.py`, on Windows you should be able to just double-click it. Otherwise in a command prompt run: `python3 ezMoMacro.py`.
 - Select the macro you want to run, press the toggle hotkey to enable/disable it.

## Macros
### Autowalk
Useful for levelling armor training, combat maneuvering, and footspeed skills.

### Autoattack
Useful for pickaxe sieging, levelling strength, dexterity, melee combat, aggressive stance and endurance skills. Stand in front of a training dummy or a friend you want to stat up before starting. If using it to stat up on a friend make sure you enable "thrust as default attack" in the game settings before starting.

### Autocast
Useful for levelling intelligence, psyche, resting and basically all mage skills.

You can configure the hotkeys used for chanelling a spell, self-casting it and resting by changing the variables at the top of the script. By default it will press "9" to channel spell, "E" to self-cast, "0" to rest.

#### Parameters
  - `action_key` - key to use for macro action, generally will be E for self-casting, Q for target-casting and LMB for swinging
  - `action_duration` - how long to wait between triggering each action (should be roughly the time it takes to perform the action ingame)
  - `cycle_length` - amount of times to repeat action each cycle
  - `rest_key` - key to use for resting, this should be whatever hotkey you bind rest to ingame
  - `rest_duration` - amount of seconds to rest for between each action cycle, set to 0 to disable resting