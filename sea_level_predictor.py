import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig = df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', label='Original Data')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_vars = pd.Series(x for x in range(1880, 2051))
    y_vars = res.intercept +  res.slope*x_vars
    fig.plot(x_vars, y_vars, 'r')
    
    # Create second line of best fit
    newdf = df.copy()
    newYear = 2000
    newdf = newdf.loc[df['Year'] >= newYear]
    res = linregress(newdf['Year'], newdf['CSIRO Adjusted Sea Level'])
    x_vars = pd.Series(x for x in range(newYear, 2051))
    y_vars = res.intercept +  res.slope*x_vars
    fig.plot(x_vars, y_vars, 'r',)


    # Add labels and title
    fig.set_title('Rise in Sea Level')
    fig.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()