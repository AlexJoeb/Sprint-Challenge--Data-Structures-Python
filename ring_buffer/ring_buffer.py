class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.nextToReplace = 0

    def __len__(self):
        return len(self.storage)

    def append(self, item):
        if len(self) >= self.capacity:
            # At capacity. Now rotate.
            if self.nextToReplace >= len(self):
                self.nextToReplace = 0

            self.storage[self.nextToReplace] = item
            self.nextToReplace += 1
        else:
            self.storage.append(item)

    def get(self):
        return self.storage