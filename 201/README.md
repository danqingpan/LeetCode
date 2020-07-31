# Priciple:
The problem tests how to implement topological sorting method.

## Solving steps:
1. Find courses with zero inlets. This is where we start.
2. Push them into a queue(collections.deque in python)
3. Count the inlet for each course
4. Pop a course from queue and add it to result.
5. Check adjacent courses. If an an adjacent course has zero inlet, push it into zero inlet queue. Else reduce the inlet count.
6. Run until the queue has no entities.
