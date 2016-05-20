#file that contains grid making nodes

class GraphNode:

    def __init__(self, value=None, up=None, down=None, left=None, right=None):
        self.value = value
        self.up = up
        self.down = down
        self.left = left
        self.right = right

#makes a matrix of graph nodes
def graphmatrix(w, l):
    assert w > 0 and l > 0
    return [[GraphNode() for i in range(w)] for i in range(l)]