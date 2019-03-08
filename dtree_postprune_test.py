import dtrree_preprocessing, dtree_draw, time, copy, dtree_evaluation
import dtree_build as dtree


def main(col_names=None):
    start = time.time()
    '''Open data file'''
    data = dtrree_preprocessing.open_csv_file('store_data_numerical.csv')


    '''Remove col #1 (CUSTOMER ID) and all headers'''
    data = dtrree_preprocessing.delete_col(data, 1)
    data.pop(0)


    '''Convert data to type: float'''
    data = dtrree_preprocessing.str_to_float(data)


    '''train/test split'''
    data_rows = len(data)
    train_split = int((data_rows/10)*8)
    train_set = copy.deepcopy(data[0:train_split])
    test_set = copy.deepcopy(data[train_split:])


    '''Preprocess: Sort each column to numerical intervals
                   Remove labels from test set
                   Create list of labels of test set'''
    cols_to_round = []
    for i in range(len(data[0])):
        cols_to_round.append(i+1)
    train_set = dtrree_preprocessing.sort_variance(train_set, cols_to_round)
    test_set = dtrree_preprocessing.sort_variance(test_set, cols_to_round)
    test_set_labels = copy.deepcopy(test_set)

    for rows in range(len(test_set)):
        del test_set[rows][-1]
    for rows in test_set_labels:
        for i in range(len(rows)-1):
            del rows[0]

    test_set_labels = [label for list in test_set_labels for label in list]


    '''Build decision tree and export pre-prune and post-prune 
       tree as JPEG and display post-pruned tree in console'''
    print("Total number of records = ", len(data))
    tree = dtree.buildtree(train_set, min_gain=0.001, min_samples=20)
    dtree_draw.drawtree(tree, jpeg='pre-prune.jpg')
    dtree.prune(tree, 0.1)
    dtree_draw.drawtree(tree, jpeg='post-prune.jpg')
    dtree.printtree(tree, '', col_names)
    max_tree_depth = dtree.max_depth(tree)
    print("max number of questions=" + str(max_tree_depth))


    '''Classify test set with the decision tree built and calculating the accuracy'''
    predictions = []
    predictions = dtree_evaluation.get_predictions(predictions, test_set, tree, test_set_labels)
    dtree_evaluation.write_2d_list_to_csv(predictions)
    accuracy = dtree_evaluation.calc_accuracy(predictions, test_set_labels)


    '''Print run-time and results (accuracy)'''
    end = time.time()
    print(accuracy)
    print("run-time: " + str(end-start))


if __name__ == "__main__":
    col_names = ['ZIP_CODE', 'TOTAL_VISITS', 'TOTAL_SPENT',
                 'AVRG_SPENT_PER_VISIT', 'HAS_CREDIT_CARD', 'PSWEATERS',
                 'PKNIT_TOPS', 'PKNIT_DRES', 'PBLOUSES',
                 'PJACKETS', 'PCAR_PNTS', 'PCAS_PNTS',
                 'PSHIRTS', 'PDRESSES', 'PSUITS', 'POUTERWEAR',
                 'PJEWELRY', 'PFASHION', 'PLEGWEAR', 'PCOLLSPND',
                 'AMSPEND', 'PSSPEND', 'CCSPEND', 'AXSPEND',
                 'SPEND_LAST_MONTH', 'SPEND_LAST_3MONTH', 'SPEND_LAST_6MONTH',
                 'SPENT_LAST_YEAR', 'GMP', 'PROMOS_ON_FILE',
                 'DAYS_ON_FILE', 'FREQ_DAYS', 'MARKDOWN', 'PRODUCT_CLASSES',
                 'COUPONS', 'STYLES', 'STORES', 'STORELOY',
                 'VALPHON', 'WEB', 'MAILED', 'RESPONDED', 'RESPONSERATE',
                 'LTFREDAY', 'CLUSTYPE', 'PERCRET', 'PERCRET',
                 'RESP']
    main(col_names)
