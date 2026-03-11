import akshare as ak
import pandas as pd
from datetime import datetime
import time

# 获取港股IPO数据
def fetch_hk_ipo_history():
    print("正在获取港股IPO历史数据...")
    
    try:
        # 获取港股新股列表
        ipo_df = ak.stock_hk_ipo_calendar()
        print(f"获取到 {len(ipo_df)} 条IPO记录")
        return ipo_df
    except Exception as e:
        print(f"获取IPO列表失败: {e}")
        return pd.DataFrame()

# 获取个股IPO详细信息
def fetch_ipo_detail(stock_code):
    try:
        # 去除.HK后缀
        code = stock_code.replace('.HK', '')
        # 获取发行信息
        detail = ak.stock_hk_ipo_info(symbol=code)
        time.sleep(0.5)  # 避免请求过快
        return detail
    except Exception as e:
        print(f"获取 {stock_code} 详情失败: {e}")
        return None

# 获取财务数据
def fetch_financial_data(stock_code):
    try:
        finance = ak.stock_financial_report_sina(stock=stock_code, symbol="现金流量表")
        time.sleep(0.5)
        return finance
    except Exception as e:
        print(f"获取 {stock_code} 财务数据失败: {e}")
        return None

if __name__ == "__main__":
    # 获取IPO列表
    ipo_list = fetch_hk_ipo_history()
    
    if not ipo_list.empty:
        # 保存原始数据
        output_file = f"hk_ipo_raw_{datetime.now().strftime('%Y%m%d')}.csv"
        ipo_list.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"原始IPO数据已保存到 {output_file}")
        
        # 显示前10条
        print("\n前10条记录：")
        print(ipo_list.head(10))
