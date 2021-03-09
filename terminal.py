import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



COMMODITY = ['corn', 'soybean', 'crude oil', 'gasoline', 'natural gas']
OPTIONS = ['Price Charts', 'COT', 'Ending Stocks'] 

corn = pd.read_csv('corn.csv')
soybean = pd.read_csv('soybean.csv')
crude_oil = pd.read_csv('crude oil.csv')
gasoline = pd.read_csv('gasoline.csv')
natgas = pd.read_csv('natural gas.csv')


def price_chart(data): 
	fig = go.Figure(data=[go.Candlestick(x=data['Date'],
	                open=data['Open'],
	                high=data['High'],
	                low=data['Low'],
	                close=data['Settle']),
	                	go.Scatter(x=data['Date'], y=data['50DMA'], line=dict(color='blue', width=1), name="50 DMA"),
	                	go.Scatter(x=data['Date'], y=data['100DMA'], line=dict(color='black', width=1), name="100 DMA")])

	fig.update_layout(
	    title=' Daily Chart',
	    xaxis_title="Date",
	    yaxis_title="Price ($)",
	    font=dict(
	        family="Courier New, monospace",
	        size=12,
	        color="black"
	    )
	)

	fig.update_layout(showlegend=True)

	return fig

def rsi_chart(data): 
	fig = go.Figure(go.Scatter(x=data['Date'], y=data['RSI'], line=dict(color='black', width=1), name="RSI"))

	fig.add_shape(type='line',
                x0=min(data['Date']),
                y0=30,
                x1=max(data['Date']),
                y1=30,
                line=dict(color='Green',),
                xref='x',
                yref='y')

	fig.add_shape(type='line',
                x0=min(data['Date']),
                y0=70,
                x1=max(data['Date']),
                y1=70,
                line=dict(color='Red',),
                xref='x',
                yref='y')

	fig.update_layout(
	    title='RSI',
	    xaxis_title="Date",
	    yaxis_title="RSI",
	    font=dict(
	        family="Courier New, monospace",
	        size=12,
	        color="black"
	    )

	)

	fig.update_layout(showlegend=True)

	return fig


option = st.selectbox(
    'Commodity',
     	COMMODITY)

'Daily Technicals: ', option

if option == 'corn':
	st.plotly_chart(price_chart(corn))
	st.plotly_chart(rsi_chart(corn))

if option == 'soybean':
	st.plotly_chart(price_chart(soybean))
	st.plotly_chart(rsi_chart(soybean))

if option == 'crude oil':
	st.plotly_chart(price_chart(crude_oil))
	st.plotly_chart(rsi_chart(crude_oil))

if option == 'gasoline':
	st.plotly_chart(price_chart(gasoline))
	st.plotly_chart(rsi_chart(gasoline))

if option == 'natural gas':
	st.plotly_chart(price_chart(natgas))
	st.plotly_chart(rsi_chart(natgas))
