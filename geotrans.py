import geopandas as gpd
import os

print("=== 脚本开始 ===")

# 1. 输入路径（Shapefile）
input_dir = r"D:\ne_10m_admin_0_countries"
input_shp = os.path.join(input_dir, "ne_10m_admin_0_countries.shp")
print(f"输入文件路径: {input_shp}")
print(f"文件是否存在: {os.path.exists(input_shp)}")

# 2. 检查Shapefile配套文件是否齐全
required_files = ['.shp', '.dbf', '.shx', '.prj']
missing_files = [ext for ext in required_files if not os.path.exists(input_shp.replace('.shp', ext))]
if missing_files:
    print(f"错误: 缺少配套文件: {missing_files}")
    exit()

# 3. 读取数据
try:
    world_data = gpd.read_file(input_shp)
    print("数据读取成功！字段名:", world_data.columns.tolist())
    print("示例数据（前5行）:\n", world_data[['NAME', 'ISO_A3']].head())
except Exception as e:
    print(f"读取失败: {e}")
    exit()

# 4. 输出路径
output_dir = r"D:\output"
output_path = os.path.join(output_dir, "world.geojson")
os.makedirs(output_dir, exist_ok=True)

# 5. 保存为GeoJSON
try:
    world_data.to_file(output_path, driver="GeoJSON")
    print(f"文件已生成: {output_path}")
    print(f"文件大小: {os.path.getsize(output_path)/1024:.2f} KB")  # 检查文件是否非空
except Exception as e:
    print(f"保存失败: {e}")




print("=== 脚本结束 ===")