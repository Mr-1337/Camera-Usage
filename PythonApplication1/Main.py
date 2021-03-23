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
    print('\nCorrelation:')
    print(variable.corr(lifetimeImpressions, method='pearson'))
    print('\n\n\n')

