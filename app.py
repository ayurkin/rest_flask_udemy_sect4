from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'alex'

items = []

class ItemList(Resource):
    def get(self):
        return {'items': items}

class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': None}, 200 if item else 404


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name'{}' already exists".format(name)}, 400
        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == "__main__":
    app.run(port=5000, debug=True)