string_input = 'aaaskklkliiithtalal'
def pprint_string_counts(string_input):
    count_dict = {}
    for i in list(set(string_input)):
        count_dict[i]=string_input.count(i)
    for k, v in sorted(count_dict.items(), key = lambda x: x[1], reverse=True):
        print(k,' ',v)
pprint_string_counts(string_input)
