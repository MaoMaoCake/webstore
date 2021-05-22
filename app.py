from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello World!'

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
def show_products():
    pass

@app.route("/products")
def show_products():
    pass

@app.route("/cart")
def show_products():
    pass

if __name__ == '__main__':
    app.run()
