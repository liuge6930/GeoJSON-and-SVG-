import geopandas as gpd
import os

# 1. 输入输出路径
input_file = r"D:\output\world.geojson"
output_file = r"D:\output\europe_countries.geojson"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# 2. 加载数据
world = gpd.read_file(input_file)

# 3. 调试：检查字段和法国记录
print("=== 调试信息 ===")
print("字段名:", world.columns.tolist())
print("法国记录（ISO_A3_EH）:\n", world[world['ISO_A3_EH'] == 'FRA'])
print("法国记录（NAME）:\n", world[world['NAME'] == 'France'])

# 4. 筛选欧洲国家
europe_iso_codes = ['AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE']
europe = world[world['ISO_A3_EH'].isin(europe_iso_codes)]

# 5. 验证筛选结果
print("筛选出的欧洲国家:", europe['NAME'].tolist())

# 6. 保存结果
if not europe.empty:
    europe.to_file(output_file, driver="GeoJSON")
    print(f"=== 结果 ===")
    print(f"筛选出 {len(europe)} 个欧洲国家")
    print(f"文件已保存至: {os.path.abspath(output_file)}")
else:
    print("错误：未筛选到任何欧洲国家！")