import matplotlib.pyplot as plt
import pandas as pd
import warnings

import statsmodels.api as sm

dta = sm.datasets.sunspots.load_pandas().data[['SUNACTIVITY']]
dta.index = pd.date_range(start='1700', end='2009', freq='A')
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    res = sm.tsa.ARMA(dta, (3, 0)).fit(disp=0)
fig, ax = plt.subplots()
ax = dta.loc['1950':].plot(ax=ax)
res.plot_predict('1990', '2012', dynamic=True, ax=ax,
                 plot_insample=False)
