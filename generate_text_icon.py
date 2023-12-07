import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, cairo

def generate_svg(number, font_path, output_file):
    width, height = 100, 100

    surface = cairo.Surface(output_file, width, height)
    context = cairo.Context(surface)

    # 设置字体
    context.select_font_face(font_path, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    context.set_font_size(50)

    # 计算文本的宽度和高度
    text_extents = context.text_extents(number)
    text_width = text_extents.width
    text_height = text_extents.height

    # 计算文本的位置，使其居中显示
    x = (width - text_width) / 2
    y = (height + text_height) / 2

    # 绘制文本
    context.move_to(x, y)
    context.show_text(number)
    context.stroke()

    # 保存并关闭SVG图片
    surface.finish()

# 创建output_svg文件夹（如果不存在）
import os
if not os.path.exists("output_svg"):
    os.makedirs("output_svg")

# 指定自定义的TTF字体路径
font_path = "/home/maary/Downloads/ndot-45.ttf" 
# 生成数字0到99的SVG图片
for i in range(100):
    number = str(i) if i < 100 else "!!"
    output_file = f"output_svg/{number}.svg"
    generate_svg(number, font_path, output_file)
