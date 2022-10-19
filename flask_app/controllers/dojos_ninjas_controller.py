from flask import Flask, render_template, request, redirect
from flask_app import app

from flask_app.models.dojos import Dojo #aqui hago la importacion para dojo
from flask_app.models.ninjas import Ninja

# todos los enlaces deben derivarme a /localhost5000/dojos
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html') 

#Aqui estoy creando la ruta para guardar
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {name: Chile} 
    Dojo.save(request.form)
    return redirect('/dojos')  

@app.route('/new/ninja')
def new_ninja():
    return render_template('/new.html')
    dojos = Dojo.get_all('new.html', dojos=dojos    )      

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    #Recibo request.form = {dojo_id: 1, first_name:Elena, last_name: De Troya, age: 30}
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo.html', dojo=dojo)