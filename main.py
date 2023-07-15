from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': 'T-shirt',
        'price': 20.99,
        'description': 'A basic t-shirt'
    },
    {
        'id': 2,
        'name': 'Pants',
        'price': 35.99,
        'description': 'A pair of jeans'
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'id': request.json['id'],
        'name': request.json['name'],
        'price': request.json['price'],
        'description': request.json['description']
    }
    products.append(new_product)
    return jsonify({'message': 'Product created successfully'}), 201

if __name__ == '__main__':
    app.run()
