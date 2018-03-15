from flask import Flask, render_template
from data import Pizza, Makarony, Przystawki, Napoje, Sosy, Gadzety

app = Flask(__name__)

Pizza = Pizza()
Makarony = Makarony()
Przystawki = Przystawki()
Napoje = Napoje()
Sosy = Sosy()
Gadzety = Gadzety()

@app.route('/')
def index():
	return render_template('zamowienie.html')

@app.route('/menu')
def menu():
	return render_template('menu.html', pizza = Pizza, makarony = Makarony, przystawki = Przystawki, napoje = Napoje, sosy = Sosy, gadzety = Gadzety )
def SetPizza():
	active_list = "pizza"

if __name__ == '__main__':
	app.run(debug=True)