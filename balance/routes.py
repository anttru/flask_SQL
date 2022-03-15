from balance import app

@app.route("/")
def start():
    return "Working"

