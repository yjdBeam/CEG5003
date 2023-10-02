# we shall compute the mode(众数) for each attribute, which is the most frequent values of the attribute.
# For each data set feature, the most frequent value is set to true and remaining are false.
# task will be performed in both numerical and categorical data like below.
# this to accomplish the reliability of model output adopting to relevant attributes.

import numpy as np
from mlxtend.frequent_patterns import association_rules


def create_arm_data(data):
    """ Create the binary mode for the data
    Find the most frequent data point in an attribute"""
    columns = data.columns
    for col in columns:
        # find mode of a attribute and make the model value 1 and others 0
        data[col] = np.where(data[col] == data[col].mode().values[0], 1, 0)
    return data


def create_arm_rule(result):
    """Create association rule for the given apriori data set """
    rules = association_rules(result, metric="confidence", min_threshold=1)
    # sort in order of confidence and lift
    rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
    # find the length of antecedents & consequents
    rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
    rules["consequents_len"] = rules["consequents"].apply(lambda x: len(x))
    rules_list_sorted = []
    # iterate each row to add the both antecedents & consequents in single column set
    for x, y in rules.iterrows():
        rules_list_sorted.append(sorted(set(y.antecedents) | set(y.consequents)))
    rules['rules_set_sorted'] = rules_list_sorted
    rules["rules_len"] = rules["rules_set_sorted"].apply(lambda x: len(x))
    # sort the set and make it list
    rules['rules_sorted'] = rules.rules_set_sorted.apply(lambda x: ','.join(map(str, x)))
    return rules
