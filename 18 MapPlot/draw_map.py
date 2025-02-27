      
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random
import matplotlib

# 设置matplotlib支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

def generate_random_objects(num_objects=10):
    """生成随机物体数据"""
    object_types = ['椅子', '桌子', '沙发', '床', '柜子', '书架', '电视', '灯', '植物', '冰箱']
    object_bboxes = {}
    
    for i in range(num_objects):
        # 随机选择物体类型
        obj_type = random.choice(object_types)
        obj_id = f"{i+1:03d}"
        
        # 随机生成中心点
        center_x = random.uniform(-5, 5)
        center_y = random.uniform(-5, 5)
        
        # 随机生成尺寸
        width = random.uniform(0.5, 2.0)
        height = random.uniform(0.5, 2.0)
        
        # 随机生成旋转角度
        angle = random.uniform(0, 90)
        
        # 计算四个角点
        corners = np.array([
            [center_x - width/2, center_y - height/2],
            [center_x + width/2, center_y - height/2],
            [center_x + width/2, center_y + height/2],
            [center_x - width/2, center_y + height/2]
        ])
        
        # 旋转角点
        theta = np.radians(angle)
        rot_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        
        # 将角点围绕中心点旋转
        center = np.array([center_x, center_y])
        corners = np.array([(rot_matrix @ (corner - center).T).T + center for corner in corners])
        
        object_bboxes[f"{obj_type}_{obj_id}"] = {
            'center': np.array([center_x, center_y]),
            'width': width,
            'height': height,
            'angle': angle,
            'corners': corners
        }
    
    return object_bboxes

def plot_2d_scene(object_bboxes, output_path=None, start_point=None, obj_center=None):
    """绘制2D场景图"""
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_facecolor('white')
    
    # 收集所有需要显示的点
    all_points = []
    
    # 设置颜色循环
    colors = plt.cm.rainbow(np.linspace(0, 1, len(object_bboxes)))
    
    # 绘制物体边界框
    for (label_with_id, bbox), color in zip(object_bboxes.items(), colors):
        label = label_with_id.rsplit('_', 1)[0]
        object_id = label_with_id.rsplit('_', 1)[1]
        
        # 创建多边形
        polygon = Polygon(bbox['corners'], 
                         facecolor=color, 
                         edgecolor='black',
                         alpha=0.5,
                         linewidth=1)
        ax.add_patch(polygon)
        
        # 在中心添加标签
        center = bbox['center']
        ax.text(center[0], center[1], 
                f"{label}\n(ID: {object_id})", 
                fontsize=8, 
                ha='center', 
                va='center',
                color='black')
        
        # 添加物体边界框的角点到显示范围计算中
        all_points.append(bbox['corners'])
    
    # 绘制起点（红色星标）
    if start_point is not None:
        ax.scatter(start_point[0], start_point[1], 
                  color='red', 
                  marker='*', 
                  s=200, 
                  label='起点', 
                  zorder=5)
        all_points.append(start_point.reshape(1, 2))
    
    # 绘制目标点（蓝色圆点）
    if obj_center is not None:
        ax.scatter(obj_center[0], obj_center[1], 
                  color='blue', 
                  marker='o', 
                  s=200, 
                  label='目标点', 
                  zorder=5)
        all_points.append(obj_center.reshape(1, 2))
    
    ax.set_aspect('equal')
    if start_point is not None or obj_center is not None:
        ax.legend()
    
    # 合并所有点并计算显示范围
    all_points = np.vstack(all_points)
    x_min, y_min = all_points.min(axis=0) - 1  # 减1米作为边距
    x_max, y_max = all_points.max(axis=0) + 1  # 加1米作为边距
    
    # 确保坐标轴经过原点(0,0)
    x_min = min(x_min, 0)
    y_min = min(y_min, 0)
    x_max = max(x_max, 0)
    y_max = max(y_max, 0)
    
    # 确保显示范围是正方形（保持纵横比）
    x_range = x_max - x_min
    y_range = y_max - y_min
    max_range = max(x_range, y_range)
    center_x = (x_max + x_min) / 2
    center_y = (y_max + y_min) / 2
    
    x_min = center_x - max_range/2 - 1
    x_max = center_x + max_range/2 + 1
    y_min = center_y - max_range/2 - 1
    y_max = center_y + max_range/2 + 1
    
    # 再次确保包含原点
    x_min = min(x_min, 0)
    y_min = min(y_min, 0)
    x_max = max(x_max, 0)
    y_max = max(y_max, 0)
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    
    # 添加网格
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # 添加坐标轴
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    plt.xlabel('X轴 (米)')
    plt.ylabel('Y轴 (米)')
    plt.title('场景俯视图 - 随机生成的家具布局')
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"2D场景图已保存至 {output_path}")
    else:
        plt.show()
    plt.close()

def main():
    # 生成随机物体
    object_bboxes = generate_random_objects(num_objects=15)
    
    # 随机生成起点和目标点
    start_point = np.array([random.uniform(-6, 6), random.uniform(-6, 6)])
    obj_center = np.array([random.uniform(-6, 6), random.uniform(-6, 6)])
    
    # 绘制场景并保存在当前运行目录下
    import os
    current_dir = os.getcwd()
    output_path = os.path.join(current_dir, "draw_map.png")
    plot_2d_scene(object_bboxes, output_path=output_path, 
                 start_point=start_point, obj_center=obj_center)
    
    # 也可以直接显示而不保存
    # plot_2d_scene(object_bboxes, start_point=start_point, obj_center=obj_center)

if __name__ == '__main__':
    main()
