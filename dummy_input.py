from server import PromptServer
import torch

class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False

any = AnyType("*")


class dummyInput:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )},
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True

    RETURN_TYPES = (any,)
    OUTPUT_NODE = False
    FUNCTION = "dummy_input"
    CATEGORY = "Blueraincoat"
    
    def dummy_input(self, value):

         return (value,)


NODE_CLASS_MAPPINGS = {
    "dummyInput|blueraincoat": dummyInput
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "dummyInput|blueraincoat": "Dummy Input"
}