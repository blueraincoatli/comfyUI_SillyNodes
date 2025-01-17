import pyautogui
import time
import os
import itchat  # 添加: 导入 itchat 库

class CloseErrorWindowNode:
    def __init__(self):
        # 添加: 初始化微信登录
        itchat.auto_login(hotReload=True)
        self.to_user = 'filehelper'  # 可以修改为其他用户的微信号或文件助手

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ()
    FUNCTION = "close_error_window"
    CATEGORY = "SillyNode"

    def close_error_window(self):
        # 尝试检测报错信息窗口的特定文本或图像
        try:
            # 使用多个图像模板来匹配错误窗口的关闭按钮
            close_button_templates = ['close_button.png', 'error_close_button.png']
            template_path = os.path.join(os.path.dirname(__file__), 'templates')
            for template in close_button_templates:
                template_full_path = os.path.join(template_path, template)
                close_button_location = pyautogui.locateOnScreen(template_full_path, confidence=0.9)
                if close_button_location:
                    close_button_center = pyautogui.center(close_button_location)
                    pyautogui.click(close_button_center)
                    print("Error window closed.")
                    # 添加: 发送微信消息
                    itchat.send_msg("Error window closed.", toUserName=self.to_user)
                    return
            print("Error window not found.")
            # 添加: 发送微信消息
            itchat.send_msg("Error window not found.", toUserName=self.to_user)
        except Exception as e:
            print(f"An error occurred: {e}")
            # 添加: 发送微信消息
            itchat.send_msg(f"An error occurred: {e}", toUserName=self.to_user)