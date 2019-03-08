import nb_build, time
from nb_preprocessing import *
from nb_evaluation import *


start = time.time()
'''Importing dataset and remove headers'''
data = open_csv_file(r'C:\Users\stalk\PycharmProjects\NBClassifier\store_data.csv')
data = prob_round(str_to_float(delete_col(data, 1)))


'''Calculating probabilities'''
label_counts = nb_build.label_count(data)
total_count_labels = sum(label_counts.values())
prob_yes = label_counts.get('yes') / total_count_labels
prob_no = label_counts.get('no') / total_count_labels
prob_list = [prob_yes, prob_no]


'''Creating train/test sets'''
data_rows = len(data)
train_split = int((data_rows / 10) * 9)
test_split = len(data) - train_split
train_set = bootstrap_sampling(data, rows=train_split)
test_set = bootstrap_sampling(data, rows=test_split)
test_set_labels = get_col(test_set,47)


'''Creating lists of cols for storing conditional probabilities, mu, 
   and variance (numerical attribute)'''
categorical_cols = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 29, 33, 34, 35, 37, 39, 40, 41, 42, 45]
numerical_cols = []
for i in range(len(train_set[0])+1):
    if i == 0:
        continue
    if i not in categorical_cols:
        numerical_cols.append(i)
numerical_cols.pop()


'''Creating nested dict: keys = column number (starting from 1)
                         values = dictionary'''
cols_vars = dict()
for col in range(len(train_set[0])-1):
    cols_vars[col+1] = {}


'''Calculate conditional probabilities, mu, and variance'''
cols_vars = nb_build.calc_categorical_conditional_prob(train_set, categorical_cols, cols_vars, label_counts)
cols_vars = nb_build.calc_mu_variance(train_set, numerical_cols, cols_vars)

'''Classify and Calculate Accuracy'''
predictions = nb_build.classify_records(test_set, cols_vars, categorical_cols, numerical_cols, prob_list)
accuracy = calc_accuracy(predictions, test_set_labels)
print(accuracy)


