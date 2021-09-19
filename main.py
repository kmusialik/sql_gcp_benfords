#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:21:07 2021

@author: kmusial
"""

from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
app = Flask(__name__)

output = str()
celsius = str()


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/benfords_law", methods=['GET', 'POST'])
def benfords_law():
    if request.method == 'POST':  
       celsius = request.form['celsius']
       output = fahrenheit_from(celsius)
       if output[2] == 0:
           name_file = '0/' + output[1]
       if output[2] == 1:
           name_file = '1/' + output[1]
       if output[2] == 2:
           name_file = '2/' + output[1]
       if output[2] == 3:
           name_file = '3/' + output[1]
       if output[2] == 4:
           name_file = '4/' + output[1]
       if output[2] == 5:
           name_file = '5/' + output[1]
       if output[2] == 6:
           name_file = '6/' + output[1]  
       return render_template('wynik.html', usr=output[0], name=celsius, filename=name_file)
    else:
       return render_template("benfords_law.html",)


 
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        df = pd.read_csv('1_2020_total_6299_companies.csv', encoding='utf-8')
        #df = pd.read_csv('1_F-20_408_companies.csv')
        df_a = df[df.ticker_1 == celsius]
        
        #output = df_a.chi
        output = df_a.iloc[0]['chi']
        bucket = df_a.iloc[0]['bucket']
        #output = round(output, 1)
        filename = df_a.iloc[0]['company']
        #filename = filename.replace(' ', '_')
        filename = filename + '.png'
        print (output)
        print (filename)
        #fahrenheit = float(celsius) * 9 / 5 + 32
        #fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return [output, filename, bucket]
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)