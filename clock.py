''' clock execution'''
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == '__main__':

    sched = BlockingScheduler()

    @sched.scheduled_job('interval', seconds=30)
    def timed_job():
        subprocess.call('python -u replurk.py scheduler', shell=True, close_fds=True)

    sched.start()
