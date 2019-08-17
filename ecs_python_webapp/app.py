from flask import Flask
from flask import request
from functools import partial
from multiprocessing import Pool
from multiprocessing import cpu_count
import os
import socket
import time


app = Flask(__name__)

@app.route("/")
def hello():
    timenow = int(round(time.time() * 1000))

    html = "<h3>Welcome {name}!</h3>" \
           "<h4>EC2: {ec2}</h4>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Timestamp:</b> {timenow}"
    return html.format(name=os.getenv("NAME", "Boy"), ec2=os.getenv("EC2IP", "ec2 null"), hostname=socket.gethostname(), timenow=timenow)

@app.route("/app1")
def app1():
    timenow = int(round(time.time() * 1000))

    html = "<h3>APP1 Hello {name}!</h3>" \
           "<h4>EC2: {ec2}</h4>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Timestamp:</b> {timenow}"
    return html.format(name=os.getenv("NAME", "Boy"), ec2=os.getenv("EC2IP", "ec2 null"), hostname=socket.gethostname(), timenow=timenow)

@app.route('/app1/stress')
def stressApp1():
    timenow = int(round(time.time() * 1000))
    minutes = request.args.get('minutes', default = 0, type = int)
    processes = cpu_count()
    
    pool = Pool(processes)
    do_run = partial(run, y=minutes) # prod_x has only one argument x (y is fixed to 10) 
    pool.map_async(do_run, range(processes))

    html = "<h3>APP1 Hello {name}! Running load on CPU</h3>" \
           "<h4>EC2: {ec2}</h4>" \
           "<b>Hostname:</b> {hostname}<br/> <b>Timestamp:</b> {timenow} <br/>" \
           "<b>CPU Cores:</b> {cores}"
    return html.format(name=os.getenv("NAME", "Boy"), ec2=os.getenv("EC2IP", "ec2 null"), hostname=socket.gethostname(), timenow=timenow, cores=processes)

@app.route("/app2")
def app2():
    timenow = int(round(time.time() * 1000))

    html = "<h3>APP2 Hello {name}!</h3>" \
           "<h4>EC2: {ec2}</h4>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Timestamp:</b> {timenow}"
    return html.format(name=os.getenv("NAME", "Boy"), ec2=os.getenv("EC2IP", "ec2 null"), hostname=socket.gethostname(), timenow=timenow)

@app.route('/app2/stress')
def stressApp2():
    timenow = int(round(time.time() * 1000))
    minutes = request.args.get('minutes', default = 0, type = int)
    processes = cpu_count()
    
    pool = Pool(processes)
    do_run = partial(run, y=minutes) # prod_x has only one argument x (y is fixed to 10) 
    pool.map_async(do_run, range(processes))

    html = "<h3>APP2 Hello {name}! Running load on CPU</h3>" \
           "<h4>EC2: {ec2}</h4>" \
           "<b>Hostname:</b> {hostname}<br/> <b>Timestamp:</b> {timenow} <br/>" \
           "<b>CPU Cores:</b> {cores}"
    return html.format(name=os.getenv("NAME", "Boy"), ec2=os.getenv("EC2IP", "ec2 null"), hostname=socket.gethostname(), timenow=timenow, cores=processes)


def run(x, y):
    import time

    t_end = time.time() + 60 * y
    while time.time() < t_end:
        x*x

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
