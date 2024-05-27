# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 5


'''
Write a function that accepts a year between 1913 and 2013 inclusive 
and displays the maximum inflation during that year and the month(s) in which it was achieved.

Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    inflation = []
    with open('cpiai.csv') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if line[0][:4] == str(year):
                inflation.append(float(line[-1]))
    
    max_inflation = max(inflation)
    position = []
    for i in range(len(inflation)):
        if inflation[i] == max_inflation:
            position.append(months[i])

    print(f'In {year}, maximum inflation was: {max_inflation}')
    result = ', '.join(position)
    print(f'It was achieved in the following months: {result}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()