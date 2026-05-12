import os as _os
_os.environ.setdefault('DISPLAY', ':0')
import pyautogui
import comfy
import comfy.utils

from .screenshots import Screenshots
from .queue_sequence import QueueSequence
from .dummy_input import dummyInput
from .boolean_jumper import BooleanJumper
from .text_batch_load_path import TextBatchLoadPath

Screenshots.CATEGORY = "SillyNode"
QueueSequence.CATEGORY = "SillyNode"
dummyInput.CATEGORY = "SillyNode"
BooleanJumper.CATEGORY = "SillyNode"


NODE_CLASS_MAPPINGS = {
    "Screenshots|SillyNode": Screenshots,
    "QueueSequence|SillyNode": QueueSequence,
    "dummyInput|SillyNode": dummyInput,
    "BooleanJumper|SillyNode": BooleanJumper,
    "TextBatchLoadPath|SillyNode": TextBatchLoadPath 
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Screenshots|SillyNode": "Screen Shots",
    "QueueSequence|SillyNode": "Queue Sequence",
    "dummyInput|SillyNode": "Dummy Input",
    "BooleanJumper|SillyNode": "Boolean Jumper",
    "TextBatchLoadPath|SillyNode": "Text Batch Load (Path)"  
}


# WEB_DIRECTORY is the comfyui nodes directory that ComfyUI will link and auto-load.
WEB_DIRECTORY = "./js"


__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
