from flask import Flask
from cpn import cpn_gen


app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h3> central polygonal numbers sequence generator</h3>"


@app.route("/cpn/<int:num>")
def get_cpn(num):
    cpn = cpn_gen()
    return [next(cpn) for _ in range(num)]


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)