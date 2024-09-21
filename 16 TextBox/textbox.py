from PIL import Image, ImageDraw, ImageFont
import os


def wrap_text(text, font, max_width):
    """
    根据像素宽度将文本拆分为多行，确保每行的宽度不超过 max_width。

    :param text: 要拆分的文本
    :param font: 字体对象
    :param max_width: 每行的最大宽度（像素）
    :return: 拆分后的多行文本列表
    """
    lines = []
    words = text.split()
    if not words:
        return lines

    current_line = words[0]
    for word in words[1:]:
        # 测试加入下一个单词后的行宽
        test_line = current_line + ' ' + word
        line_width, _ = font.getsize(test_line)
        if line_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines


def fit_text(draw, text, font_path, max_width, max_font_size, min_font_size):
    """
    调整字体大小以适应指定宽度。如果在最小字体大小下仍然过长，则进行换行。

    :param draw: ImageDraw 对象
    :param text: 要绘制的文本
    :param font_path: 字体文件路径
    :param max_width: 最大宽度
    :param max_font_size: 最大字体大小
    :param min_font_size: 最小字体大小
    :return: (调整后的字体对象, 分行后的文本列表)
    """
    for font_size in range(max_font_size, min_font_size - 1, -1):
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            continue  # 跳过无法加载的字体大小
        lines = wrap_text(text, font, max_width)
        if all(font.getsize(line)[0] <= max_width for line in lines):
            return font, lines

    # 如果仍然无法适应，返回最小字体和拆分后的文本
    try:
        font = ImageFont.truetype(font_path, min_font_size)
    except IOError:
        font = ImageFont.load_default()
    lines = wrap_text(text, font, max_width)
    return font, lines


def draw_text_bold(draw, position, text, font, fill, spacing=1):
    """
    绘制加粗的文本，通过多次绘制轻微偏移来模拟粗体效果。

    :param draw: ImageDraw 对象
    :param position: 文本起始位置 (x, y)
    :param text: 要绘制的文本
    :param font: 字体对象
    :param fill: 文本颜色
    :param spacing: 偏移量
    """
    x, y = position
    # 绘制多次，偏移不同方向
    draw.text((x - spacing, y), text, font=font, fill=fill)
    draw.text((x + spacing, y), text, font=font, fill=fill)
    draw.text((x, y - spacing), text, font=font, fill=fill)
    draw.text((x, y + spacing), text, font=font, fill=fill)
    draw.text(position, text, font=font, fill=fill)


# 文本框内容
content = {
    "title": "What is the main cause of climate change?",
    "content": (
        "The main cause of climate change is the increased concentration of greenhouse gases in the atmosphere, "
        "primarily due to human activities like burning fossil fuels, deforestation, and industrial processes. "
        "These gases trap heat from the sun, leading to a warming effect known as the greenhouse effect, which "
        "results in global temperature rises and shifts in weather patterns."
    ),
    "title_fontsize": 24,  # 设置标题字体大小
    "content_fontsize": 20,  # 设置内容字体大小
    "title_bold": True,  # 设置标题是否加粗
    "box_width": 700,  # 设置文本框宽度（像素）
    "box_height": 300,  # 设置文本框高度（像素）
}

# 创建图片
padding = 20  # 图像与文本框的内边距
img_width = content["box_width"] + 2 * padding
img_height = content["box_height"] + 2 * padding
image = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(image)

# 设置字体路径（确保字体文件存在于指定路径）
font_name = "arial.ttf"  # 根据系统字体路径调整


# 查找字体文件路径
def find_font_path(font_name, bold=False):
    """
    在系统中查找指定字体文件的路径。如果bold为True，尝试查找粗体版本。
    """
    # 针对不同操作系统的字体路径
    if os.name == "nt":  # Windows
        base_paths = [
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts'),
            'C:\\Windows\\Fonts'
        ]
        if bold:
            # 常见的粗体字体命名方式
            bold_font_name = font_name.replace('.ttf', 'bd.ttf')
        else:
            bold_font_name = font_name
    elif os.name == "posix":
        base_paths = [
            "/usr/share/fonts/truetype",
            "/usr/local/share/fonts",
            "/Library/Fonts"  # macOS
        ]
        if bold:
            # macOS 常见粗体字体命名方式
            bold_font_name = font_name.replace('.ttf', ' Bold.ttf')
        else:
            bold_font_name = font_name
    else:
        base_paths = []
        bold_font_name = font_name  # 默认

    for base_path in base_paths:
        potential_path = os.path.join(base_path, bold_font_name)
        if os.path.exists(potential_path):
            return potential_path

    # 如果没有找到粗体字体，返回 None
    return None


# 尝试找到标题的粗体字体路径
title_font_path = find_font_path(font_name, bold=True)
if title_font_path is None:
    print(f"未找到粗体字体 '{font_name}' 的粗体版本，将使用普通字体并模拟加粗。")
    title_font_path = find_font_path(font_name, bold=False)
    title_bold_simulate = content.get("title_bold", False)  # 需要模拟加粗
