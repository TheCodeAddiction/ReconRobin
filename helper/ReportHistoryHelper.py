from helper.data_helper import comma_seperated_string_to_set


def compare_report_data(new_data, old_data):

    new_data_set = new_data
    old_data_set = old_data

    new_data = new_data_set - old_data_set
    removed_data = old_data_set - new_data_set
    same_data = old_data_set.intersection(new_data_set)


    return [new_data, removed_data, same_data] # returns a list that we can loop through to get the data

