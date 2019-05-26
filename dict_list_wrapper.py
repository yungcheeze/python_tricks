class DictListMemberWraper(object):
    """
    A class to make a list of dictionary act like a list of values

    e.g.
    l_of_d = [{"x": 10, "y":20}, {"x": 17, "y": 57}]
    xs = DictListMemberWraper(l_of_d, "x")
    print(xs[1]) # outputs 27
    """

    def __init__(self, dict_list, member):
        self.dict_list = dict_list
        self.member = member

    def __getitem__(self, index):
        return self.dict_list[index][self.member]

    def __len__(self):
        return self.dict_list.__len__()
