import json

if __name__ == '__main__':
    # read the file normally
    with open('airlines.csv', 'r') as f:
        # header of the csv
        header = f.readline().rstrip().split(',')
        # print(header)
        out1_dict = dict()                                  # Output Dictionary
        for line in f.readlines():                          # loop over all the lines
            data = line.rstrip().split(',')                 # line split by comma saved into list
            name = ','.join(data[1:3])[1:-1]                # getting airport name
            out1_dict[name] = 1 + out1_dict.get(name, 0)    # filling up dictionary as hashmap

    # OUTPUT 1
    output_1 = json.dumps(out1_dict, indent=4)              # creating json object
    print('OUTPUT 1: Unique Airport Names & their Counts')
    print(output_1, '\n')

    # OUTPUT 2
    max_cnt_name = max(out1_dict, key=out1_dict.get)
    max_cnt = out1_dict[max_cnt_name]
    print('OUTPUT 3: Airport mentioned most number of times')
    print(f'Name: {max_cnt_name}\nCount: {max_cnt}\n')

    # OUTPUT 3
    min_cnt_name = min(out1_dict, key=out1_dict.get)
    min_cnt = out1_dict[min_cnt_name]
    print('OUTPUT 2: Airport mentioned least number of times')
    print(f'Name: {min_cnt_name}\nCount: {min_cnt}\n')
