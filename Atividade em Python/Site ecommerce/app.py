#Importações
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


#instancia o Flask
app = Flask(__name__)
#configura o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Modelagem

# Criando o objeto  produto que será armazenada no nosso banco de dados
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])     # Na criação das rotas também adicionamos os métodos
def add_product():
    data = request.json    # request é importado do flask
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))    # Cria o prduto baseado no que o usuário inseriu no postman
        db.session.add(product)      # Adiciona um produto
        db.session.commit()     # Commita 
        return jsonify({"message": 'Product added correctly'})
    return jsonify({"message": "Invalid product data"}), 400  #jsonify() - retorna um json e o 400 mostra que deu erro

@app.route(f'/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product =Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'product deleted successfully'})
    else:
        return jsonify({'message': 'product not found'}), 404      # 404 é para algo não encontrado 


#Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'hello world'



if __name__ == '__main__':
    app.run(debug=True)