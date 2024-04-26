from PIL import Image, ImageDraw, ImageFont

"""
    该脚本出现的需求点是：在写论文的时候需要贴图大量的例子，但手动一个个贴其实很慢慢，所以可以用该脚本快速批量生成，只需要定义子图片的路径和相应所需要的文本内容即可
    如：
    images_with_text = [
        [('resource/3_512crop_Moment1.jpg', 'Text for image 1'), ('resource/3_512crop_Moment2.jpg', '')],
        [('resource/4_512crop_Moment1.jpg', ''), ('resource/4_512crop_Moment2.jpg', '')],
        # ... 更多图片和文本
    ]
"""



def create_collage_with_text(images_with_text, font_path, font_size, font_color, bg_color=(255, 255, 255), spacing=10, image_width_padding=5, image_text_padding=10):
    """
    创建一个带有文本的图片拼贴画，每行的高度根据该行内所有图片的最大高度决定。
    """
    # 计算每行的最大高度
    max_heights = []
    for row in images_with_text:
        heights = [Image.open(img_path[0]).size[1] for img_path in row if img_path is not None]
        max_heights.append(max(heights))

    # 计算每张图片的宽度
    all_images = []
    for row in images_with_text:
        for item in row:
            if item is not None:  # 跳过None值
                img_path, _ = item
                img = Image.open(img_path)
                all_images.append(img.size)

    widths, _ = zip(*all_images)
    tile_width = max(widths)

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)

    # 创建一个新的指定背景色的空白图片，宽度固定，高度根据行高和间距计算
    new_im = Image.new('RGB', (tile_width * len(images_with_text[0]) + image_width_padding * (len(images_with_text[0]) - 1), sum(max_heights) + spacing * (len(images_with_text))), color=bg_color)

    # 初始化y坐标
    y_offset = 0

    # 遍历所有的小图片和文本，并将它们粘贴到大图片上
    for row_index, row in enumerate(images_with_text):
        x_offset = 0
        # 计算当前行的y偏移，基于之前所有行的高度总和
        current_row_height = max_heights[row_index]
        for col_index, item in enumerate(row):
            if item is None:  # 如果是None，即空白位置，则跳过
                x_offset += tile_width + image_width_padding
                continue
            img_path, text = item
            img = Image.open(img_path)
            img = img.resize((tile_width, current_row_height), Image.LANCZOS)
            new_im.paste(img, (x_offset, y_offset))

            # 如果存在文本，将其绘制在图片下方
            if text:
                draw = ImageDraw.Draw(new_im)
                text_width = font.getlength(text)
                text_x = x_offset + (tile_width - text_width) // 2
                text_y = y_offset + current_row_height + image_text_padding  # 将文本放在图片下方的间隙中
                draw.text((text_x, text_y), text, font=font, fill=font_color)

            x_offset += tile_width + image_width_padding

        y_offset += current_row_height + spacing  # 增加当前行高度和间距

    # 返回拼贴画的Image对象
    return new_im


# 创建拼贴画
"""
    例子1 有一个空白图，带文字
"""
font_path = 'font/tmp_font.ttf'  # 请替换为你的字体文件路径
font_size = 45
font_color = (0, 0, 0)  # 黑色
bg_color = (255, 255, 255)  # 白色
spacing = font_size + 20  # 行与行之间的间距
images_with_text = [
    [('resource/3_512crop_Moment1.jpg', 'Text for image 1'), ('resource/3_512crop_Moment2.jpg', ''), ('resource/3_512crop_Moment3.jpg', 'Text for image 3')],
    [('resource/4_512crop_Moment1.jpg', ''), ('resource/4_512crop_Moment2.jpg', ''), ('resource/4_512crop_Moment3.jpg', '')],
    [None, ('resource/5_512crop_Moment1.jpg', 'Image5 1'), ('resource/5_512crop_Moment2.jpg', 'Image5 2')],
    # ... 更多图片和文本
]
collage = create_collage_with_text(images_with_text, font_path, font_size, font_color, bg_color, spacing)
collage.save('collage_with_text1.jpg')

print('ok')

# 创建拼贴画
"""
    例子2 不带任何文字
"""
font_path = 'font/tmp_font.ttf'  # 请替换为你的字体文件路径
font_size = 45
font_color = (0, 0, 0)  # 黑色
bg_color = (255, 255, 255)  # 白色
spacing = 5  # 行与行之间的间距
images_with_text = [
    [('resource/3_512crop_Moment1.jpg', ''), ('resource/3_512crop_Moment2.jpg', ''), ('resource/3_512crop_Moment3.jpg', '')],
    [('resource/4_512crop_Moment1.jpg', ''), ('resource/4_512crop_Moment2.jpg', ''), ('resource/4_512crop_Moment3.jpg', '')],
    [None, ('resource/5_512crop_Moment1.jpg', ''), ('resource/5_512crop_Moment2.jpg', '')],
    # ... 更多图片和文本
]
collage = create_collage_with_text(images_with_text, font_path, font_size, font_color, bg_color, spacing)
collage.save('collage_with_text2.jpg')

print('ok')


# 创建拼贴画
"""
    例子3 正常带文字
"""
font_path = 'font/tmp_font.ttf'  # 请替换为你的字体文件路径
font_size = 45
font_color = (0, 0, 0)  # 黑色
bg_color = (255, 255, 255)  # 白色
spacing = font_size + 20  # 行与行之间的间距
images_with_text = [
    [('resource/3_512crop_Moment1.jpg', '3_1'), ('resource/3_512crop_Moment2.jpg', '3_2'), ('resource/3_512crop_Moment3.jpg', '3_3')],
    [('resource/4_512crop_Moment1.jpg', '4_1'), ('resource/4_512crop_Moment2.jpg', '4_2'), ('resource/4_512crop_Moment3.jpg', '4_3')],
    [('resource/5_512crop_Moment1.jpg', '5_1'), ('resource/5_512crop_Moment2.jpg', '5_2'), ('resource/5_512crop_Moment3.jpg', '5_3')],
    # ... 更多图片和文本
]
collage = create_collage_with_text(images_with_text, font_path, font_size, font_color, bg_color, spacing)
collage.save('collage_with_text3.jpg')

print('ok')

# 创建拼贴画
"""
    例子4 不同图片大小组合
"""
font_path = 'font/tmp_font.ttf'  # 请替换为你的字体文件路径
font_size = 45
font_color = (0, 0, 0)  # 黑色
bg_color = (255, 255, 255)  # 白色
spacing = font_size + 20  # 行与行之间的间距
images_with_text = [
    [('resource/3_512crop_Moment1.jpg', '3_1'), ('resource/3_512crop_Moment2.jpg', '3_2'), ('resource/3_512crop_Moment3.jpg', '3_3')],
    [('resource/4_512crop_Moment1.jpg', '4_1'), ('resource/4_512crop_Moment2.jpg', '4_2'), ('resource/4_512crop_Moment3.jpg', '4_3')],
    [('resource/5_512crop_Moment1.jpg', '5_1'), ('resource/5_512crop_Moment2.jpg', '5_2'), ('resource/5_512crop_Moment3.jpg', '5_3')],
    [('resource/6_special.jpg', '6_1')],
    [('resource/5_512crop_Moment1.jpg', '5_1'), ('resource/5_512crop_Moment2.jpg', '5_2'), ('resource/5_512crop_Moment3.jpg', '5_3')],
    # ... 更多图片和文本
]
collage = create_collage_with_text(images_with_text, font_path, font_size, font_color, bg_color, spacing)
collage.save('collage_with_text4.jpg')

print('ok')