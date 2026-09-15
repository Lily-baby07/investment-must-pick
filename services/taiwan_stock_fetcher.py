# -*- coding: utf-8 -*-

import random
from models.stock import Stock

class TaiwanStockDataFetcher:
    """台灣股票數據獲取服務"""
    
    def __init__(self):
        self.taiwan_stocks = {
            # 金融股
            '2330': {'name': '台積電', 'industry': '半導體'},
            '2412': {'name': '中華電', 'industry': '電信'},
            '2454': {'name': '聯發科', 'industry': '半導體'},
            '2882': {'name': '國泰金', 'industry': '金融'},
            '2891': {'name': '中信金', 'industry': '金融'},
            '2892': {'name': '第一金', 'industry': '金融'},
            '3008': {'name': '大立光', 'industry': '光學'},
            
            # 電子股
            '2317': {'name': '鴻海', 'industry': '電子'},
            '2303': {'name': '聯電', 'industry': '半導體'},
            '2308': {'name': '台達電', 'industry': '電源'},
            '2357': {'name': '華碩', 'industry': '電腦'},
            '2382': {'name': '廣達', 'industry': '電腦'},
            '2408': {'name': '南亞科', 'industry': '記憶體'},
            '2409': {'name': '友達', 'industry': '面板'},
            
            # 傳統產業
            '1101': {'name': '台泥', 'industry': '水泥'},
            '1102': {'name': '亞泥', 'industry': '水泥'},
            '1216': {'name': '統一', 'industry': '食品'},
            '1301': {'name': '台塑', 'industry': '塑化'},
            '1402': {'name': '遠東新', 'industry': '紡織'},
            '2105': {'name': '正新', 'industry': '輪胎'},
            
            # 其他
            '1590': {'name': '日月光', 'industry': '封測'},
            '2886': {'name': '兆豐金', 'industry': '金融'},
            '0050': {'name': '元大台灣50', 'industry': 'ETF'},
            '0056': {'name': '元大高股息', 'industry': 'ETF'},
        }
    
    def fetch_stock_data(self, stock_code):
        """獲取台灣股票數據"""
        if stock_code in self.taiwan_stocks:
            stock_info = self.taiwan_stocks[stock_code]
            stock = Stock(
                stock_code,
                stock_info['name'],
                price=random.uniform(20, 600),
                pe_ratio=random.uniform(8, 35),
                pb_ratio=random.uniform(0.5, 4),
                roe=random.uniform(0.05, 0.35)
            )
            stock.industry = stock_info['industry']
            stock.debt_ratio = random.uniform(0.2, 0.65)
            stock.current_ratio = random.uniform(0.8, 2.5)
            stock.cash_flow = random.randint(-500000, 5000000)
            stock.revenue_growth = random.uniform(-0.1, 0.3)
            return stock
        else:
            # 返回模擬數據
            return Stock(
                stock_code,
                f'股票_{stock_code}',
                price=random.uniform(20, 600),
                pe_ratio=random.uniform(8, 35),
                pb_ratio=random.uniform(0.5, 4),
                roe=random.uniform(0.05, 0.35)
            )
    
    def get_popular_stocks(self):
        """獲取熱門台灣股票列表"""
        popular = ['2330', '2454', '2317', '2882', '2891', '2412', '3008', '2303']
        return [self.fetch_stock_data(code) for code in popular]
    
    def get_stocks_by_industry(self, industry):
        """按行業獲取股票"""
        stocks = []
        for code, info in self.taiwan_stocks.items():
            if info['industry'] == industry:
                stocks.append(self.fetch_stock_data(code))
        return stocks
