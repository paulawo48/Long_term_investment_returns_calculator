from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, numpy as np, matplotlib.pyplot as plt

tickername = input("Enter the stock ticker sysmbol: ").upper()
if len(tickername)<1:
    tickername = 'AAPL'

# Open connection to browser
options = webdriver.ChromeOptions()
options.add_argument("headless") 
browser = webdriver.Chrome(options= options)

def total_revenue():
    #Open broswer connection to url
    income_statement = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/income-statement' 
    # Open current the page 
    browser.get(income_statement)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    revenue_list = soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[0:6]
    revenue = []
    for i in revenue_list:
        revenue.append(float(''.join(i.text[1:].split(','))))
    return revenue

def eps():
    #Open broswer connection to url
    income_statement = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/income-statement' 
    # Open current the page 
    browser.get(income_statement)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    eps_2019 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[60].text[1:].split(',')))
    eps_2018 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[61].text[1:].split(',')))
    eps_2017 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[62].text[1:].split(',')))
    eps_2016 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[63].text[1:].split(',')))
    eps_2015 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[64].text[1:].split(',')))
    #Form EPS array
    eps = [eps_2019,eps_2018, eps_2017, eps_2016, eps_2015]
    return eps

def operating_cashflow():
    #Open broswer connection to url
    cash_flow = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/cash-flow-statement' 
    # Open current the page 
    browser.get(cash_flow)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    opcash_2019 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[0].text[1:].split(',')))
    opcash_2018 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[1].text[1:].split(',')))
    opcash_2017 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[2].text[1:].split(',')))
    opcash_2016 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[3].text[1:].split(',')))
    opcash_2015 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[4].text[1:].split(',')))
    #Form operating cashflow array
    opcash = [opcash_2019,opcash_2018, opcash_2017, opcash_2016, opcash_2015]
    return opcash

def equity():
    #Open broswer connection to url
    balance_sheet = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/balance-sheet' 
    # Open current the page 
    browser.get(balance_sheet)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    equity_2019 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[12].text[1:].split(',')))
    equity_2018 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[13].text[1:].split(',')))
    equity_2017 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[14].text[1:].split(',')))
    equity_2016 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[15].text[1:].split(',')))
    equity_2015 = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[16].text[1:].split(','))) 
    #Form equity array
    equity = [equity_2019,equity_2018, equity_2017, equity_2016, equity_2015]
    return equity

def pe_ratio():
    #Open broswer connection to url
    pe_ratio = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/pe-ratio' 
    # Open current the page 
    browser.get(pe_ratio)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    pe_2019 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[23].text)
    pe_2018 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[39].text)
    pe_2017 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[55].text)
    pe_2016 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[71].text)
    pe_2015 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[87].text)
    #Form Price-Earning ratio array
    pe = [pe_2019,pe_2018, pe_2017, pe_2016, pe_2015]
    return pe

def stock_price(): 
    #Open broswer connection to url
    pe_ratio = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/pe-ratio' 
    # Open current the page 
    browser.get(pe_ratio)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    stockprice_2019 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[21].text)
    stockprice_2018 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[37].text)
    stockprice_2017 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[53].text)
    stockprice_2016 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[69].text)
    stockprice_2015 = float(soup.find_all('td', attrs = {'style':'text-align:center;'})[85].text)
    #From price array
    price = [stockprice_2019,stockprice_2018, stockprice_2017, stockprice_2016, stockprice_2015]
    return price

def free_cash():
    #Open broswer connection to url
    free_cash = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/free-cash-flow' 
    # Open current the page 
    browser.get(free_cash)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    fc_2019 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[1].text.split(',')))
    fc_2018 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[3].text.split(',')))
    fc_2017 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[5].text.split(',')))
    fc_2016 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[7].text.split(',')))
    fc_2015 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[9].text.split(',')))
    # Form free cashflow array
    fc = [fc_2019,fc_2018, fc_2017, fc_2016, fc_2015]
    return fc

def maintenance_capex():
    #Open broswer connection to url
    ppe = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/net-change-in-property-plant-equipment' 
    # Open current the page 
    browser.get(ppe)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    ppe_2019 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:right'})[0].text[1:].split(',')))
    ppe_2018 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:right'})[1].text[1:].split(',')))
    ppe_2017 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:right'})[2].text[1:].split(',')))
    ppe_2016 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:right'})[3].text[1:].split(',')))
    ppe_2015 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:right'})[4].text[1:].split(',')))
    #Form PPE array
    ppe = [ppe_2019, ppe_2018,ppe_2017, ppe_2016, ppe_2015]
    revenue = total_revenue()
    #Calculate change in revenue YOY/capex
    opcash = operating_cashflow()
    freecash = free_cash()
    capex = []
    sales_growth = []
    for i in range(0,5):
        sales_growth.append(revenue[i]-revenue[i+1])
        capex.append(opcash[i]-freecash[i])
    #Calculate ppe as a % of sales
    ppe_sales = []
    for (v,k) in zip(ppe, revenue): 
        ppe_sales.append(abs(v)/k)
    #Calculating maintenance capex
    mcap = []
    for i in range(0,5):
        mcap.append(abs(ppe_sales[i]*sales_growth[i]-capex[i]))
    return mcap

