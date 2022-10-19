from tkinter import INSERT
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        #data ={id: 1, name: Chile, crated_at: 0000-00-00., update_at : 0000-00-00}
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']

        #lista con todos los ninjas 
        self.ninjas = []

    #aqui estoy haciendo la funcionalidad para guardar todos los dojos
    @classmethod
    def save(cls, formulario):
        #formulario voy a recibir un diccionario (name: chile)
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query, formulario) # aqui debe ir el mismo nombre que le puse al esquema en mysql
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL ('dojos_ninjas').query_db(query)  
        dojos = []
        for d in results:
            #id =(id: 1, name: colombia, created_at: 0000-00-00, updated_at: 0000-00-00)
            dojos.append( cls(d) ) #cls(d) lo que hace es crear una instancia de doj, append ingresa esa instancia e ala lista de dojos    
        return dojos
    