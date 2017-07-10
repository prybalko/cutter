from cutter import app


@app.route("/")
def hello():
    return "Hello World!"
