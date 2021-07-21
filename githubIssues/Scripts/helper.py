def bubble_sort(list):
    '''
    bubblesort elements without being case sensitive
    '''
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j][1].capitalize() > list[j + 1][1].capitalize():
                # sorting by using simultaneous assignment in python
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def json_format(list):

    json_format = {"result": []}
    for i in range(len(list)):
        json_format["result"].append({"number": list[i][0],
                                      "title": list[i][1]})
    return json_format
