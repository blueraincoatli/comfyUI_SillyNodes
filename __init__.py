import pyautogui
import comfy
import comfy.utils

from .screenshots import Screenshots
from .queue_sequence import QueueSequence
from .dummy_input import dummyInput
from .boolean_jumper import BooleanJumper
from .close_error_window_node import CloseErrorWindowNode  # 修改: 导入 CloseErrorWindowNode 类

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update({
    "Screenshots|SillyNode": Screenshots,
    "QueueSequence|SillyNode": QueueSequence,
    "dummyInput|SillyNode": dummyInput,
    "BooleanJumper|SillyNode": BooleanJumper,
    "CloseErrorWindowNode|SillyNode": CloseErrorWindowNode  # 修改: 注册 CloseErrorWindowNode 节点
})

NODE_DISPLAY_NAME_MAPPINGS = {
    "Screenshots|SillyNode": "Screen Shots",
    "QueueSequence|SillyNode": "Queue Sequence",
    "dummyInput|SillyNode": "Dummy Input",
    "BooleanJumper|SillyNode": "Boolean Jumper",
    "CloseErrorWindowNode|SillyNode": "Close Error Window"  # 添加这一行以显示节点名称
}

# WEB_DIRECTORY is the comfyui nodes directory that ComfyUI will link and auto-load.
WEB_DIRECTORY = "./js"

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]