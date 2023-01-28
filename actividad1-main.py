from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        if request.form.get('opcion') == '1':
            return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif request.form.get('opcion') == '2':
            return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif request.form.get('opcion') == '3':
            return "<h1> La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        elif request.form.get('opcion') == '4':
            return "<h1> La division es: {} </h1>".format(str(int(num1)/int(num2)))
    else:
        return'''
        <form action = "/operasBas" method="POST">
        <label>Selecciona la Operacion: </label><br>
        <label>Suma </label>
        <input type="radio" name="opcion" value="1"><br><br>
        <label>Resta </label>
        <input type="radio" name="opcion" value="2"><br><br>
        <label>Multiplicacion </label>
        <input type="radio" name="opcion" value="3"><br><br>
        <label>Division </label>
        <input type="radio" name="opcion" value="4"><br><br>
        <button type="submit" value="Calcular">Calcular operaciones</button>
        <h3>Inserta los numeros</h3>
        <label>N1: </label>
        <input type="text" name="num1"/><br><br>
        <label>N2: </label>
        <input type="text" name="num2"/><br><br>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True,port=3000)