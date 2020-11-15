# Long term investment analysis
In order to determine if a company is a good investment, it's important to be able to effectively understand its quantitative prospects. The quantitative analysis is performed in "Quantitative analysis.ipynb" and automates the collection of essential data such as; market capitalisation, sales growth, eps growth, free cashflow growth and the yearly return on invested capital for shareholders. 

It then compares the chosen company against others within the same industry, before performing a basic growth forecast and discount cash flow analysis to determine the required growth rate for the company to be a feasible buy[1]. By knowing the required growth rate for the investment to be be profitable, the qualitative research can be better directed. 

The jupyter notebook scripts focus on forecasting the growth of a company over a one year period. By collecting the optimised indicators found by Nikola[2], the random forest classification model was able to determine if a company will grow by atleast 10% within the year. This model can then predict future instance.

Future considerations:
1. Using a better API, such as 'Financial modelling prep' to get current,rather than delayed, market data.
2. Building a larger database by collecting indicators for the same company in multiple year and repeating for all the companies within the market.
3. The collection of reports/articles, detailing the history of management. 

References
1. https://www.youtube.com/watch?v=P5sICGKnpwE&t=624s&ab_channel=HamishHodder
2. https://www.researchgate.net/publication/301847788_Equity_forecast_Predicting_long_term_stock_price_movement_using_machine_learning
