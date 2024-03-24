import pyautogui
import comfy
import comfy.utils

from .screenshots import Screenshots
from .queue_sequence import QueueSequence
from .dummy_input import dummyInput
from .boolean_jumper import BooleanJumper

Screenshots.CATEGORY = "SillyNode"
QueueSequence.CATEGORY = "SillyNode"
dummyInput.CATEGORY = "SillyNode"
BooleanJumper.CATEGORY = "SillyNode"


NODE_CLASS_MAPPINGS = {
    "Screenshots|SillyNode": Screenshots,
    "QueueSequence|SillyNode": QueueSequence,
    "dummyInput|SillyNode": dummyInput,
    "BooleanJumper|SillyNode": BooleanJumper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Screenshots|SillyNode": "Screen Shots",
    "QueueSequence|SillyNode": "Queue Sequence",
    "dummyInput|SillyNode": "Dummy Input",
    "BooleanJumper|SillyNode": "Boolean Jumper"
}


# WEB_DIRECTORY is the comfyui nodes directory that ComfyUI will link and auto-load.
WEB_DIRECTORY = "./js"


__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
