from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "Pathnex"
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": "Pathnex",
        "version": "1.0.0",
        "environment": "AWS EKS"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
