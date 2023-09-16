def remove_duplicates_from_list(array):
        duplicate_free_list = []
        for item in array:
            if item not in duplicate_free_list:
                duplicate_free_list.append(item)
        return duplicate_free_list

def merge_all_data(set1, set2): # merges all data without duplicates
    merged_set = set()
    for data in set1:
        merged_set.add(data)
    for data in set2:
        merged_set.add(data)
    return merged_set

def comma_seperated_string_to_set(string):
    return set(string.split(','))

def service_string_to_set(string):
    return set(string.split('\|'))