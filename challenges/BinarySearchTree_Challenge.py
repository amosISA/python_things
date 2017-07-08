# -*- coding: utf-8 -*-
"""
Un árbol binario de búsqueda(ABB) es un árbol binario con la propiedad de que 
todos los elementos almacenados en el subárbol izquierdo de cualquier nodo x 
son menores que el elemento almacenado en x ,y todos los elementos almacenados 
en el subárbol derecho de x son mayores que el elemento almacenado en x.

The Challenge

You are given a list of numbers stored in a list, A. Your challenge is to build a Binary Search Tree37 to store these numbers. You will need to:

Represent each node of the tree (including its data, left child, and right child).
Print the tree out in an understandable form.
Make a function to insert a list of numbers (A) into the tree.
Check if you can insert all the numbers in A into your tree, and that it prints out as expected.


Intermediate difficulty

Write a function to check if your created Binary Search Tree is balanced.


Hard Difficulty

Adapt your function to insert a list of n numbers so that it runs in O(n log n) time. Bear in mind that this is just the average case for a random sequence of numbers. If the list A was sorted it would take O(n^2).
Adapt your function to check if the tree is balanced so that it runs in O(n) time.

tagrockstar79958 answer from codeacademy!
"""
import random


class _Node(object):
    """
    node representation class. The node is fully handled by the BST 
    class and is not mean to be used outside of that context
    """

    """
    Here we keep track of how many nodes where added to the tree, 
    so that we can compare against the item count in the original
    numbers array.
    """
    created_node_count = 0

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

        _Node.created_node_count += 1

    def insert(self, value):
        """
        this method inserts a new node into the tree, if the value
        isn't already in the tree. The value trickles down the tree
        in a recursive manor.
        Greater values travels to right child and smaller travels to 
        left child.
        """

        if value == self.value:
            pass
        elif value > self.value:
            if self.right_child:
                self.right_child.insert(value)
            else:
                self.right_child = _Node(value)
        elif value < self.value:
            if self.left_child:
                self.left_child.insert(value)
            else:
                self.left_child = _Node(value)


class BST(object):
    """
    Represents the binary tree. This is the interface for interacting
    with the tree.
    """

    def __init__(self):
        self.root = None
        _Node.created_node_count = 0

    def insert(self, value):
        """
        If the root doesn't exist, one is created and the value passed to 
        it. Otherwise, this is where the recursive sorting of the values 
        is kick started
        """

        if not self.root:
            self.root = _Node(value)
        else:
            self.root.insert(value)

    def insert_array(self, value_array, start, end):

        self.insert_array_recursive(value_array, start, end)

        print('')
        print('%s values in the array and %s nodes created' % (len(value_array), self.root.created_node_count))

        if len(value_array) == self.root.created_node_count:
            print('The right amount of nodes have been inserted in the BST')
        else:
            print('An unexpected amount of nodes have been inserted in the BST')

    def insert_array_recursive(self, value_array, start, end):
        """
        This method is the key to creating a balanced tree. The value array must be sorted. 
        For each node that is created, the value of the median index of the current array
        segment [start:end], is picked. The segment to the left and right of the median index
        is passed to the left child  and right child respectively. 
        As the recursion progresses, the array is chopped into smaller and smaller segments,
        passed left and right depending on, on what side of the median index the segment
        happens to be. In the end, the segments contains just a single or no value and we 
        are done.
        """

        if start > end:
            return

        mid = int((start + end) / 2)

        self.insert(value_array[mid])
        self.insert_array_recursive(value_array, start, mid-1)
        self.insert_array_recursive(value_array, mid+1, end)

    def is_balanced(self):
        """
        I gather all the maximum depths of the tree recursively. 
        - If all depths are the same, the tree is balanced. 
        - If we have two different depths were the one is just +1 greater than the other, the tree is balanced
        - if we have more than two different depths, the tree is not balanced
        """

        depths = list()
        self._is_balanced_recursive(self.root, 0, depths)
        depths = list(set(sorted(depths)))
        print('Unique tree depths : %s' % depths)

        depths_count = len(depths)

        if 2 >= depths_count > 0:

            if depths_count == 2:
                if depths[0] + 1 == depths[1]:
                    return True
                else:
                    return False
            elif depths_count == 1:
                return True
            else:
                return False

    def _is_balanced_recursive(self, node, depth, depths):

        if node.left_child:
            self._is_balanced_recursive(node.left_child, depth+1, depths)
        else:
            depths.append(depth+1)

        if node.right_child:
            self._is_balanced_recursive(node.right_child, depth+1, depths)
        else:
            depths.append(depth + 1)

    def print_tree(self):

        depth_dict = dict()
        self._sort_by_depth(self.root, 1, depth_dict)

        print('')
        print('1 :  ' + '  ' * ((2**(len(depth_dict)-1))-1) + '%s' % self.root.value)

        for depth in sorted(depth_dict.keys()):

            if depth == len(depth_dict):
                break

            margin = (2 ** (len(depth_dict) - (depth+1)))-1
            spacer = (margin*2)+1

            values = list()

            for node in reversed(depth_dict[depth]):

                values.append(self._format_value(node.left_child))
                values.append(self._format_value(node.right_child))

            row = '%s :  ' % (depth + 1)

            print(row + ('  ' * margin) + ('  ' * spacer).join(values))

    def _sort_by_depth(self, node, depth, depth_dict):

        if not node:
            return

        depth_dict.setdefault(depth, list()).append(node)

        self._sort_by_depth(node.right_child, depth + 1, depth_dict)
        self._sort_by_depth(node.left_child, depth + 1, depth_dict)

    def _format_value(self, node):
        if node is None:
            return '--'

        if node.value < 10:
            return ' %s' % node.value

        elif node.value < 100:
            return '%s' % node.value


bst = BST()

array_length = random.randrange(20, 100)

"""" by converting to set I remove duplicate values"""
a = list(sorted(set([random.randrange(100) for x in range(array_length)])))

print(a)
print('')

bst.insert_array(a, 0, len(a)-1)
bst.print_tree()

print('')

if bst.is_balanced():
    print('The tree is balanced')
else:
    print('The tree is NOT balanced')







































































