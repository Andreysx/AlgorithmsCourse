from bunary_tree import BinaryTree

tree_elements = [5, 10, 11, 8, 4, 1, 3, 2]
print_created_from = True
print_tree_len = True
print_tree = True
print_without_none_elements = True
print_removal_example = True
print_search_example = True

if print_created_from:
    print(f"Tree will be created from {tree_elements}")

bin_tree = BinaryTree()
for el in tree_elements:
    bin_tree.add(el)

if print_tree_len:
    print(f"Tree length is {len(bin_tree)}")
if print_tree:
    print("Current tree state:")
    bin_tree.print(filter_none=print_without_none_elements)
    print("Alternative tree print:")
    bin_tree.print(filter_none=not print_without_none_elements)
if print_removal_example:
    bin_tree.remove(10)
    print("Tree state after remove element with both children")
    bin_tree.print(filter_none=print_without_none_elements)
    bin_tree.remove(8)
    print("Tree state after remove element with one children")
    bin_tree.print(filter_none=print_without_none_elements)
    bin_tree.remove(2)
    print("Tree state after remove element without children")
    bin_tree.print(filter_none=print_without_none_elements)

if print_search_example:
    print(f"Result of search element that exist in tree: {bin_tree.search(4)}, type: {type(bin_tree.search(4))}")
    print(f"Result of search element that not exist in tree: {bin_tree.search(9)}")
