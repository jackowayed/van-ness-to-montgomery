from flask import Flask
app = Flask(__name__)

#import py_nextbus
import nextbus
import string
import threading
import time

NONCE = 0
#client = py_nextbus.NextBusClient(output_format='json', agency='sf-muni')

@app.route("/")
def hello():
  return "Hello World! {}".format(NONCE)

@app.route("/update-times", methods=["POST"])
def update_times():
  global NONCE
  NONCE += 1
  return "Updated {}".format(NONCE)

if __name__ == "__main__":
  app.run()