def cashflow_for_owner():
    opcash = operating_cashflow()
    mcap = maintenance_capex()
    cash = []
    for i in range(0,5):
        cash.append(opcash[i]-mcap[i])
    return cash

def total_liabilities():
    #Open broswer connection to url
    balance_sheet = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/balance-sheet' 
    # Open current the page 
    browser.get(balance_sheet)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    total_liabilities = float(''.join(soup.find_all('div', attrs = {'style':'font-weight:bold; text-align:right; margin-top:5px; margin-right:4px;'})[6].text[1:].split(',')))
    return total_liabilities 

def current_liabilities():
    #Open broswer connection to url
    current_lia = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/total-current-liabilities' 
    # Open current the page 
    browser.get(current_lia)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    liabilities = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[1].text[1:].split(',')))
    return liabilities

def current_asset():
    #Open broswer connection to url
    current_asset = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/total-current-assets' 
    # Open current the page 
    browser.get(current_asset)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    assets = int(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[1].text[1:].split(',')))
    return assets

def long_term_debt():
    #Open broswer connection to url
    lt_debt = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/long-term-debt' 
    # Open current the page 
    browser.get(lt_debt)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    try:
        ltdebt_2019 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[1].text[1:].split(',')))
        ltdebt_2018 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[3].text[1:].split(',')))
        ltdebt_2017 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[5].text[1:].split(',')))
        ltdebt_2016 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[7].text[1:].split(',')))
        ltdebt_2015 = float(''.join(soup.find_all('td', attrs = {'style':'text-align:center'})[9].text[1:].split(',')))
    except:
        ltdebt_2019 = 0
        ltdebt_2018 = 0
        ltdebt_2017 = 0
        ltdebt_2016 = 0
        ltdebt_2015 = 0
    #Form long term debt array
    ltdebt = [ltdebt_2019, ltdebt_2018, ltdebt_2017, ltdebt_2016, ltdebt_2015]
    return ltdebt

def outstanding_share():
    #Open broswer connection to url
    shares_out = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/shares-outstanding' 
    # Open current the page 
    browser.get(shares_out)
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    outstanding_shares = float(soup.find('strong').text[:-1])*1000
    return outstanding_shares

def current_price():
    #Open broswer connection to url
    current_price = 'https://www.macrotrends.net/stocks/charts/'+ tickername + '/' +tickername +'/stock-price-history' 
    # Open current the page 
    browser.get(current_price) 
    #Give source code to BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Get JavaScript info from site
    price = soup.find('strong').text
    return price

