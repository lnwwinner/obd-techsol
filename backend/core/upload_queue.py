import time

class UploadQueue:

    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append({
            "data": data,
            "retry": 0
        })

    def process(self, send_func):
        for item in list(self.queue):
            try:
                send_func(item["data"])
                self.queue.remove(item)
            except Exception:
                item["retry"] += 1
                time.sleep(1)

    def size(self):
        return len(self.queue)
