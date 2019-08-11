from flask import Flask
app = Flask(__name__)

import collections
import nextbus
import string
import threading
import time

class Times:
  def __init__(self):
    self.coming = set()
    self.in_transit = set()
    self.left_ts = dict()
    self.times = collections.deque()
    
  def update_times(self):
    old_coming = self.coming
    self.coming = {vid for _, vid, __ in nextbus.nextbus_stop_helper('sf-muni', 'L', '15419')}
    for vid in old_coming:
      if vid not in self.coming:
        self.left_ts[vid] = time.time()
        self.in_transit.append(vid)
    arriving = {vid for _, vid, __ in nextbus.nextbus_stop_helper('sf-muni', 'L', '15731')}
    for vid in self.in_transit:
      if vid not in arriving:
        self.in_transit.remove(vid)
        if vid in left_ts:
          self.times.appendleft((time.time() - left_ts.pop(vid)) / 60)
        
        
        
  def debug(self):
    return "Coming: {}\nIn Transit: {}\nLeft: {}\nTimes: {}\n".format(
      self.coming, self.in_transit, self.left_ts, self.times)
        
TIMES = Times()
    

@app.route("/")
def times():
  return list(TIMES.times)[:10]

@app.route("/update-times", methods=["POST"])
def update_times():
  TIMES.update_times()
  return "Updated"

@app.route("/debug")
def debug():
  return TIMES.debug()

@app.route("/debug.html")
def debug_html():
  return TIMES.debug().replace("\n", "<br/>")
  

if __name__ == "__main__":
  app.run()
