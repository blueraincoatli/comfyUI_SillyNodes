import pyautogui
import torch
from PIL import Image 
import numpy as np
from nodes import PreviewImage
import time
from importlib import import_module
import os
import sys

# Get the absolute path of various directories
my_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_dir = os.path.abspath(os.path.join(my_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(my_dir, '..', '..'))

# Append comfy_dir to sys.path & import files
sys.path.append(comfy_dir)
from nodes import PreviewImage
import comfy.utils

sys.path.remove(comfy_dir)


class Screenshots:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):  # whatever int input from the previous node
        return {
            "required": {
                "trigger_field": ("INT", {
                    "default": 0,
                    "min": 0,  # Minimum value
                    "max": 99999999999,  # Maximum value
                    "step": 1,  # Slider's step
                    "display": "number"  # Cosmetic only: display as "number" or "slider"
                }),
                "print_to_screen": (["enable", "disable"],),
            },

        }

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "process_image"

    CATEGORY = "SillyNode"

    def process_image(self, trigger_field, print_to_screen):

            time.sleep(int(trigger_field)/1000)

            # Capture the screenshot
            screenshot = pyautogui.screenshot()

            # Convert the screenshot to an image
            image = screenshot.convert("RGB")

            # Convert the image to a NumPy arra,Normalize the image values to the range [0, 1]
            image = np.array(image).astype(np.float32) / 255.0

            # Convert the NumPy array to a PyTorch tensor, Add a batch dimension to the tensor
            image = torch.from_numpy(image)[None,]
                
            # return (image,)

            # Preview the image
            preview = PreviewImage().save_images(image)["ui"]
             
            return (image,)


NODE_CLASS_MAPPINGS = {
    "Screenshots|SillyNode": Screenshots
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Screenshots|SillyNode": "Screen Shots"
}