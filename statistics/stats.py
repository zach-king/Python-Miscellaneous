import math


def entry():
    """Gets user inputted floats and returns them as a list"""
	l = []
	n = input('> ')
	while n != '-1':
		l.append(float(n))
		n = input('> ')
	return sorted(l)


def mean(lyst):
    """Returns the average, or mean, of a given list"""
	return sum(lyst) / len(lyst)


def median(lyst):
    """Returns the median of a given list"""
	l = len(lyst)
	if l % 2 == 0: 
		return (lyst[int(l/2)] + lyst[int(l/2)+1]) / 2
	else:
		return lyst[int(l/2)]


def variance(lyst):
    """Returns the sample variance for a given list"""
	n = (sum(lyst)**2) / len(lyst)
	n2 = sum([x**2 for x in lyst])
	return (n2 - n) / (len(lyst) - 1)


def stdDev(lyst):
    """Returns the sample standard deviation for a 
	given list."""
	return math.sqrt(variance(lyst))


def process(lyst):
    """Calculates the mean, median, variance, and 
	standard deviation for a given list of data."""
	print('Mean: ' + str(mean(lyst)))
	print('Median: ' + str(median(lyst)))
	print('Sample Variance: ' + str(variance(lyst)))
	print('Sample Std. Dev: ' + str(stdDev(lyst)))

