''' clock execution'''
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == '__main__':

    sched = BlockingScheduler()

    @sched.scheduled_job('interval', minutes=5)
    def timed_job():
        subprocess.call('python -u replurk.py >> replurk.log scheduler', shell=True, close_fds=True)

    sched.start()
