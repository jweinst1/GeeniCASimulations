#file for making grids

def MakeMatrix(w, l):
    assert w > 0 and l > 0
    return [[None for i in range(w)] for i in range(l)]

def customMatrix(w, l, value):
    assert w > 0 and l > 0
    return [[value for i in range(w)] for i in range(l)]