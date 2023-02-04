
from flask import Flask, render_template
from flask import request

app=Flask(__name__)


@app.route("/cinepolis",methods=["GET"])
def cinepolis():
    return render_template("actividad3-cinepolis.html")

@app.route("/resultado",methods=["POST"])
def resultado():
     nombre=request.form.get('txtNombre')
     numCompradores=int(request.form.get('txtCantidad'))
     numBoletos=int(request.form.get('txtCantidadB'))
     tarjeta=request.form.get('opcion')
     totalv = 12*numBoletos
     respuesta=""
     
     if int(numBoletos)>7:
        respuesta="solo puedes comprar 7 boletos"
        totalDes=""
     else:
        if int(numBoletos) >5:
            if tarjeta=="si":
                totalM=totalv-(totalv*0.15)
                totalDes=totalM-(totalM*0.10)
            else:
                totalDes=totalv-(totalv*0.15)
        elif int(numBoletos)<=5 and int(numBoletos >=3 ):
                if tarjeta=="si":
                    totalM=totalv-(totalv*0.10)
                    totalDes=totalM-(totalM*0.10)
                else:
                    totalDes=totalv-(totalv*0.10)
        else: 
            if tarjeta=="si":
                totalDes=totalv-(totalv*0.10)
            else:
                totalDes=totalv




     return render_template("actividad3-cinepolis.html",totalDes=totalDes,respuesta=respuesta)
    
if __name__ == "__main__":
    app.run(debug=True, port=3000)
