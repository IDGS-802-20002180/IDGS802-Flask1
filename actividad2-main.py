
from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/operasBas",methods=["GET"])
def operasBas():
    return render_template("operasBas.html")

@app.route("/resultado",methods=["POST"])
def resultado():
    n1=int(request.form.get("txtNum1"))
    n2=int(request.form.get("txtNum2"))
    res=0
    for i in range(n2):
        res += n1
    
    return render_template("resultado.html",res=res,n1=n1,n2=n2)

    
if __name__ == "__main__":
    app.run(debug=True, port=3000)
