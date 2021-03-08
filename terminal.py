import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


COMMODITY = ['corn', 'soybean', 'crude oil', 'gasoline', 'natural gas']

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
	                	go.Scatter(x=data['Date'], y=data['50DMA'], line=dict(color='blue', width=1), name="50 DMA")])

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

option = st.selectbox(
    'Commodity',
     	COMMODITY)

'Daily Technicals: ', option

if option == 'corn':
	st.plotly_chart(price_chart(corn))

if option == 'soybean':
	st.plotly_chart(price_chart(soybean))

if option == 'crude oil':
	st.plotly_chart(price_chart(crude_oil))

if option == 'gasoline':
	st.plotly_chart(price_chart(gasoline))

if option == 'natural gas':
	st.plotly_chart(price_chart(natgas))
