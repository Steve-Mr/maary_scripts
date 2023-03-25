from collections import OrderedDict

s = "'地图', '机器人', '巡检范围', '地图文件', '巡检区域', '地图名称', '巡检路径', '巡检点', '巡检动作', '巡检路径', '巡检点', '路径点', '巡检特殊区域', '巡检计划', '巡检路线', '地图', '巡检路线', '巡检动作', '机器人实时数据', '巡检结果', '24小时内巡检结果', '巡检报告', '警报', '资源', '虚拟物理环境', '虚拟巡检地图', '虚拟机器人', '虚拟巡检路径', '虚拟巡检点', '虚拟巡检动作', '路径点', '充电位置点', '巡检动作点', '路径点', '虚拟巡检特殊区域', '测试计划', '虚拟巡检路径', '测试报告', '虚拟机器人', '机器人配置', '实体机器人', '机器人', '机器人配置', '系统操作日志', '系统运行日志', '系统日志', '系统资源', '历史数据', '巡检记录', '巡检历史数据'"
word_list = s.split(",")  # 按照 "、" 分隔成单词列表
word_dict = OrderedDict.fromkeys(word_list)  # 将列表转换为有序字典，去除重复单词并保留顺序
result = "、".join(word_dict.keys())  # 将字典的键按照 "、" 连接成字符串
print(result)  # 输出结果为：hello、world、python