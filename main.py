from flask import Flask,render_template,redirect

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/about-us")
def about_us():
    return render_template("Page-4.html")

@app.route("/our-services")
def our_service():
    return render_template("Page-2.html")

@app.route("/Privacy")
def privacy():
    return render_template("Page-1.html")


if __name__ == "__main__":
    app.run(debug=True)