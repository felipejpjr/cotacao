from datetime import datetime
from yahoo_fin.stock_info import get_data, get_live_price, get_market_status

def getCotacaoStatus():
    cot = get_live_price("USDBRL=X")
    status = get_market_status()
    return (cot, status)

def getCotacaoYahoo():
    end = datetime.today()
    tesla_daily = get_data("USDBRL=X", start_date="01/01/2022", end_date = end, index_as_date = True, interval="1d")
    return (tesla_daily)

#cot, status = getCotacaoStatus()
#print(cot, status)
#print(getCotacaoYahoo())