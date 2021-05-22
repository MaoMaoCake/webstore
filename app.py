from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/changepw")
def change_password():
    return render_template("changepw.html")


@app.route("/addmoney")
def add_money():
    return render_template("addmoney.html")


@app.route("/purchase")
def purchase():
    return render_template("purchase.html")


@app.route("/products")
def show_products():
    return render_template("products.html")


@app.route("/cart")
def show_cart():
    pass


if __name__ == '__main__':
    app.run()
