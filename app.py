from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

# Сначала открывается регистрация
@app.route("/")
def register_page():
    return render_template("register.html")


# После регистрации -> главная страница
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    users.append({
        "username": username,
        "email": email,
        "password": password
    })

    return redirect(url_for("home"))


# Главная страница
@app.route("/home")
def home():
    return render_template("index.html")


# Раздел машин
@app.route("/cars")
def cars():
    return render_template("cars.html")


# Раздел домов
@app.route("/houses")
def houses():
    return render_template("houses.html")


# Профиль
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)
