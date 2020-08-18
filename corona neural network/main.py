import graph.graph as g
import os
import xray.pred as x
import json
from flask import Flask, render_template, request, jsonify,make_response


app = Flask(__name__,template_folder='template')
app.config["IMAGE_UPLOADS"] = "C:/Users/waelh/Downloads/corona/corona/uploads/scan.png"
app.config["IMAGE"] = "C:/Users/waelh/Downloads/corona/corona/static"
@app.route('/')
def root():
   return render_template('TimeSliderChoropleth.html')
@app.route('/pred')
def pred():
   return render_template('pred.html')
@app.route('/upload')
def upload():
   return render_template('text.html')

@app.route('/uploader', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':

        f = request.files['image']
        f.save(os.path.join(app.config["IMAGE_UPLOADS"]))
        pr = x.Predict()
        result = pr.result(os.path.join(app.config["IMAGE_UPLOADS"]))
        return result
    else:
        return render_template('text.html')

@app.route('/output/confirmed')
def show_confirmed():
    filename = "confirmed.png"
    graph = g.Graph()
    res = graph.graph_confirmed()
    res.savefig(os.path.join(app.config["IMAGE"],filename))
    return render_template("image.html", filename=filename)

@app.route('/output/death')
def show_death():
    filename = "death.png"
    graph = g.Graph()
    res = graph.graph_death()
    res.savefig(os.path.join(app.config["IMAGE"],filename))
    return render_template("image.html", filename=filename) 

@app.route('/output/recovered')
def show_recovered():
    filename = "recovered.png"
    graph = g.Graph()
    res = graph.graph_recovered()
    res.savefig(os.path.join(app.config["IMAGE"],filename))
    return render_template("image.html", filename=filename) 


app.run(host = "127.0.0.1",port  = "5000")