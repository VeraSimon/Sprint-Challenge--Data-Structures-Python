Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n). We're recursing over every node in the tree to execute a lambda function. Mind you, the lambda function passed could add arbitrary extra runtime depending on what it implements in a given call, but that's outside the scope of the problem.

2. What is the space complexity of your `depth_first_for_each` function?
O(c). Basically our only overhead here is the memory used for each instance of the BinarySearchTree initialized. Walking the tree with the recursion written does all callback operations in place.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
O(n^2). We have a simple nested for loop.

6. What is the space complexity of the provided code in `names.py`?
At worst, this would be O(n), where n is the length of the shorter file and all elements in it are also in the file being compared.

7. What is the runtime complexity of your optimized code in `names.py`?
For this data set, the runtime is O(n) on average (some duplicates), or O(n^2) for worst case (all elements are duplicates). Running in a couple thousandths of a second isn't too bad though. In addition to this, we have two O(n) items with the imports for each file, since each impotr goes through and generates a list containing every element of each file, but nothing's nested, so it's still O(n) on average.

8. What is the space complexity of your optimized code in `names.py`?
Still O(n) in the worst case of everything being a duplicate.
