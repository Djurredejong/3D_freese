import time
import sys 

class Logger:
  def __init__(self, steps):
    self.start_time  = time.time()
    self.total_steps = steps
    self.current     = 0
    self.log_n_step  = 1

  def manual(self, string):
    sys.stdout.write("%s\n" % string)

  def step(self):
    self.current += 1
    if self.current % self.log_n_step == 0:
      self.log()

  def log(self):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write("%s/%s" % (self.current, self.total_steps))

  def done(self):
    total_time = time.time() - self.start_time
    per_step = total_time / self.total_steps
    sys.stdout.write("\nTime: %.1f sec. (%.3f sec/step)\n" % (total_time, per_step)) 
