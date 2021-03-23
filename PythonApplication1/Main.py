import pandas
import numpy
from matplotlib import pyplot
import pprint
import re

dataset = pandas.read_excel('dataset.xlsx')
vars = ['What is your major?', 'What year are you?', 'What is your age?', 'How many live online classes are you currently taking?']

def showCorrelation(variable):
    df = pandas.DataFrame({vars[4] : lifetimeImpressions, variable.name : variable})
    df.plot.scatter(x=0, y=1)
    pyplot.show()

def calcMetrics(variable):
    print('Variable Name: ' + variable.name)
    print('Mean: %.3f' % variable.mean())
    print('Median: %d' % variable.median())
    print('Std dev: %.3f' % variable.std())
    print('Variance: %.3f' % variable.var())
    print('Range: %d' % (variable.max() - variable.min()))
    print('Skewness: %.3f' % variable.skew())

    q1 = variable.quantile(0.25)
    q3 = variable.quantile(0.75)
    iqr = q3 - q1

    print('\n')
    print('Min: %d' % variable.min())
    print('Q1: %.3f' % q1)
    print('Q3: %.3f' % q3)
    print('IQR: %.3f' % iqr)
    print('Max: %d' % variable.max())
    print('\n')
    print('Outliers: \n')
    outliers = variable[(variable-variable.median()).abs() > (1.5 * iqr)].values
    print('Count: %d' % outliers.size)
    print('Values: ')
    print(outliers)
    print('\n\n\n')

def printCategorical(variable):
    print('Variable Name: ' + variable.name)
    variable = variable.astype("category")
    print(variable)
    print(variable.describe())
    pprint.pprint(variable.value_counts().to_dict(), width=1)

def countReasons(variable):
    rows = [0,0,0,0]
    columns = [
        "Lecture",
        "Office Hours",
        "Peer Meeting",
        "No preference"
    ]
    for x in variable:             
        #check if x is valid
        if isinstance(x, str):
            if re.search(columns[0], x):
                rows[0] += 1
            if re.search(columns[1], x): 
                rows[1] += 1
            if re.search(columns[2], x): 
                rows[2] += 1
            if re.search(columns[3], x): 
                rows[3] += 1
    df = pandas.DataFrame(rows, columns)
    print(df)
    pyplot.bar(columns, rows )
    pyplot.show()

calcMetrics(dataset[vars[3]])
printCategorical(dataset[vars[0]])
countReasons(dataset["Are you more likely to turn on your camera for a lecture, office hours, or peer meeting?"])