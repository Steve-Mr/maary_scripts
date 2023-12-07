def process_text(input_text):
    lines = input_text.splitlines()
    output_lines = [f"\\item {line.strip()}" for line in lines if line.strip()]
    return "\n".join(output_lines)

user_input = ""
processing = False

while True:
    line = input()
    user_input += line + "\n"

    if line.strip().lower() == 'aaa':
        # processing = not processing
        # if processing:
        #     print("开始处理输入的内容...")
        # else:
            processed_text = process_text(user_input)
            print("处理后的结果：")
            print(processed_text)
            user_input = ""
            print("输入 'aaa' 以继续或输入 'exit' 退出程序:")

    elif line.strip().lower() == 'exit':
        break
