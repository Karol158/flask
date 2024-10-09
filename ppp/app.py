from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contas = []

@app.route('/')
def index():
    return render_template( "index.html", contas=contas)

@app.route('/criar', methods=["POST"])
def create():
    nome = request.form["nome"]
    email = request.form["email"]
    contas.append(nome)
    contas.append(email)
    return redirect("/")

@app.route('/alterar', methods=["POST"])
def update():
    old_name=request.form["old_name"]
    new_name=request.form["new_name"]
    old_email=request.form["old_email "]
    new_email=request.form["new_email"]
    if old_name in contas:
        index=contas.index(old_name)
        contas[index]=new_name
    if old_email in contas:
        index=contas.index(old_email)
        index=contas.index(new_email)
    return redirect("/")
@app.route('/deletar',methods=["POST"])
def delete():
    nome=request.form["name"]
    email=request.form["email"]
    if nome in contas:
        contas.remove(nome)
    if email in contas:
        contas.remove(email)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)