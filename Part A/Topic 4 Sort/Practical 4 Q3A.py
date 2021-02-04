def builtin_sort(words_list):
    h_list = []
    others_list = []


    for word in words_list:
        if word.startswith('H'):
            h_list.append(word)
        else:
            others_list.append(word)

    return sorted(h_list) + sorted(others_list)


# Test Code
words_list = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
print(builtin_sort(words_list))