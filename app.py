from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])

def root():
    return render_template("form.html")


@app.route("/response", methods = ['GET','POST'])

def greeting():
    return render_template("greeting.html", method = request.method, username = request.form["data"])

if __name__ == '__main__':
    app.debug = True
    app.run()
