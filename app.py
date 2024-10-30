from flask import Flask, render_template
import math
from turtle import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw-heart')
def draw_heart():
    # Aqui você pode chamar a lógica do seu código Turtle
    def hearta(k):
        return 15 * math.sin(k)**3

    def heartb(k):
        return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

    speed(0)
    bgcolor("black")
    for i in range(6000):
        goto(hearta(i) * 20, heartb(i) * 20)
        for j in range(5):
            color("red")
            goto(0, 0)
    done()

    return "Coração desenhado!"

if __name__ == '__main__':
    app.run(debug=True)
