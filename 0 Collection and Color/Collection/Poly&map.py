import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature import COASTLINE, BORDERS
from matplotlib.collections import PolyCollection
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 5))
ax.add_feature(COASTLINE, linewidth=0.5)
ax.add_feature(BORDERS, linestyle=':', linewidth=0.5)

# 定义一些点的经纬度
polygons = [
    #
    [(0, 0), (30, 0), (45, 30), (20, 50),(0,40),(-10,30)],
    [(60, 0), (120, 0), (120, 45), (60, 45)],
    # 澳大利亚的点...
    [(114,-22),(121,-19),(126,-13.9),(127,-13.5),(129,-15),(132,-11.5),(136.8,-12.6),(135,-15),(140,-17.5),(143,-11),(145,-19),(150,-24),(154,-27),
     (152,-33),(145,-38),(139,-38),(134,-33),(128,-31),(124,-33.5),(116,-34.6),(115,-31),(113,-21.5),(117.4,-20)]

]
facecolor=['lightblue','#e45800','orange']
# 创建PolyCollection对象
pc = PolyCollection(polygons, facecolors=facecolor, edgecolors='k')
ax.add_collection(pc)
# 和下面的代码效果相同
# for polygon in polygons:
#     lons, lats = zip(*polygon)
#     ax.fill(lons, lats, facecolor=['lightblue','#e85800','orange'], edgecolor='k')
ax.set_extent([-180, 180, -90, 90])
ax.set_title('World Map')
plt.show()
