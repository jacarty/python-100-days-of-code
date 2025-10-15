"""
What you'll learn today

    How to make time-series data comparable by resampling and converting to the same periodicity (e.g., from daily data to monthly data).

    Fine-tuning the styling of Matplotlib charts by using limits, labels, linestyles, markers, colours, and the chart's resolution.

    Using grids to help visually identify seasonality in a time series.

    Finding the number of missing and NaN values and how to locate NaN values in a DataFrame.

    How to work with Locators to better style the time axis on a chart

    Review the concepts learned in the previous three days and apply them to new datasets
"""

"""

What do the Search Numbers mean?

We can see from our DataFrames that Google's search interest ranges between 0 and 100. 
But what does that mean? Google defines the values of search interest as: 

    Numbers represent search interest relative to the highest point on the chart for the given region and time. 
    A value of 100 is the peak popularity for the term. 
    A value of 50 means that the term is half as popular. 
    A score of 0 means there was not enough data for this term. 

Basically, the actual search volume of a term is not publicly available. 
Google only offers a scaled number. 
Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity.

For each word in your search, Google finds how much search volume in each region 
and time period your term had relative to all the searches in that region and time period. 
It then combines all of these measures into a single measure of popularity, 
and then it scales the values across your topics, so the largest measure is set to 100. 
In short: Google Trends doesn’t exactly tell you how many searches occurred for your topic, 
but it does give you a nice proxy.

Here are the Google Trends Search Parameters that I used to generate the .csv data:

    "Tesla", Worldwide, Web Search

    "Bitcoin", Worldwide, News Search

    "Unemployment Benefits", United States, Web Search
"""

"""
In this lesson we looked at how to:

    How to use .describe() to quickly see some descriptive statistics at a glance.

    How to use .resample() to make a time-series data comparable to another by changing the periodicity.

    How to work with matplotlib.dates Locators to better style a timeline (e.g., an axis on a chart).

    How to find the number of NaN values with .isna().values.sum()

    How to change the resolution of a chart using the figure's dpi

    How to create dashed '--' and dotted '-.' lines using linestyles

    How to use different kinds of markers (e.g., 'o' or '^') on charts.

    Fine-tuning the styling of Matplotlib charts by using limits, labels, linewidth and colours (both in the form of named colours and HEX codes).

    Using .grid() to help visually identify seasonality in a time series.
   
"""