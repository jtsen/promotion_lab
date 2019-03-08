import dtree_build as dtree
import copy, csv


def get_predictions(list, test, tree, labels):
    headers = ['Instance', 'Actual', 'Predictions', 'Probability']
    list.append(copy.deepcopy(headers))
    counter = 0
    for rows in test:
        curr_row_pred = []
        pos_prob, neg_prob = 0, 0
        curr_prediction = dtree.classify(rows, tree)
        if curr_prediction.get(1.0) is not None:
            pos_prob = curr_prediction.get(1.0)
            pos_prob = float(pos_prob.replace('%', ''))

        if curr_prediction.get(0.0) is not None:
            neg_prob = curr_prediction.get(0.0)
            neg_prob = float(neg_prob.replace('%',''))

        if neg_prob > pos_prob:
            curr_row_pred.append(counter)
            curr_row_pred.append(labels[counter])
            curr_row_pred.append(0.0)
            curr_row_pred.append(neg_prob)
            list.append(copy.deepcopy(curr_row_pred))
            counter+=1
            curr_row_pred.clear()

        else:
            curr_row_pred.append(counter)
            curr_row_pred.append(labels[counter])
            curr_row_pred.append(1.0)
            curr_row_pred.append(pos_prob)
            list.append(copy.deepcopy(curr_row_pred))
            counter+=1
            curr_row_pred.clear()
    return list


def calc_accuracy(predictions, labels):
    accuracy = {}
    counter, correct, wrong = 1, 0, 0
    for row in labels:
        if row == predictions[counter][2]:
            correct+=1
        else:
            wrong+=1
        counter+=1
    correct = str(correct/len(labels)) + '%'
    wrong = str(wrong/len(labels)) + '%'
    accuracy['Correct'] = correct
    accuracy['Wrong'] = wrong

    return accuracy


def write_2d_list_to_csv(list):
    with open('dtree_results.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(list)
    csvFile.close()
    return 1

