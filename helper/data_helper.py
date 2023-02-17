def remove_duplicates_from_list(array):
        duplicate_free_list = []
        for item in array:
            if item not in duplicate_free_list:
                duplicate_free_list.append(item)
        return duplicate_free_list
