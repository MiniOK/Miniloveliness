import threading
import time

# print(threading.active_count())  # 当前启动的线程数
# print(threading.current_thread())  # 当前启动的线程


def t1_job():
    print("t1  start\n")
    for i in range(10):
        time.sleep(0.1)
    print("t1  finish\n")


def t2_job():
    print('t2  start\n')
    print("t2  finish\n")


def main():
    """
    主要是检测 join（）方法  线程锁lock() 防止共享内存时的访问发生混乱
    使用 join（） 对控制多个线程的执行顺序非常关键
    看上面的方法 t1 的任务量比 t2 的大
    所以 t2 会比 t1 更快完成
    而且 我们不能忍受的是
        在 t2 还没运行完毕时  all done 执行了
        因此要使用 join 加以控制



    :return:
    """
    thread_1 = threading.Thread(target=t1_job, name='T1')  # 定义线程
    thread_2 = threading.Thread(target=t2_job, name='T2')
    thread_1.start()
    thread_1.join()
    thread_2.start()
    thread_2.join()

    print("all done\n")


if __name__ == '__main__':
    main()
