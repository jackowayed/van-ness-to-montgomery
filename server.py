from flask import Flask
app = Flask(__name__)

#import py_nextbus
import nextbus
import string
import threading
import time

NONCE = 0
#client = py_nextbus.NextBusClient(output_format='json', agency='sf-muni')

class Times:
  def __init__(self):
    self.coming = set()
    self.in_transit = set()
    self.left_ts = dict()
    self.arrived_ts = dict()
    
  def update_times(self):
    old_coming = self.coming
    self.coming = [vid for _, vid, __ in nextbus.nextbus_stop_helper('sf-muni', 'L', '15419')]
    for vid in old_coming:
      if vid not in self.coming:
        self.left_ts[vid] = time.

@app.route("/")
def hello():
  outs = nextbus.nextbus_stop_helper('sf-muni', 'L', '15419')
  return "Hello World! {}\n{}".format(NONCE, outs)

@app.route("/update-times", methods=["POST"])
def update_times():
  global NONCE
  NONCE += 1
  return "Updated {}".format(NONCE)

if __name__ == "__main__":
  app.run()
