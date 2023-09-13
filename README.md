# ezMoMacro
This is a simple and configurable script that can be used to macro various actions in Mortal Online 2.

# Features
  - Fully configurable
  - Easy toggle on/off hotkey
  - Does not require keeping MO2 focused

## Requirements
  - Install [Python 3](https://www.python.org/downloads/windows/)
  - Clone or download & extract files from this repository somewhere on your computer
  - Install dependencies by running `install-requirements.bat` or `pip install -r requirements.txt` in the `ezMoMacro` folder

## Usage
 - Edit the configurable paramaters like keybinds and timings at the top of `ezMoMacro.py` to suit your needs for whatever you're macroing
 - Run `ezMoMacro.py`, on Windows you should be able to just double-click it. Otherwise in a command prompt run: `python3 ezMoMacro.py`

## Parameters
`toggle_key` - key to use for toggling the macro on/off
`action_key` - key to use for macro action, generally will be E for self-casting, Q for target-casting and LMB for swinging
`action_duration` - how long to wait between triggering each action (should be roughly the time it takes to perform the action ingame)
`cycle_length` - amount of times to repeat action each cycle
`rest_key` - key to use for resting, this should be whatever hotkey you bind rest to ingame
`rest_interval` - amount of seconds to rest for between each action cycle, set to 0 to disable resting