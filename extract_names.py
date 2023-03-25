import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("（1）地图建模   | 用例名称 | 地图建模   | ---------- | -------- |   | 参与者   | 巡检员   | 描述     | 巡检员控制机器人在预定巡检范围内对地图进行建模，产生地图文件    | 前置条件 | 1）巡检员登录系统 2）巡检员进入「巡检区域管理」页面   | 后置条件 | 跳转回巡检区域管理页面，地图列表更新   | 基本流程 | 1. 页面中显示当前存在地图，巡检员点击「新增巡检区域地图」按钮；   |          | 2. 进入新增地图页，页面有地图名称输入框、机器人选择列表、「开始建模」按钮；    |          | 3. 用户输入地图名称、选择机器人列表中的机器人，点击「开始建模」按钮；   |          | 4. 进入实时建模状态页，页面中有当前地图建模结果框，结果框下有「完成建模」和「取消建模」按钮、机器人行驶控制按钮（前、后、转向按钮）、机器人速度控制滑块；   |          | 5. 用户使用页面上的控制按钮或机器人遥控器控制机器人移动，地图建模结果框中地图开始更新；   |          | 6. 用户结束建模，点击「完成建模」按钮，跳转回地图列表，新增地图在列表最上方；    | 补充说明 |")
nouns = set([token.text for token in doc if token.pos_ == "NOUN"])  # Extract all the nouns
print(nouns)