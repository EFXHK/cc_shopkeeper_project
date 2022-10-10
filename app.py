from flask import Flask, render_template
from controllers.inventory_controller import inventory_blueprint


app = Flask(__name__)

app.register_blueprint(inventory_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



#####
#double check inventory controller and 
#inventory blueprint
#####