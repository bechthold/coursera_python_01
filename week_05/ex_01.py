#запускать через C:\cygwin64\bin\mintty.exe

#import time
#import os
#from multiprocessing import Process
#from threading import Thread
#from concurrent.futures import ThreadPoolExecutor, as_completed
    
#===============================================================================
# pid = os.fork()
# 
# if pid == 0:
#     while True:
#         print('child: ',os.getpid())
#         time.sleep(5)
# else:
#     print('parent: ', os.getpid())
#     os.wait()
#===============================================================================

#===============================================================================
# f = open('data.txt')
# foo = f.readline()
# 
# if os.fork() == 0:
#     foo = f.readline()
#     print('child: ', foo)
# else:
#     foo = f.readline()
#     print('parent: ', foo)
#===============================================================================

#===============================================================================
# def f(name):
#     print('Hello', name)
#  
# if __name__ == '__main__':            
#     p = Process(target=f, args=('Bob', ))
#     p.start()
#     p.join()
#===============================================================================

#===============================================================================
# class PrintProcessing(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         
#     def run(self):
#         print('Hello', self.name)
# if __name__ == '__main__':        
#     p = PrintProcessing('Mike')
#     p.start()
#     p.join()
#===============================================================================

#===============================================================================
# def f(name):
#     print('hello ', name)
#     
# if __name__ == '__main__':
#     th = Thread(target=f, args=('Bob', ))
#     th.start()
#     th.join()
#===============================================================================

#===============================================================================
# class PrintThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         
#     def run(self):
#         print('Hello ', self.name)
#         
# if __name__ == '__main__':
#     th =PrintThread('Mike')
#     th.start()
#     th.join()
#===============================================================================

#===============================================================================
# def f(a):
#     return a * a
# 
# if __name__ == '__main__':
#     with ThreadPoolExecutor(max_workers=3) as pool:
#         results = [pool.submit(f, i) for i in range(10)]
#         
#         for future in as_completed(results):
#             print(future.result())
#===============================================================================




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
