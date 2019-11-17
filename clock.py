''' clock execution'''
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def time_stamp():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


if __name__ == '__main__':

    sched = BlockingScheduler()

    @sched.scheduled_job('interval', seconds=10)
    def timed_job():
        subprocess.call('python -u replurk.py scheduler', shell=True, close_fds=True)

    print(f"{time_stamp()} Start report\n")

    sched.start()

    print(f"{time_stamp()} End report\n")