else:
    title_bold_simulate = False  # 使用粗体字体，无需模拟加粗

# 查找内容字体路径
content_font_path = find_font_path(font_name, bold=False)

if title_font_path is None:
    print(f"未找到字体文件 '{font_name}'，将使用默认字体。")
    use_default_font = True
else:
    print(f"标题字体文件路径: {title_font_path}")
    use_default_font = False

if content_font_path is None:
    print(f"未找到内容字体文件 '{font_name}'，将使用默认字体。")
    use_content_default_font = True
else:
    print(f"内容字体文件路径: {content_font_path}")
    use_content_default_font = False

# 绘制阴影效果 (灰色的偏移矩形)
shadow_color = (200, 200, 200)  # 调整阴影颜色更柔和
shadow_offset = 5  # 阴影偏移量
box_x0, box_y0 = padding, padding
box_x1, box_y1 = padding + content["box_width"], padding + content["box_height"]

draw.rounded_rectangle(
    [box_x0 + shadow_offset, box_y0 + shadow_offset, box_x1 + shadow_offset, box_y1 + shadow_offset],
    radius=15, fill=shadow_color
)

# 绘制圆角边框
draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=15, outline="black", width=3, fill="white")

# 自动调整标题字体大小和换行
max_title_width = content["box_width"] - 40  # 保持左右20像素的内边距
max_font_size_title = content.get("title_fontsize", 24)  # 默认24
min_font_size_title = 15  # 可以根据需要调整

if not use_default_font:
    try:
        # 调整标题字体
        title_font, title_lines = fit_text(
            draw,
            content["title"],
            title_font_path,
            max_title_width,
            max_font_size_title,
            min_font_size_title
        )
    except IOError:
        # 如果指定字体无法加载，使用默认字体
        title_font = ImageFont.load_default()
        title_lines = [content["title"]]
else:
    title_font = ImageFont.load_default()
    title_lines = [content["title"]]

# 计算标题总高度
line_height_title = title_font.getsize('A')[1]
spacing_title = 10  # 每行之间的间距
title_text_total_height = len(title_lines) * line_height_title + (len(title_lines) - 1) * spacing_title

# 设置固定的标题背景高度
fixed_title_bg_height = max(60, title_text_total_height + 20)  # 最小高度60，确保有足够空间
title_bg_y0 = box_y0
title_bg_y1 = title_bg_y0 + fixed_title_bg_height

# 绘制标题黑色背景
draw.rectangle([box_x0, title_bg_y0, box_x1, title_bg_y1], fill="black")

# 计算垂直居中的起始Y坐标
available_height = fixed_title_bg_height
start_y = title_bg_y0 + (available_height - title_text_total_height) // 2

# 绘制标题文本（加粗）
title_x = box_x0 + 20  # 左边距20像素
current_y = start_y

for line in title_lines:
    if not use_default_font:
        if title_font_path and not title_bold_simulate:
            # 使用粗体字体直接绘制
            draw.text((title_x, current_y), line, font=title_font, fill="white")
        elif title_bold_simulate:
            # 模拟加粗效果
            draw_text_bold(draw, (title_x, current_y), line, title_font, fill="white", spacing=1)
        else:
            # 普通绘制
            draw.text((title_x, current_y), line, font=title_font, fill="white")
    else:
        # 使用默认字体，无法加粗
        draw.text((title_x, current_y), line, font=title_font, fill="white")
    current_y += line_height_title + spacing_title

# 设置内容文本左对齐，并进行自动换行
content_text = content["content"]
content_x = box_x0 + 20  # 左边距20像素
content_y = title_bg_y1 + 30  # 内容与标题背景有30像素间隔
content_max_width = content["box_width"] - 40  # 左右各20像素内边距

# 获取内容字体大小
content_font_size = content.get("content_fontsize", 16)  # 默认16

if not use_content_default_font and content_font_path is not None:
    try:
        content_font = ImageFont.truetype(content_font_path, content_font_size)
    except IOError:
        content_font = ImageFont.load_default()
else:
    content_font = ImageFont.load_default()

# 拆分内容为多行（基于像素宽度的换行）
wrapped_content = wrap_text(content_text, content_font, content_max_width)
content_lines = wrapped_content

# 绘制内容文本为左对齐
for line in content_lines:
    draw.text((content_x, content_y), line, font=content_font, fill="black")
    content_y += content_font.getsize(line)[1] + 5  # 行间距5像素

# 检查内容是否超出图片高度
if content_y > box_y1:
    print("注意：内容超出图片范围，您可能需要增加图片高度或缩小字体。")

# 保存图片
output_path = "output.png"
image.save(output_path)
image.show()  # 可视化显示图片

print(f"图片已保存到 {output_path}")