from flask import Flask,jsonify,request,render_template,url_for
from werkzeug.serving import WSGIRequestHandler
from yolov5.detect import run

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html",html_url=url_for('detect'))

@app.route('/detectobject',methods = ['POST','GET'])
def detect():

    img = request.files['file']
    img.save('images/temp.jpg')

    lines = run(weights='last_20_epoch.pt',source='images/temp.jpg',imgsz=640,save_txt=True,conf_thres=0.25,augment=True)
    print(lines)

    return jsonify(lines),200

if __name__ == "__main__":

    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded = True, host='0.0.0.0',port=8080)