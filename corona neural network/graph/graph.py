# importing the required libraries
import pandas as pd
# Visualisation libraries

from fbprophet import Prophet


# Disable warnings 
import warnings
warnings.filterwarnings('ignore')


class Graph():
    
    df = []

    def __init__(self):
        self.df = pd.read_csv('C:/Users/waelh/Downloads/corona/corona/graph/covid_19_clean_complete.csv',parse_dates=['Date'])
        self.df.rename(columns={'ObservationDate':'Date', 'Country/Region':'Country'}, inplace=True)

    def graph_confirmed(self):
        confirmed = self.df.groupby('Date').sum()['Confirmed'].reset_index()
        confirmed.columns = ['ds','y']
        confirmed['ds'] = pd.to_datetime(confirmed['ds'])
        m = Prophet(interval_width=0.95)
        m.fit(confirmed)
        futur = m.make_future_dataframe(periods=7)
        forecast = m.predict(futur)
        comp = m.plot_components(forecast)
        axes = comp.get_axes()
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Confirmed')
        return comp
        
    
    def graph_death(self):
        death = self.df.groupby('Date').sum()['Deaths'].reset_index()
        death.columns = ['ds','y']
        death['ds'] = pd.to_datetime(death['ds'])
        m = Prophet(interval_width=0.95)
        m.fit(death)
        futur = m.make_future_dataframe(periods=7)
        forecast = m.predict(futur)
        comp = m.plot_components(forecast)
        axes = comp.get_axes()
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Death')
        return comp
        
    def graph_recovered(self):
        recovered = self.df.groupby('Date').sum()['Recovered'].reset_index()
        recovered.columns = ['ds','y']
        recovered['ds'] = pd.to_datetime(recovered['ds'])
        m = Prophet(interval_width=0.95)
        m.fit(recovered)
        futur = m.make_future_dataframe(periods=7)
        forecast = m.predict(futur)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        comp  = m.plot_components(forecast)
        axes = comp.get_axes()
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Recovered')
        return comp
        
            
        
        
        