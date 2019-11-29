from nsetools import Nse
nse = Nse()
all_stocks1 = { '3MINDIA': '3M India Limited',
'ACC': 'ACC Limited',
'ASIANTILES': 'Asian Granito India Limited',
'ADANIENT': 'Adani Enterprises Limited',
'ADANIPORTS': 'Adani Ports and Special Economic Zone Limited',
'ADANIPOWER': 'Adani Power Limited',
'AMARAJABAT': 'Amara Raja Batteries Limited',
'AMBUJACEM': 'Ambuja Cements Limited',
'APOLLOHOSP': 'Apollo Hospitals Enterprise Limited',
'APOLLOTYRE': 'Apollo Tyres Limited',
'ASHOKLEY': 'Ashok Leyland Limited',
'ASIANPAINT': 'Asian Paints Limited',
'AUROPHARMA': 'Aurobindo Pharma Limited',
'AXISBANK': 'Axis Bank Limited',
'BAJAJ-AUTO': 'Bajaj Auto Limited',
'BAJAJFINSV': 'Bajaj Finserv Limited',
'BAJFINANCE': 'Bajaj Finance Limited',
'BALKRISIND': 'Balkrishna Industries Limited',
'BANKBARODA': 'Bank of Baroda',
'BANKINDIA': 'Bank of India',
'BATAINDIA': 'Bata India Limited',
'BEL': 'Bharat Electronics Limited',
'BERGEPAINT': 'Berger Paints (I) Limited',
'BHARATFORG': 'Bharat Forge Limited',
'BHARTIARTL': 'Bharti Airtel Limited',
'BHEL': 'Bharat Heavy Electricals Limited',
'BIOCON': 'Biocon Limited',
'BOSCHLTD': 'Bosch Limited',
'BPCL': 'Bharat Petroleum Corporation Limited',
'BRITANNIA': 'Britannia Industries Limited',
'CADILAHC': 'Cadila Healthcare Limited',
'CANBK': 'Canara Bank',
'CASTROLIND': 'Castrol India Limited',
'CENTURYTEX': 'Century Textiles & Industries Limited',
'CESC': 'CESC Limited',
'CHOLAFIN': 'Cholamandalam Investment and Finance Company Limited',
'CIPLA': 'Cipla Limited',
'COALINDIA': 'Coal India Limited',
'COLPAL': 'Colgate Palmolive (India) Limited',
'CONCOR': 'Container Corporation of India Limited',
'CUMMINSIND': 'Cummins India Limited',
'DABUR': 'Dabur India Limited',
'DISHTV': 'Dish TV India Limited',
'DLF': 'DLF Limited',
'DRREDDY': "Dr. Reddy's Laboratories Limited",
'EICHERMOT': 'Eicher Motors Limited',
'EQUITAS': 'Equitas Holdings Limited',
'ESCORTS': 'Escorts Limited',
'EXIDEIND': 'Exide Industries Limited',
'FEDERALBNK': 'The Federal Bank  Limited',
'GAIL': 'GAIL (India) Limited',
'GLENMARK': 'Glenmark Pharmaceuticals Limited',
'GMRINFRA': 'GMR Infrastructure Limited',
'GODREJCP': 'Godrej Consumer Products Limited',
'GRASIM': 'Grasim Industries Limited',
'HAVELLS': 'Havells India Limited',
'HCLTECH': 'HCL Technologies Limited',
'HDFC': 'Housing Development Finance Corporation Limited',
'HDFCBANK': 'HDFC Bank Limited',
'HEROMOTOCO': 'Hero MotoCorp Limited',
'HEXAWARE': 'Hexaware Technologies Limited',
'HINDALCO': 'Hindalco Industries Limited',
'HINDPETRO': 'Hindustan Petroleum Corporation Limited',
'HINDUNILVR': 'Hindustan Unilever Limited',
'IBULHSGFIN': 'Indiabulls Housing Finance Limited',
'ICICIBANK': 'ICICI Bank Limited',
'ICICIPRULI': 'ICICI Prudential Life Insurance Company Limited',
'IDEA': 'Vodafone Idea Limited',
'IDFCFIRSTB': 'IDFC First Bank Limited',
'IGL': 'Indraprastha Gas Limited',
'INDIGO': 'InterGlobe Aviation Limited',
'INDUSINDBK': 'IndusInd Bank Limited',
'INFRATEL': 'Bharti Infratel Limited',
'INFY': 'Infosys Limited',
'IOC': 'Indian Oil Corporation Limited',
'ITC': 'ITC Limited',
'JINDALSTEL': 'Jindal Steel & Power Limited',
'JSWSTEEL': 'JSW Steel Limited',
'JUBLFOOD': 'Jubilant Foodworks Limited',
'JUSTDIAL': 'Just Dial Limited',
'KOTAKBANK': 'Kotak Mahindra Bank Limited',
'L&TFH': 'L&T Finance Holdings Limited',
'LICHSGFIN': 'LIC Housing Finance Limited',
'LT': 'Larsen & Toubro Limited',
'LUPIN': 'Lupin Limited',
'M&M': 'Mahindra & Mahindra Limited',
'M&MFIN': 'Mahindra & Mahindra Financial Services Limited',
'MANAPPURAM': 'Manappuram Finance Limited',
'MARICO': 'Marico Limited',
'MARUTI': 'Maruti Suzuki India Limited',
'MCDOWELL-N': 'United Spirits Limited',
'MFSL': 'Max Financial Services Limited',
'MGL': 'Mahanagar Gas Limited',
'MINDTREE': 'MindTree Limited',
'MOTHERSUMI': 'Motherson Sumi Systems Limited',
'MRF': 'MRF Limited',
'MUTHOOTFIN': 'Muthoot Finance Limited',
'NATIONALUM': 'National Aluminium Company Limited',
'NBCC': 'NBCC (India) Limited',
'NCC': 'NCC Limited',
'NESTLEIND': 'Nestle India Limited',
'NIITTECH': 'NIIT Technologies Limited',
'NMDC': 'NMDC Limited',
'NTPC': 'NTPC Limited',
'OIL': 'Oil India Limited',
'ONGC': 'Oil & Natural Gas Corporation Limited',
'PAGEIND': 'Page Industries Limited',
'PEL': 'Piramal Enterprises Limited',
'PETRONET': 'Petronet LNG Limited',
'PFC': 'Power Finance Corporation Limited',
'PIDILITIND': 'Pidilite Industries Limited',
'PNB': 'Punjab National Bank',
'POWERGRID': 'Power Grid Corporation of India Limited',
'PVR': 'PVR Limited',
'RAMCOCEM': 'The Ramco Cements Limited',
'RBLBANK': 'RBL Bank Limited',
'RECLTD': 'REC Limited',
'RELIANCE': 'Reliance Industries Limited',
'SAIL': 'Steel Authority of India Limited',
'SBIN': 'State Bank of India',
'SHREECEM': 'SHREE CEMENT LIMITED',
'SIEMENS': 'Siemens Limited',
'SRF': 'SRF Limited',
'SRTRANSFIN': 'Shriram Transport Finance Company Limited',
'SUNPHARMA': 'Sun Pharmaceutical Industries Limited',
'SUNTV': 'Sun TV Network Limited',
'TATACHEM': 'Tata Chemicals Limited',
'TATAELXSI': 'Tata Elxsi Limited',
'TATAGLOBAL': 'Tata Global Beverages Limited',
'TATAMOTORS': 'Tata Motors Limited',
'TATAMTRDVR': 'Tata Motors Limited',
'TATAPOWER': 'Tata Power Company Limited',
'TATASTEEL': 'Tata Steel Limited',
'TCS': 'Tata Consultancy Services Limited',
'TECHM': 'Tech Mahindra Limited',
'TITAN': 'Titan Company Limited',
'TORNTPHARM': 'Torrent Pharmaceuticals Limited',
'TORNTPOWER': 'Torrent Power Limited',
'TVSMOTOR': 'TVS Motor Company Limited',
'UBL': 'United Breweries Limited',
'UJJIVAN': 'Ujjivan Financial Services Limited',
'ULTRACEMCO': 'UltraTech Cement Limited',
'UNIONBANK': 'Union Bank of India',
'UPL': 'UPL Limited',
'VEDL': 'Vedanta Limited',
'VOLTAS': 'Voltas Limited',
'WIPRO': 'Wipro Limited',
'YESBANK': 'Yes Bank Limited',
'ZEEL': 'Zee Entertainment Enterprises Limited'
}

