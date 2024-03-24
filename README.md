queueSequence:
利用rgthree的fast_group_muter和bookmark节点，引入pyautogui库，模拟点击和热键，依次运行group。涉及到屏幕操作，请注意以下几点：
1. 第一个bookmark的热键和缩放比不要改
2. 第一个bookmak和fast_group_muter叠放在一起，相对位置要固定
3. queue一次后，用ctrl+/组合键测量fast_group_muter节点中第一个组的中心位置，在控制台中将打印出来坐标
4. 填入group1_x 和_y
5. totalRounds 控制整个序列运行轮数
6. numOfQueues 是每一个序列中有多少组（多少个小序列），一般而言，fast_group_muter中有多少组，这里就填多少
   

Just convert the 'trigger_field' to the input, an link a INT node. 
whatever int input from the previous node, it takes a full screenshot, and output an image.
The print_to_screen is no use for now.

<img src="https://github.com/blueraincoatli/comfy_screenshots/blob/main/example/20240112104802.png">
