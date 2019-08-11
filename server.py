from flask import Flask
app = Flask(__name__)

import nextbus
import string
import threading
import time

class Times:
  def __init__(self):
    self.coming = set()
    self.in_transit = set()
    self.left_ts = dict()
    self.arrived_ts = dict()
    
  def update_times(self):
    old_coming = self.coming
    self.coming = {vid for _, vid, __ in nextbus.nextbus_stop_helper('sf-muni', 'L', '15419')}
    for vid in old_coming:
      if vid not in self.coming:
        self.left_ts[vid] = time.time()
        self.in_transit.add(vid)
    arriving = {vid for _, vid, __ in nextbus.nextbus_stop_helper('sf-muni', 'L', '15731')}
    for vid in in_transit:
      if vid not in arriving:
        self.in_transit.remove(vid)
        
        
  def debug(self):
    return "Coming: {}\nIn Transit: {}\nLeft: {}\n In Transit: {}\n".format(
      self.coming, self.in_transit, self.left_ts, self.arrived_ts)
        
TIMES = Times()
    

@app.route("/")
def hello():
  return TIMES.debug().replace("\n", "<br/>")

@app.route("/update-times", methods=["POST"])
def update_times():
  TIMES.update_times()
  return "Updated {}".format(TIMES.left_ts)

@app.route("/debug")
def debug():
  return TIMES.debug()

@app.route("/debug.html")
def debug_html():
  return TIMES.debug().replace("\n", "<br/>")
  

if __name__ == "__main__":
  app.run()
