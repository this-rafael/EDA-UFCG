from BST import BST

bst = BST()


while True:
    a = input()
    if a == "e": break
    bst.insert(int(a))

    print(bst.preOrder())

print(bst.max())
print(bst.min())

while True:
    a = input()
    if a == "e": break
    bst.remove(int(a))

    print(bst.preOrder())


