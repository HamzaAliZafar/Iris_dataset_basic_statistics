import pandas as pd
from pandas.api.types import is_numeric_dtype
import math

data = pd.read_csv('iris.data', header=None)
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

print('Part 1')
for col in data.columns:
    if is_numeric_dtype(data[col]):
        print('%s:' % (col))
        print('\t Mean = %.2f' % data[col].mean())
        print('\t Standard deviation = %.2f' % data[col].std())
        print('\t Minimum = %.2f' % data[col].min())
        print('\t Maximum = %.2f' % data[col].max())
print(data['class'].value_counts())
print('Covariance:')
print(data.cov())
print('Correlation:')
print(data.corr())

# Class count function
def class_count(classes):
	dict = {}
	for i,x in enumerate(classes):
		if x not in dict.keys():
			dict[x] = 1
		else:
			dict[x] += 1
	print(dict)

# Mean function
def mean(name):
	sepal_length_sum = 0
	total = 0
	for ind,row in data.iterrows():
		sepal_length_sum += (row[name])
		total += 1

	mean_val = sepal_length_sum/total
	print('Mean of %s : %.2f'  % (name, mean_val))
	return mean_val

# Standard Deviation function
def std_dev(name, mean_val):
	sum_std = 0
	total = 0
	for ind,row in data.iterrows():
		sum_std += pow((row[name]) - mean_val, 2)
		total += 1

	std_val = math.sqrt((1/(total-1))*sum_std)
	print('Standard Deviation of %s : %.2f'  % (name, std_val))
	return std_val

# Covariance Function
def cov_fun(name1, name2, mean_val1, mean_val2):
	sum_cov = 0
	total = 0
	for ind,row in data.iterrows():
		sum_cov += (row[name1] - mean_val1)*(row[name2] - mean_val2)
		total += 1

	cov_val = (1/(total-1))*sum_cov
	print('Covariance of %s and %s : %.6f'  % (name1, name2, cov_val))
	return cov_val

#Correlation
def corr_fun(cov_val, std_val1, std_val2):
	corr_val = cov_val/(std_val1*std_val2)
	print('Correlation: ', corr_val)
	return corr_val

# Counting classes
print('\nPart 2')
class_count(data['class'])

# mean
print('\nPart 3')
mean_sepal_len = mean('sepal length')
mean_sepal_wid = mean('sepal width')
mean_petal_len = mean('petal length')
mean_petal_wid = mean('petal width')

#standard Deviation
print('\nPart 4')
std_sepal_len = std_dev('sepal length', mean_sepal_len)
std_sepal_wid = std_dev('sepal width', mean_sepal_wid)
std_petal_len = std_dev('petal length', mean_petal_len)
std_petal_wid = std_dev('petal width', mean_petal_wid)

# Covariance
print('\nPart 5')
cov_sepal_len_sepal_wid = cov_fun('sepal length', 'sepal width', mean_sepal_len, mean_sepal_wid)
cov_sepal_len_sepal_len = cov_fun('sepal length', 'sepal length', mean_sepal_len, mean_sepal_len)
cov_sepal_wid_sepal_len = cov_fun('sepal width', 'sepal length', mean_sepal_wid, mean_sepal_len)
cov_sepal_wid_sepal_wid = cov_fun('sepal width', 'sepal width', mean_sepal_wid, mean_sepal_wid)

print('\nPart 6')
corr__sepal_len_sepal_wid = corr_fun(cov_sepal_len_sepal_wid,std_sepal_len,std_sepal_wid)
corr__sepal_len_sepal_len = corr_fun(cov_sepal_len_sepal_len,std_sepal_len,std_sepal_len)
corr__sepal_wid_sepal_len = corr_fun(cov_sepal_wid_sepal_len,std_sepal_wid,std_sepal_len)
corr__sepal_wid_sepal_wid = corr_fun(cov_sepal_wid_sepal_wid,std_sepal_wid,std_sepal_wid)
