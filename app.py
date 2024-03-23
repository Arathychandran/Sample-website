from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = {
  'id' : 1,
  'title' : 'Serum',
  'Price' : 'Rs. 550',
  'Description' : 'This is a serum for your skin'
},{
  'id' : 2,
  'title' : 'Toner', 
  'Description' : 'This is a toner for your skin'
},{
  'id' : 3,
  'title' : 'Sunscreen',
  'Price' : 'Rs. 850',
  'Description' : 'This is a sunscreen for your skin'
}

@app.route('/')
def hello_world():
  return render_template('home.html',
                        products=PRODUCTS)

@app.route("/api/products")
def list_prod(): 
  return jsonify(PRODUCTS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
