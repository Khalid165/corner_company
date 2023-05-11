from flask import Flask,render_template,redirect

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about-us")
def about_us():
    return render_template("about_us.html")

@app.route("/our-services")
def our_service():
    return render_template("our_services.html")

@app.route("/Privacy")
def privacy():
    return render_template("policy.html")


if __name__ == "__main__":
    app.run(debug=True)