from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja


class Dojo:
    def __init__(self, data):
        #data ={id: 1, name: Chile, crated_at: 0000-00-00., update_at : 0000-00-00}
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

        #lista con todos los ninjas 
        self.ninjas = []

    #aqui estoy haciendo la funcionalidad para guardar todos los dojos
    @classmethod
    def save(cls, formulario):
        #formulario = {name: Chile}
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL ('dojos_ninjas').query_db(query)  
        #results = [
        #    {id: 1, name: "Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #    {id: 2, name: "México", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #    {id: 3, name: "Perú", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #]
        dojos = []
        for d in results:
            #id =(id: 1, name: colombia, created_at: 0000-00-00, updated_at: 0000-00-00)
            dojos.append( cls(d) ) #cls(d) lo que hace es crear una instancia de dojo, append ingresa esa instancia e ala lista de dojos    
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        #data = {id: 1}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        dojo = cls(results[0]) #Aquí creamos la instancia de Dojo

        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'update_at': row['update_at'],
                'id': row['id']
            }

            instancia_ninja = Ninja(ninja)
            dojo.ninjas.append(instancia_ninja)
        
        return dojo