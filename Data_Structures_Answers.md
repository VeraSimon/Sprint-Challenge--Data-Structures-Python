Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method? O(n). We're recursing over every node in the tree to execute a lambda function. Mind you, the lambda function passed could add arbitrary extra runtime depending on what it implements in a given call, but that's outside the scope of the problem.

2. What is the space complexity of your `depth_first_for_each` function? O(c). Basically our only overhead here is the memory used for each instance of the BinarySearchTree initialized. Walking the tree with the recursion written does all callback operations in place.

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
