def create_queue(deque):
    return deque


def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    if queue:
        return queue.popleft()
    return None