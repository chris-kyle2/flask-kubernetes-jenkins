from flask import Flask, render_template_string

app = Flask(__name__)

DEVOPS_STAGES = [
    {"name": "Plan", "description": "Define requirements, architecture, and strategies."},
    {"name": "Develop", "description": "Write, review, and manage source code."},
    {"name": "Build", "description": "Compile and package source code into artifacts."},
    {"name": "Test", "description": "Perform automated and manual testing."},
    {"name": "Release", "description": "Prepare release notes and approvals."},
    {"name": "Deploy", "description": "Deploy application to production environments."},
    {"name": "Operate", "description": "Manage infrastructure and ensure availability."},
    {"name": "Monitor", "description": "Collect logs, metrics, and feedback for improvement."}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Lifecycle</title>
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            text-align: center; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #1e3c72, #2a5298); 
            color: white;
        }
        h1 { 
            margin: 20px 0; 
            font-size: 2.5em; 
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            padding: 20px;
        }
        .stage { 
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px; 
            padding: 20px; 
            width: 280px; 
            transition: transform 0.3s, background 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
            position: relative;
        }
        .stage:hover {
            transform: scale(1.05);
            background: rgba(255, 255, 255, 0.2);
        }
        h3 { 
            margin-bottom: 10px; 
            font-size: 1.5em;
        }
        p { 
            font-size: 1em; 
            opacity: 0.9; 
        }
        .number {
            position: absolute;
            top: -10px;
            left: -10px;
            background: #FFD700;
            color: #333;
            font-size: 1.2em;
            font-weight: bold;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <h1>DevOps Lifecycle</h1>
    <div class="container">
        {% for stage in stages %}
            <div class="stage">
                <div class="number">{{ loop.index }}</div>
                <h3>{{ stage.name }}</h3>
                <p>{{ stage.description }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, stages=DEVOPS_STAGES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
