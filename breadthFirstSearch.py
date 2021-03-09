from queue import Queue


def breadth_first_search(problem):
    # a FIFO open_set
    open_set = Queue()
    # an empty set to maintain visited nodes
    closed_set = set()
    # a dictionary to maintain meta information (used for path formation)
    meta = dict()  # key -> (parent state, action to reach child)

    # initialize
    start = problem.get_start_state()
    meta[start] = (None, None)
    open_set.enqueue(start)

    while not open_set.is_empty():

        parent_state = open_set.dequeue()

        if problem.is_goal(parent_state):
            return construct_path(parent_state, meta)

        for (child_state, action) in problem.get_successors(parent_state):

            if child_state in closed_set:
                continue

            if child_state not in open_set:
                meta[child_state] = (parent_state, action)
                open_set.enqueue(child_state)

        closed_set.add(parent_state)


def construct_path(state, meta):
    action_list = list()

    while True:
        row = meta[state]
        if len(row) == 2:
            state = row[0]
            action = row[1]
            action_list.append(action)
        else:
            break

    return action_list.reverse()
