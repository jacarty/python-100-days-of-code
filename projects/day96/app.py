"""
Stock Lookup Website using Marketstack API
"""

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv("../../.env")
MARKETSTACK_API_KEY = os.getenv("MARKETSTACK_API_KEY")

app = Flask(__name__)

# Marketstack API endpoint
MARKETSTACK_URL = "http://api.marketstack.com/v1/eod"

@app.route('/')
def index():
    """Main page with stock search form"""
    return render_template('index.html')

@app.route('/stock/<symbol>')
def get_stock(symbol):
    """
    Get stock data for a given symbol
    Returns JSON data for the stock
    """
    try:
        # Parameters for Marketstack API
        params = {
            'access_key': MARKETSTACK_API_KEY,
            'symbols': symbol.upper(),
            'limit': 5  # Get last 5 days of data
        }
        
        # Make API request
        response = requests.get(MARKETSTACK_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if we got data
        if 'data' not in data or len(data['data']) == 0:
            return jsonify({
                'error': f'No data found for symbol: {symbol.upper()}'
            }), 404
        
        # Process the stock data
        stock_data = data['data']
        latest = stock_data[0]
        
        # Calculate change if we have previous day data
        change = None
        change_percent = None
        if len(stock_data) > 1:
            previous = stock_data[1]
            change = latest['close'] - previous['close']
            change_percent = (change / previous['close']) * 100
        
        result = {
            'symbol': latest['symbol'],
            'date': latest['date'],
            'open': latest['open'],
            'high': latest['high'],
            'low': latest['low'],
            'close': latest['close'],
            'volume': latest['volume'],
            'change': change,
            'change_percent': change_percent,
            'history': stock_data
        }
        
        return jsonify(result)
    
    except requests.exceptions.RequestException as e:
        return jsonify({
            'error': f'API request failed: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/popular')
def popular_stocks():
    """Return a list of popular stock symbols"""
    popular = [
        {'symbol': 'AAPL', 'name': 'Apple Inc.'},
        {'symbol': 'MSFT', 'name': 'Microsoft Corporation'},
        {'symbol': 'GOOGL', 'name': 'Alphabet Inc.'},
        {'symbol': 'AMZN', 'name': 'Amazon.com Inc.'},
        {'symbol': 'TSLA', 'name': 'Tesla Inc.'},
        {'symbol': 'BKCG.L', 'name': 'Blockchain ETF.'},
        {'symbol': 'NVDA', 'name': 'NVIDIA Corporation'},
        {'symbol': 'JPM', 'name': 'JPMorgan Chase & Co.'}
    ]
    return jsonify(popular)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
