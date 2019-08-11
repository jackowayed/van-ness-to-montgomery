from flask import Flask
app = Flask(__name__)

import threading
import time

nonce = 0

@app.route("/")
def hello():
  return f"Hello World! {nonce}"

if __name__ == "__main__":
  app.run()
  
  
def update_times():
  nonce += 1

def update_times_recurring():
  update_times()
  time.sleep(20)