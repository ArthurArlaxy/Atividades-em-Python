#Importações
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

#instancia o Flask
application = Flask(__name__)
#configura o banco de dados
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
#configura o chave secreta do LoginManager
application.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(application)
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'
CORS(application)
# Modelagem

# Criando o objeto  produto que será armazenada no nosso banco de dados
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique= True)
    password = db.Column(db.String(80), nullable=False)
    cart = db.relationship('CartItem', backref='user', lazy= True) # Cria uma relação entre o CartItem e o usuario

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable= False)

#Autenticacao
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@application.route('/')
def initial():
    return 'API ECOMMERCE IS WORKING'

@application.route('/api/user/create', methods=['POST'])
def add_user():
    data = request.json
    if 'username' in data and 'email' in data and 'password' in data:
        user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    return jsonify({'message': 'User invalid data'}), 400

@application.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and data.get('password') == user.password:
        login_user(user)
        return jsonify({'message': 'Logged in successfully'})
    return jsonify({'message': 'Unauthorized. Invalid credentials'}),401

@application.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'logout successfully'})

@application.route('/api/products/add', methods=["POST"])
@login_required     # Na criação das rotas também adicionamos os métodos
def add_product():
    data = request.json    # request é importado do flask
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))    # Cria o prduto baseado no que o usuário inseriu no postman
        db.session.add(product)      # Adiciona um produto
        db.session.commit()     # Commita 
        return jsonify({"message": 'Product added correctly'})
    return jsonify({"message": "Invalid product data"}), 400  #jsonify() - retorna um json e o 400 mostra que deu erro

@application.route(f'/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    product =Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'product deleted successfully'})
    else:
        return jsonify({'message': 'product not found'}), 404      # 404 é para algo não encontrado 

@application.route('/api/products/<int:product_id>', methods=['GET'])
def get_prudoct_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    return jsonify({'message': 'Not found, product not available' }), 404

@application.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    data = request.json
    if 'name' in data or 'price' in data or 'description' in data:
        product = Product.query.get(product_id)
        if product:
            product.name = data.get('name',product.name)
            product.price = data.get('price',product.price)
            product.description = data.get('description', product.description)
            db.session.commit()
            return jsonify({'message': 'product updated successfully'})
        return jsonify({'message': 'Product not found'}), 404     #três retornos diferentes
    return jsonify({'message': 'Invalid product data'}), 400

@application.route('/api/products', methods= ['GET'])
def get_products():
    products = Product.query.all()
    list_products=[]
    for product in products:
        product_info = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        }
        list_products.append(product_info)
    return jsonify(list_products)

@application.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = User.query.get(int(current_user.id))     # Usuário
    product = Product.query.get(product_id)         # Produto
    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({'message': 'Item added to the cart successfully'})
    return jsonify({'message': 'Failed to add item to the cart'}), 400

@application.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id,product_id= product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify ({'message': 'Product deleted from cart'})
    return jsonify ({'message': 'Failed to remove item from the cart'}), 400

@application.route('/api/cart',methods=['GET'])
@login_required
def view_cart_items():
    cart = []
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        cart_item_info = {
            'id': cart_item.id,
            'product_id': cart_item.product_id,
            'product_name': product.name,
            'product_price': product.price
        }
        cart.append(cart_item_info)
    return jsonify (cart)

@application.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
    user = User.query.get(current_user.id)
    cart_items = user.cart
    for cart_item in cart_items:
        db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'messager': 'Checkout successfully. Cart has been cleared'})

if __name__ == '__main__':
    application.run(debug=True)