from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("layout.html")


@app.route("/register")
def register():
    pass


@app.route("/login")
def login():
    pass


@app.route("/logout")
def logout():
    pass


@app.route("/changepw")
def change_password():
    pass


@app.route("/addmoney")
def add_money():
    pass


@app.route("/purchase")
def purchase():
    pass


@app.route("/products")
def show_products():
    pass


@app.route("/cart")
def show_cart():
    pass


if __name__ == '__main__':
    app.run()
