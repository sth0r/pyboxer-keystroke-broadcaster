# pyboxer - keystroke broadcaster
python script for broadcasting keystroks to a background window

This script is a bit hacked togehter but it works for what iam doing with it.

how to launch the script:
python pyboxer.py <window name>
example:
python pyboxer.py "calculator"
Then you need to bring the window in focus within 5 sec of launching the script and keep it in focus till 5 sec after you launched the script, now key strocks defined in scanToVirtualKey() will be broadcast to the window even when it is in the background.

this script need you to have installed or in the folder the script.

pywin32 (https://github.com/mhammond/pywin32/releases) (installed)

keyboard (https://github.com/boppreh/keyboard) (in the folder with the script)
