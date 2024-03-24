import pyautogui  
import time  
import keyboard  
  
class BooleanJumper:  
    y_step = 36  # Step value for the y-coordinate  
      
    def __init__(self):  
        self.group1_x = 160  # Initialize default x-coordinate value  
        self.group1_y = 460  # Initialize default y-coordinate value  
          
        # Code to add a listener for Ctrl+/ event to capture mouse position  
        print("Press Ctrl+/ to get the current mouse position.")  
        keyboard.add_hotkey('ctrl+/', self.print_mouse_position) 

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "true_false": ("STRING", {"forceInput": True}),
                "group1_x": ("INT", {"default": 160, "min": 0, "max": 4096, "step": 1}),
                "group1_y": ("INT", {"default": 460, "min": 0, "max": 4096, "step": 1}),
                "groupIndex_if_true": ("INT", {"default": 1, "min": 1, "max": 20}),   
                "groupIndex_if_false": ("INT", {"default": 1, "min": 1, "max": 20}),   
            },
        }
    
    RETURN_TYPES =("BOOLEAN",)
    OUTPUT_NODE = True
    FUNCTION = "jump_to"    
    CATEGORY = "SillyNode"


    def str_to_bool(self, true_false):  # 注意这里添加了self参数  
        if true_false.lower() == 'true':    
            return True    
        elif true_false.lower() == 'false':    
            return False    
        else:    
            raise ValueError('Cannot convert string to boolean')  

    
    def jump_to(self, true_false, group1_x=None, group1_y=None, groupIndex_if_true=None, groupIndex_if_false=None,unique_id=None, extra_pnginfo=None):  
        # 使用str_to_bool方法将字符串转换为布尔值  
        boolean_value = self.str_to_bool(true_false)
          
        if group1_x is None:  
            group1_x = self.group1_x  
        if group1_y is None:  
            group1_y = self.group1_y  
          
        if boolean_value:  
            if groupIndex_if_true is not None:  
                y_coordinate = group1_y + ((groupIndex_if_true-1) * self.y_step) 
                bookmark = groupIndex_if_true 
            else:  
                raise ValueError("groupIndex_if_true cannot be None")  
        else:  
            if groupIndex_if_false is not None:  
                y_coordinate = group1_y + ((groupIndex_if_false-1) * self.y_step)
                bookmark = groupIndex_if_false  
            else:  
                raise ValueError("groupIndex_if_false cannot be None")  
          
        pyautogui.press('1')  # Simulate pressing the number 1 key  
        time.sleep(1)  
        pyautogui.click(group1_x, y_coordinate)  # Click at the specified coordinates  
        time.sleep(1)
        pyautogui.press(str(bookmark))  # Simulate pressing the number key
        time.sleep(1)  
        pyautogui.hotkey('ctrl', 'enter')
          
        return (boolean_value,) 

    # Prints the default position with an added offset in the y-coordinate
    def print_mouse_position(self):
        x, y = pyautogui.position()
        print(f"default position is: x={x}, y={y}")


NODE_CLASS_MAPPINGS = {
    "BooleanJumper|SillyNode": BooleanJumper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BooleanJumper|SillyNode": "Boolean Jumper"
}