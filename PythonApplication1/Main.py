import pandas
import numpy
from matplotlib import pyplot
import pprint

dataset = pandas.read_excel('dataset.xlsx')
vars = ['What is your major?', 'What year are you?', 'What is your age?', 'How many live online classes are you currently taking?', 'Are you more likely to turn on your camera for a lecture, office hours, or peer meeting?', 'How often do you participate?(on)', 'How often do you participate?(off)']

def showCorrelation(variable, variable2):
    df = pandas.DataFrame({variable2.name : variable2, variable.name : variable})
    print('\nCorrelation:')
    print(variable.corr(variable2, method='pearson'))
    print('\n\n\n')
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


#print(dataset[vars[0]])
#calcMetrics(dataset[vars[2]])
#dataset[vars[2]].hist()
#pyplot.show()
#calcMetrics(dataset[vars[3]])
#printCategorical(dataset[vars[0]])
#printCategorical(dataset[vars[1]])
#dataset[vars[0]].hist()
#pyplot.show()
#dataset[vars[1]].hist()
#pyplot.show()
#printCategorical(dataset[vars[4]])
#dataset[vars[4]].hist();
#pyplot.show()
#calcMetrics(dataset[vars[5]])
#dataset[vars[5]].hist()
#pyplot.show()
#calcMetrics(dataset[vars[6]])
#dataset[vars[6]].hist()
#pyplot.show()

showCorrelation(dataset[vars[6]], dataset[vars[2]])