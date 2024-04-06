from apscheduler.schedulers.blocking import BlockingScheduler


def pump_control(check_state):
    if check_state:
       print("running check_pump_state")

    print("sending command to pump")


if __name__ == '__main__':
  sched = BlockingScheduler()
  sched.add_job(pump_control, 'cron', args=[False], second='15,30,45')
  sched.add_job(pump_control, 'cron', args=[True], second='0')
  sched.start()
