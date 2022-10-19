from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, data):
        #data = {Diccionario con todos los datos}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.dojo_id = data['id']

    #aqui creamos la funcion para guardar 
    @classmethod
    def save(cls, formulario):
        query = "INSERT into ninjas (first_name, last_name, age, id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(id)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query, formulario)
        return result     