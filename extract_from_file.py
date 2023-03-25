import re

# 打开文件并读取内容
with open('/home/maary/Documents/articles/graduation/doc/tmp.md', 'r') as file:
    content = file.read()

# 匹配以 ** 开头和以 ** 结尾的字符串
matches = re.findall(r'\*\*(.*?)\*\*', content)

# 输出所有匹配的结果
print(matches)