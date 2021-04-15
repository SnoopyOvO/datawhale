# import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
# # 1
# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))#read_file方法可以读取shape文件，转化为GeoSeries和GeoDataFrame数据类型。
# world.plot()#将GeoDataFrame变成图形展示出来，得到世界地图

# 2
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# # 利用name字段选择中国区域
# china = world.loc[world['name'].isin(['China', 'Taiwan'])]
# china.plot(color='red', alpha = 0.8)
# plt.show()
# 3
# import folium
# import webbrowser
# import os
# #首先，创建一张指定中心坐标的地图，这里将其中心坐标设置为北京。zoom_start表示初始地图的缩放尺寸，数值越大放大程度越大
# m=folium.Map(location=[39.9,116.4],zoom_start=10)
# m.save('f1.png')
# # webbrowser.open('f1.html')

