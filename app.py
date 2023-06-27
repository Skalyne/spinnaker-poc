from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    image_url = 'pikachu.png'  # Replace with the actual path to your image
    description = 'updated description 2'  # Replace with your desired description
    return render_template('index.html', image_url=image_url, description=description)

if __name__ == "__main__":
    app.run()