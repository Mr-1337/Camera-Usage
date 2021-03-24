import pandas
import numpy
from matplotlib import pyplot
import pprint
import re

dataset = pandas.read_excel('dataset.xlsx')
vars = ['What is your major?', 'What year are you?', 'What is your age?', 'How many live online classes are you currently taking?', 'Are you more likely to turn on your camera for a lecture, office hours, or peer meeting?', 'How often do you participate?(on)', 'How often do you participate?(off)','How often do you look at your phone or other distractions?(off)', 'How often do you look at your phone or other distractions?(on)']

def showCorrelation(variable, variable2, title):
    df = pandas.DataFrame({variable2.name : variable2, variable.name : variable})
    print('\nCorrelation:')
    print(variable.corr(variable2, method='pearson'))
    print('\n\n\n')
    df.plot.scatter(x=0, y=1)
    pyplot.title(title)
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

def countMeetReasons(variable):
    rows = [0,0,0,0]
    columns = [
        "Lecture",
        "Office Hours",
        "Peer Meeting",
        "No preference"
    ]
    i = 0
    for x in variable:             
        #check if x is valid
        if isinstance(x, str):
            for i in range(4):                    
                if re.search(columns[i], x):
                    rows[i] += 1
    df = pandas.DataFrame(rows, columns)
    print(df)
    pyplot.bar(columns, rows)
    pyplot.title('Where Students Prefer to Turn on Their Camera')
    pyplot.xlabel('Preference')
    pyplot.ylabel('Number of Occurances')
    pyplot.show()

def countNoCameraReasons(variable):
    rows = [0,0,0,0,0,0]
    columns = [
        "It makes you uncomfortable",
        "Presentation",
        "You don't have a camera",
        "Anxiety",
        "I always have my camera on!",
        "The camera is distracting"
    ]
    labels= [
        "Uncomfortable",
        "Presentation",
        "No Camera",
        "Anxiety",
        "Camera Is On",
        "Distracting"
    ]
    
    for x in variable:             
        #check if x is valid
         if isinstance(x, str):
            for i in range(6):                    
                if re.search(columns[i], x):
                    rows[i] += 1
    df = pandas.DataFrame(rows, columns)
    print(df)
    pyplot.figure(figsize=(15,9))
    pyplot.bar(columns, rows)
    pyplot.title('Reasons For Not Turning On Webcam')
    pyplot.ylabel('Number of Occurances')
    pyplot.xlabel('Reason')
    pyplot.xticks(range(6), labels)
    pyplot.show()

countNoCameraReasons(dataset["What might prevent you from turning on your camera?"])
countMeetReasons(dataset["Are you more likely to turn on your camera for a lecture, office hours, or peer meeting?"])

print(dataset[vars[0]])
calcMetrics(dataset[vars[2]])
dataset[vars[2]].hist()
pyplot.title('Number of Responses Based on Age')
pyplot.ylabel('Number of Responses')
pyplot.xlabel('Age')
pyplot.show()




calcMetrics(dataset[vars[3]])
printCategorical(dataset[vars[0]])
printCategorical(dataset[vars[1]])
dataset[vars[0]].hist()
pyplot.title('Number of Responses Based on Field of Study')
pyplot.xlabel('Number of Responses')
pyplot.ylabel('Fields of Study')
pyplot.show()
dataset[vars[1]].hist()
pyplot.title('Number of Responses Based on Year of Study')
pyplot.xlabel('Year of Study')
pyplot.ylabel('Number of Responses')
pyplot.show()
#printCategorical(dataset[vars[4]])
#dataset[vars[4]].hist();
#pyplot.title('untitled 3')
#pyplot.xlabel('')
#pyplot.ylabel('')
#pyplot.show()
calcMetrics(dataset[vars[5]])
dataset[vars[5]].hist(bins=range(1,7), align='left')
pyplot.title('Frequency of Participation with Camera On')
pyplot.xlabel('Scale: 1 = Very Infrequent Participation 5 = Very Frequent Participation')
pyplot.ylabel("Number of Responses")
pyplot.xticks(ticks = (1,2,3,4,5))
pyplot.show()

calcMetrics(dataset[vars[6]])
dataset[vars[6]].hist(bins=range(1,7), align='left')
pyplot.title('Frequency of Participation with Camera Off')
pyplot.xlabel('Scale: 1 = Very Infrequent Participation 5 = Very Frequent Participation')
pyplot.ylabel("Number of Responses")
pyplot.xticks(ticks = (1,2,3,4,5))
pyplot.show()

calcMetrics(dataset[vars[7]])
dataset[vars[7]].hist(bins=range(1,7), align='left')
pyplot.title('Frequency of Phone Use with Camera Off')
pyplot.xlabel('Scale: 1 = Very Infrequent Participation 5 = Very Frequent Participation')
pyplot.ylabel("Number of Responses")
pyplot.xticks(ticks = (1,2,3,4,5))
pyplot.show()

calcMetrics(dataset[vars[8]])
dataset[vars[8]].hist(bins=range(1,7), align='left')
pyplot.title('Frequency of Phone Use with Camera On')
pyplot.xlabel('Scale: 1 = Very Infrequent Participation 5 = Very Frequent Participation')
pyplot.ylabel("Number of Responses")
pyplot.xticks(ticks = (1,2,3,4,5))
pyplot.show()

y1 = dataset[vars[7]]
y2 = dataset[vars[8]]
fig, ax1 = pyplot.subplots()
ax1.hist([y1,y2],color=['b','g'], bins=range(1,7), label=['Camera Off','Camera On'], align='left')
ax1.set_xlim(1,5)
ax1.set_ylabel("Number of Responses")
ax1.set_xlabel("Scale: 1 = Very Phone Use 5 = Very Frequent Phone Use")
pyplot.tight_layout()
pyplot.legend(loc='upper right')
pyplot.xticks(ticks = (0,1,2,3,4,5,6))
pyplot.show()



showCorrelation(dataset[vars[6]], dataset[vars[2]], 'Camera Off Participation Corrilated to Respondants Age')
