from flask import Flask, jsonify, render_template
from hill_climbing import i_hill_climbing, coord

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tsp')
def resolver_tsp():
    ruta, distancia = i_hill_climbing(coord)
    return jsonify({
        'mejor_ruta': ruta,
        'distancia_total': round(distancia, 4)
    })

if __name__ == '__main__':
    app.run(debug=True)
