import os
from flask import Flask, request, render_template, send_from_directory, jsonify
import histeq as h
import linear as l
import stdev as s
import logarithmic as log
import exp as e
import random

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def team():
    return render_template("team.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/enhance")
def perform():
    return render_template("enhance.html")

@app.route("/upload", methods=["POST"])
def upload():
    dest=None
    newfile=None
    target = os.path.join(APP_ROOT, 'static/input')
    enhancement=request.form['chooseenhancement']
    upload=request.files.get("file")
    filename = upload.filename
    newfilename=filename.split(".")[0]
    destination = "/".join([target, filename])
    upload.save(destination)
    dest='static/input/'+filename
    ran=random.randint(100,10000)
    if(enhancement=="linear"):
        l.linear(dest,1,ran)
        inphist='static/output/'+newfilename+str(ran)+"_linear_inp_hist.jpg"
        outimg='static/output/'+newfilename+str(ran)+"_linear_out_img.jpg"
        outhist='static/output/'+newfilename+str(ran)+"_linear_out_hist.jpg"
        enhancename="Linear"
    elif(enhancement=="stdev"):
        k=request.form['k']
        s.stdev(dest,1,ran,k)
        inphist='static/output/'+newfilename+str(ran)+"_stdev_inp_hist.jpg"
        outimg='static/output/'+newfilename+str(ran)+"_stdev_out_img.jpg"
        outhist='static/output/'+newfilename+str(ran)+"_stdev_out_hist.jpg"
        enhancename="Standard Deviation"
    elif(enhancement=="histeq"):
        h.histeq(dest,1,ran)
        inphist='static/output/'+newfilename+str(ran)+"_histeq_inp_hist.jpg"
        outimg='static/output/'+newfilename+str(ran)+"_histeq_out_img.jpg"
        outhist='static/output/'+newfilename+str(ran)+"_histeq_out_hist.jpg"
        enhancename="Histogram Equalization"
    elif(enhancement=="log"):
        log.log(dest,1,ran)
        inphist='static/output/'+newfilename+str(ran)+"_log_inp_hist.jpg"
        outimg='static/output/'+newfilename+str(ran)+"_log_out_img.jpg"
        outhist='static/output/'+newfilename+str(ran)+"_log_out_hist.jpg"
        enhancename="Logarithmic"
    else:
        g=request.form['g']
        e.exp(dest,1,ran,g)
        inphist='static/output/'+newfilename+str(ran)+"_exp_inp_hist.jpg/"
        outimg='static/output/'+newfilename+str(ran)+"_exp_out_img.jpg/"
        outhist='static/output/'+newfilename+str(ran)+"_exp_out_hist.jpg/"
        enhancename="Exponential"
    return render_template("enhance.html",inpimg=dest,outimg=outimg,inphist=inphist,outhist=outhist,enhancement=enhancename)

if __name__ == "__main__":
    app.run(debug=True)
