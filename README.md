<h3 style="color: blue;">queueSequence:</h3>
利用rgthree的fast_group_muter和bookmark节点，引入pyautogui库，模拟点击和热键，依次运行group。涉及到屏幕操作，请注意以下几点：
1. 第一个bookmark的热键和缩放比不要改
2. 第一个bookmak和fast_group_muter叠放在一起，相对位置要固定
3. queue一次后，用ctrl+/组合键测量fast_group_muter节点中第一个组的中心位置，在控制台中将打印出来坐标
4. 填入group1_x 和_y
5. totalRounds 控制整个序列运行轮数
6. numOfQueues 是每一个序列中有多少组（多少个小序列），一般而言，fast_group_muter中有多少组，这里就填多少

Using rgthree's fast_group_muter and bookmark nodes, introduce the pyautogui library to simulate clicks and hotkeys, and run groups in sequence. screen manipulation is involved, so please note the following:
1. don't change the hotkeys and zoom ratios of the first bookmark
2. the first bookmark and fast_group_muter are stacked on top of each other, and their relative positions should be fixed.
3. after queueing once, measure the center of the first group in the fast_group_muter node with the ctrl+/ key combination, and the coordinates will be printed out in the console
4. Fill in group1_x and _y.
5. totalRounds controls the number of rounds the sequence will run.
6. numOfQueues is the number of groups in each sequence (how many small sequences), in general, the number of groups in fast_group_muter is the number of groups here
<img src="https://github.com/blueraincoatli/comfyUI_SillyNodes/blob/myWorkflow/example/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20240324165032.png?raw=true" width="600" >

<h3 style="color: blue;">booleanJumper:</h3>
接收一个boolean值，根据节点中的定义跳转到相应节点，激活并运行。
Receives a boolean value, jumps to the appropriate node based on the definition in the node, activates and queues.
<img src="https://github.com/blueraincoatli/comfyUI_SillyNodes/blob/myWorkflow/example/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20240324170509.png?raw=true" width="600" >
<img src="https://github.com/blueraincoatli/comfyUI_SillyNodes/blob/myWorkflow/example/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20240324170625.png?raw=true" width="600" >
   
<h3 style="color: blue;">screenShot:</h3>
只需将 "trigger_field "转换为输入，并链接一个 INT 节点。
无论前一个节点的输入是多少，它都会截取全屏并输出图像。
print_to_screen 暂时没有用。
Just convert the 'trigger_field' to the input, an link a INT node. 
whatever int input from the previous node, it takes a full screenshot, and output an image.
The print_to_screen is no use for now.
<img src="https://github.com/blueraincoatli/comfy_screenshots/blob/main/example/20240112104802.png">