import csv

#Creating files
def createFiles():
    print('CREATING FILES')
    keylist = ['date1', 'date2']
    q = nse.get_quote('infy')
    q['date1']=0 
    q['date2']=0 
    q['custom_MD_index']=0
    for key, value in all_stocks1.items() :
        with open(key+'.csv', 'w', newline='') as f:
            wr = csv.DictWriter(f, q.keys())
            wr.writeheader()

import time
import collections
from datetime import datetime
def process():
    for stock in all_stocks1:
        if nse.is_valid_code(stock) and stock != 'SYMBOL':
            time.sleep(1)
            print(stock)
            stock_info = nse.get_quote(stock)
            stock_info['date1']=0 
            stock_info['date2']=0 
            stock_info['custom_MD_index']=0
            ostock_info = collections.OrderedDict(sorted(stock_info.items()))
            print(ostock_info)
            #with open(stock+'.csv', 'w', newline='') as f:
            #    wr = csv.DictWriter(f, ostock_info.keys())
            #    wr.writeheader()
            buyQ = 0
            if stock_info['totalBuyQuantity']:
                buyQ = stock_info['totalBuyQuantity']
            sellQ = 0
            if stock_info['totalSellQuantity']:
                sellQ = stock_info['totalSellQuantity']
            buyP = 0
            if (buyQ+sellQ):
                buyP = ((buyQ)/(buyQ+sellQ))*100
            val = (buyP-50)*2
            ostock_info['date1'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            ostock_info['date2'] = datetime.timestamp(datetime.now())
            ostock_info['custom_MD_index']=val
            print(ostock_info['date1'])
            with open('/home/tejasp/PROK/'+stock+'.csv', 'a', newline='') as f:
                wr = csv.DictWriter(f, fieldnames=ostock_info.keys())
                wr.writerow(ostock_info)
            f.close()

process()

#q = nse.get_quote('infy')
#print(q)
#buyQ = q['buyQuantity1'] + q['buyQuantity2'] + q['buyQuantity3'] + q['buyQuantity4'] + q['buyQuantity5']
#sellQ = q['sellQuantity1'] + q['sellQuantity2'] + q['sellQuantity3'] + q['sellQuantity4'] + q['sellQuantity5']
#print(buyQ)
#print(sellQ)
