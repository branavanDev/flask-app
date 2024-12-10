from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample project data
projects = [
    {
        "id": 1,
        "title": "E-Commerce Platform",
        "description": "Full-stack responsive e-commerce website with payment integration.",
        "technologies": ["React", "Node.js", "MongoDB"],
        "github_link": "https://github.com/branavanDev/flask-app",
        "demo_link": "https://demo-ecommerce.com",
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "title": "Machine Learning Dashboard",
        "description": "Interactive dashboard for real-time ML model performance tracking.",
        "technologies": ["Python", "Flask", "TensorFlow", "Chart.js"],
        "github_link": "https://github.com/branavanDev/flask-app",
        "demo_link": "https://ml-dashboard.com",
        "created_at": datetime.now()
    },
     {
        "id": 3,
        "title": "BRN portfolio",
        "description": "Full-stack responsive e-commerce website with payment integration.",
        "technologies": ["React", "Node.js", "MongoDB"],
        "github_link": "https://github.com/branavanDev/flask-app",
        "demo_link": "https://demo-ecommerce.com",
        "created_at": datetime.now()
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def project_list():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form submission (in a real app, add proper validation)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you would typically save to database or send email
        return jsonify({"status": "success", "message": "Message sent successfully!"})
    return render_template('contact.html')

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)