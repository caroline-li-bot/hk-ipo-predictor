import pandas as pd

# 读取数据
df_recent = pd.read_csv('ipo_full_data_2020_2025.csv')
df_historical = pd.read_csv('ipo_2020_2023_batch.csv')

# 合并数据
df_combined = pd.concat([df_recent, df_historical], ignore_index=True)

# 去重（按股票代码和上市日期）
df_combined = df_combined.drop_duplicates(subset=['股票代码', '上市日期'], keep='first')

# 按上市日期排序
df_combined['上市日期'] = pd.to_datetime(df_combined['上市日期'])
df_combined = df_combined.sort_values('上市日期', ascending=False).reset_index(drop=True)

# 保存合并后的数据
output_file = 'ipo_full_data_2020_2025_combined.csv'
df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"数据合并完成，总记录数：{len(df_combined)}")
print(f"时间范围：{df_combined['上市日期'].min().date()} 至 {df_combined['上市日期'].max().date()}")
print(f"合并后文件已保存为：{output_file}")

# 显示行业分布
print("\n行业分布：")
print(df_combined['行业'].value_counts())
