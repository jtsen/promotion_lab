import math
import numpy as np


def label_count(data):
    label_proportion = {'yes':0, 'no':0}
    for row in data:
        if row[len(row)-1] == 1:
            label_proportion['yes']+=1
        elif row[len(row)-1] == 0:
            label_proportion['no']+=1
    return label_proportion


def calc_categorical_conditional_prob(data, cols, dict, labels):
    for row in data:
        for num in cols:
            if row[num-1] not in dict[num].keys():
                key = row[num-1]
                if row[len(row)-1] == 1.0:
                    dict[num][key] = {1:1, 0:0}
                if row[len(row)-1] == 0.0:
                    dict[num][key] = {1:0, 0:1}
            elif row[num-1] in dict[num].keys():
                if row[len(row)-1] == 1.0:
                    dict[num][row[num-1]][1] += 1
                if row[len(row)-1] == 0.0:
                    dict[num][row[num-1]][0] += 1
    for num in cols:
        for key in dict[num].keys():
            dict[num][key][1] = dict[num][key][1]/labels.get('yes')
            dict[num][key][0] = dict[num][key][0]/labels.get('no')

    return dict


def calc_mu_variance(data, cols, dict):
    yes_sum, no_sum, yes_count, no_count = 0.0, 0.0, 0.0, 0.0
    yes_var, no_var = 0.0, 0.0
    for num in cols:
        for row in data:
            if row[len(row)-1] == 1:
                yes_sum += row[num-1]
                yes_count += 1
            elif row[len(row)-1] == 0:
                no_sum += row[num-1]
                no_count += 1
        yes_mu = yes_sum/yes_count
        no_mu = no_sum/no_count
        for row in data:
            if row[len(row)-1] == 1:
                yes_var += (row[num-1]-yes_mu)*(row[num-1]-yes_mu)
            elif row[len(row)-1] == 0:
                no_var += (row[num-1]-no_mu)*(row[num-1]-no_mu)
        yes_var = yes_var/(yes_count-1)
        no_var = no_var/(no_count-1)
        dict[num][1] = {'mu':yes_mu, 'var':yes_var}
        dict[num][0] = {'mu':no_mu, 'var':no_var}

    return dict


def classify_records(test, cond_probs, cat_list, num_list, probs):
    predictions = []
    for row in test:
        curr_probs = [math.log(probs[0]), math.log(probs[1])]
        for col in range(len(row)):
            if col == 0:
                continue
            if col in cat_list:
                try:
                    curr_probs[0] += math.log(cond_probs[col][row[col-1]][1])
                    curr_probs[1] += math.log(cond_probs[col][row[col-1]][0])
                except:
                    continue
            if col in num_list:
                try:
                    num_pos_cond = calc_numerical_cond(cond_probs[col][1]['var'], cond_probs[col][1]['mu'], row[col-1])
                    num_neg_cond = calc_numerical_cond(cond_probs[col][0]['var'], cond_probs[col][0]['mu'], row[col-1])
                    curr_probs[0]+=math.log(num_pos_cond)
                    curr_probs[1]+=math.log(num_neg_cond)
                except:
                    continue
        predictions.append(np.argmin(curr_probs))
        curr_probs.clear()
    return predictions


def calc_numerical_cond(var, mu, x):
    return 1/math.sqrt(2*math.pi*var)*math.exp(-(x-mu)**2/2*var**2)


