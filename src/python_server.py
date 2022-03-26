import flask
app=flask.Flask("my-python-server")
@app.route("/")
def title():
    return "<html><head><title>Divya Project</title></head><body><h1>my server </body></html>"

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 8080)