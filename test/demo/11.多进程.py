import os
import random
import subprocess
import time
from multiprocessing import Pool, Process


# window下新建进程可使用Process
def run_proc(name):
    # 获取线程pid，如果要获取父进程使用os.getppid()
    print('The Child %s Process pid is %s, parent is %s' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print('开始..')
    p1 = Process(target=run_proc, args=('newProcess',))     # args传的是元组
    p1.start()
    p1.join()       # 进程p1执行完才执行下面的，多用于进程的同步
    print('结束..')


# 进程池
def run_pool_proc(name):
    print('run Task%s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('end Task%s (%s) - [ %s second ]' % (name, os.getpid(), end - start))


if __name__ == '__main__':
    print('Parent Process is %s' % (os.getpid(),))
    p = Pool(6)     # 创建进程池，总共6个线程
    for i in range(7):
        p.apply_async(run_pool_proc, args=(i,))     # 进程池运行run_pool_proc，总共运行了7次
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()                                        # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    time.sleep(1)                                  # 睡1s
    print('All subprocesses done.')

# 控制子进程的输入输出
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])     # 子进程调用nslookup www.python.org命令，并输出
print('Exit Code: ', r)