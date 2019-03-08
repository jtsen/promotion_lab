def calc_accuracy(predictions, labels):
    accuracy = {}
    counter, correct, wrong = 0, 0, 0
    for row in labels:
        if row == predictions[counter]:
            correct+=1
        else:
            wrong+=1
        counter+=1
    correct = str(correct/len(labels)) + '%'
    wrong = str(wrong/len(labels)) + '%'
    accuracy['Correct'] = correct
    accuracy['Wrong'] = wrong

    return accuracy

