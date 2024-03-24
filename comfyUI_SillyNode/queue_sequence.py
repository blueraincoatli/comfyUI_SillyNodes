import pyautogui
import time
import keyboard
from server import PromptServer
import torch

# Sends a formatted message to a specified ID. If the message is a torch.Tensor, include its shape. If it's a dict with a tensor under "samples", include its shape. Otherwise, cast message to a string.
def message(id, message):
    if isinstance(message, torch.Tensor):
        string = f"Tensor shape {message.shape}"
    elif isinstance(message, dict) and "samples" in message and isinstance(message["samples"], torch.Tensor):
        string = f"Latent shape {message['samples'].shape}"
    else:
        string = f"{message}"
    PromptServer.instance.send_sync("ue-message-handler", {"id": id, "message": string})


class QueueSequence:
    y_step = 36  # Step value for the y-coordinate

    def __init__(self):
        self.group1_x = 160  # Initialize default x-coordinate value
        self.group1_y = 495  # Initialize default y-coordinate value
        self.current_round = 0  # Initialize the current round count as an instance attribute

        # Code to add a listener for Ctrl+/ event to capture mouse position
        print("Press Ctrl+/ to get the current mouse position.")
        keyboard.add_hotkey('ctrl+/', self.print_mouse_position)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger_field": ("INT", {"forceInput": True}),
                "group1_x": ("INT", {"default": 160, "min": 0, "max": 4096, "step": 1}),
                "group1_y": ("INT", {"default": 495, "min": 0, "max": 4096, "step": 1}),
                "totalRounds": ("INT", {"default": 1, "min": 0, "max": 4096, "step": 1}),
                "numOfQueues": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
            },
            "optional": { "anything" : ("*", {}) },
        }

    def func(self, id, **kwargs):
        # Send a signal message
        message(id, "Signal received.")
        return ()

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    FUNCTION = "simulate_actions"

    CATEGORY = "SillyNode"

    def simulate_actions(self, trigger_field, group1_x=None, group1_y=None, totalRounds=None, numOfQueues=None, anything=None):

        # If new values for group1_x and group1_y are passed, update the class attributes with them
        if group1_x is not None:
            self.group1_x = group1_x
        if group1_y is not None:
            self.group1_y = group1_y
        if totalRounds is not None:
            self.totalRounds = totalRounds
        if numOfQueues is not None:
            self.numOfQueues = numOfQueues

        # Update the current round count
        self.current_round += 1

        # Decide whether to continue the loop based on the values of totalRounds and numOfQueues
        if self.current_round > numOfQueues * totalRounds:
            self.current_round = 0
            return [trigger_field]  # Stop the loop and return the result

        # Decide whether to perform modulo operation on trigger_field based on the value of totalRounds
        if totalRounds != 1:
            trigger_field = (trigger_field % numOfQueues) - 1

        if totalRounds == 1:
            trigger_field = (trigger_field % numOfQueues)

        y_coordinate = self.group1_y + (trigger_field * self.y_step)
        bookmark = trigger_field + 3

        # Actual simulation of keypresses and mouse actions
        time.sleep(3)
        pyautogui.press('1')  # Simulate pressing the number 1 key
        time.sleep(0.5)
        pyautogui.click(self.group1_x, y_coordinate)  # Click at the specified coordinates
        time.sleep(0.5)
        pyautogui.press(str(bookmark))  # Simulate pressing the number key
        time.sleep(0.5)
        # Decide whether to execute Ctrl+Enter based on the values of trigger_field and numOfQueues
        if trigger_field + 1 < numOfQueues:  # Execute when trigger_field is less than numOfQueues
            pyautogui.hotkey('ctrl', 'enter')
        time.sleep(0.5)

        return [trigger_field]

    # Prints the default position with an added offset in the y-coordinate
    def print_mouse_position(self):
        x, y = pyautogui.position()
        print(f"default position is: x={x}, y={y + self.y_step}")

NODE_CLASS_MAPPINGS = {
    "QueueSequence|SillyNode": QueueSequence
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QueueSequence|SillyNode": "Queue Sequence"
}