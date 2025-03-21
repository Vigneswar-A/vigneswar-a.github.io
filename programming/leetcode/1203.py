class Foo:
    def __init__(self):
        self.f=threading.Lock()
        self.s=threading.Lock()
        self.f.acquire()
        self.s.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.f:
            printSecond()
        self.s.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.  
        with self.s:
            printThird()