# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    node_order = list()
    node_store = set()
    prev_id, _id = None, None
    while 1:
        prev_id = _id
        _id = id(node)
        if _id in node_store:
            return node_order.index(prev_id) - node_order.index(_id) + 1
        node_store.add(_id)
        node_order.append(_id)
        node = node.next
        
