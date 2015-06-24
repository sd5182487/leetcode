__author__ = 'Administrator'
def trans_palindrom(string):
#    if is_palindrom(string):
#        return string
    dict = {}
    res = []
    odd_count = 0
    for s in string:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    n = len(string)
    for d in dict:
        while dict[d] % 2 == 0 and dict[d] != 0:
            res.insert(0,d)
            res.append(d)
            dict[d] -= 2
        else:
            while dict[d] % 2 == 1:
                if dict[d] != 1:
                    res.insert(0,d)
                    res.append(d)
                    dict[d] -= 2
                else:
                    if odd_count == 0:
                        odd_count += 1
                        res.insert(len(res)/2,d)
                        dict[d] -= 1
                    else:
                        return -1

    return res