def growth_analysis():
    # PE Ratio averages
    pe = pe_ratio()
    five_year_high = max(pe)
    five_year_low = min(pe)
    five_year_avg = sum(pe)/len(pe)
    analysis = [five_year_high,five_year_avg,five_year_low]

    #Plot conditional formatted barchart showing PE Ratio
    label1 = ['Five year high','Five year average','Five year low']
    x1 = np.arange(len(label1))
    width = 0.35
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.bar(x1-width,analysis,width,label ='PE Ratio Analysis', align = 'edge')
    #Add some text for labels
    ax1.set_ylabel('Percentage(%)')
    ax1.set_title('PE Analysis')
    ax1.set_xticks(x1)
    ax1.set_xticklabels(label1)
    ax1.legend()

    # Debt ratios
    curr_asset = float(current_price())
    curr_liabilities = float(current_liabilities())
    tot_liab = total_liabilities()
    equi = equity()
    current_ratio = curr_asset/curr_liabilities
    debt_equi_ratio = tot_liab/equi[0]
    ratio = [current_ratio, debt_equi_ratio]
    #Plot conditional formatted barchart showing PE Ratio
    label2 = ['Current ratio','Debt-to-equity ratio']
    x2 = np.arange(len(label2))
    ax2.bar(x2-width,ratio,width,label ='Debt Analysis', align = 'edge')
    #Add some text for labels
    ax2.set_ylabel('Percentage(%)')
    ax2.set_title('Debt analysis Analysis')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(label2)
    ax2.legend()

    #Calculating ROIC
    cffo = cashflow_for_owner()
    ltdebt = long_term_debt()
    roic = []
    for i in range(5):
        roic.append(100*cffo[i]/(equi[i]+ltdebt[i]))
    #Plot conditional formatted barchart showing PE Ratio
    label3 = ['2019','2018','2017','2016','2015']
    x3 = np.arange(len(label3))
    ax3.plot(label3,roic)
    #Add some text for labels
    ax3.set_ylabel('Percentage(%)')
    ax3.set_title('Return on invested capital')
    ax3.set_xticks(x3)
    ax3.set_xticklabels(label3)
    ax3.legend()
    
    # Analysing ROIC
    roic_1 = roic[0]
    roic_5 = sum(roic)/len(roic)
    # Average rate of growth
    revenue = total_revenue()
    earning_ps = eps()
    sales_1 = np.rate(1,[0],pv=-revenue[1],fv=revenue[0])*100
    sales_3 = np.rate(3,[0],pv=-revenue[3],fv=revenue[0])*100
    sales_4 = np.rate(4,[0],pv=-revenue[4],fv=revenue[0])*100
    sales_combine = [sales_1, sales_3, sales_4]
    eps_1 = np.rate(1,[0],pv=-earning_ps[1],fv=earning_ps[0])*100
    eps_3 = np.rate(3,[0],pv=-earning_ps[3],fv=earning_ps[0])*100
    eps_4 = np.rate(4,[0],pv=-earning_ps[4],fv=earning_ps[0])*100
    eps_combine= [eps_1,eps_3, eps_4]
    equity_1 = np.rate(1,[0],pv=-equi[1],fv=equi[0])*100
    equity_3 = np.rate(3,[0],pv=-equi[3],fv=equi[0])*100
    equity_4 = np.rate(4,[0],pv=-equi[4],fv=equi[0])*100
    equi_combine = [equity_1, equity_3,equity_4]
    cfs_1 = np.rate(1,[0],pv=-cffo[1],fv=cffo[0])*100
    cfs_3 = np.rate(3,[0],pv=-cffo[2],fv=cffo[0])*100
    cfs_4 = np.rate(4,[0],pv=-cffo[4],fv=cffo[0])*100
    cfs_combine = [cfs_1,cfs_3, cfs_4]
    label = ['1 year','3 year', '4 year']

    # #Plot line graph
    ax4.plot(label, sales_combine, 'r-',label='Sales')
    ax4.plot(label,eps_combine, 'b-',label='EPS')
    ax4.plot(label,equi_combine,'g-', label = 'Equity')
    ax4.plot(label,cfs_combine, 'y-',label ='Cashflow for Owners')
    ax4.set_title('Growth forecast')
    ax4.set_ylabel('Percentage(%)')
    ax4.legend()
    plt.show()
    
def discounted_cf():
    #Input data on the company
    rror = float(input('Enter the porfolio required rate of return(%):'))
    tgr = float(input('Enter the terminal growth rate(%):')) 
    growth_rate = float(input('Enter inital growth rate:'))
    #Calculate the buy price per share using NPV
    def buypershare():
        y1 = y0*(1+0.01*growth_rate)
        y2 = y1*(1+0.01*growth_rate)
        y3 = y2*(1+0.01*growth_rate)
        y4 = y3*(1+0.01*growth_rate) 
        y5 = y4*(1+0.01*growth_rate)
        y6 = y5*(1+0.01*growth_rate)
        y7 = y6*(1+0.01*growth_rate)
        y8 = y7*(1+0.01*growth_rate)
        y9 = y8*(1+0.01*growth_rate)
        y10 = y9*(1+0.01*growth_rate)
        cashflow = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]

        terminal_buy = (y10*(1+0.01*tgr))/(0.01*(rror-tgr))
        cashflow.append(terminal_buy)
        buy_price = np.npv(rror*0.01,cashflow)
        buy_pershare = buy_price/(outstanding_share())
        return buy_pershare
    #Using steepest gradient descent to determine otpimal growth rate
    y0 = cashflow_for_owner()[0]
    share_price = float(current_price())
    buy_pershare = float(buypershare())
    while round(share_price,1) != round(buy_pershare,1):
        if int(share_price) > int(buy_pershare):
            growth_rate += 0.05
            buy_pershare = buypershare()
        elif int(share_price) < int(buy_pershare):
            growth_rate -= 0.05
            buy_pershare = buypershare()
    print("The required growth rate at current price is:", growth_rate)

if __name__ == "__main__":
    growth_analysis()
    browser.close()
    discounted_cf()