import threading

class MyThread():
    def __init__(self,work):
        self.event = threading.Event()
        self.thread = threading.Thread()
        self.work = work

    def start(self):
        self.event.clear()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.event.set()
        self.thread.join()
        
    def run(self):
        while not self.event.is_set():
            self.work()
    
class ThreadGroup:
    def __init__(self,list_threads):
        self.my_threads = list_threads

    def start(self):
        for thread in self.my_threads:
            thread.start()

    def stop(self):
        for thread in self.my_threads:
            thread.stop()