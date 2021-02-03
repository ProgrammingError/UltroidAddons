"""
✘ Commands Available

• `{i}figlet <text>`
    Make a text a figlet.
"""

import pyfiglet
from . import *

CMD_SET = {
    "slant": "slant",
    "3D": "3-d",
    "5line": "5lineoblique",
    "alpha": "alphabet",
    "banner": "banner3-D",
    "doh": "doh",
    "iso": "isometric1",
    "letter": "letters",
    "allig": "alligator",
    "dotm": "dotmatrix",
    "bubble": "bubble",
    "bulb": "bulbhead",
    "digi": "digital",
}

@ultroid_cmd(pattern="figlet ?(.*)")
async def figlet(event):
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await eor(event, "Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_SET[cmd]
        except KeyError:
            await eor(event, "Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await eor(event, f"‌‌‎`{result}`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
