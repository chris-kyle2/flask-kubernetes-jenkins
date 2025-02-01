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

LEARNING_STEPS = [
    {"step": "Learn Linux & Command Line", "details": "Get comfortable with shell scripting and basic Linux commands."},
    {"step": "Understand Version Control", "details": "Learn Git and platforms like GitHub/GitLab/Bitbucket."},
    {"step": "Master CI/CD", "details": "Understand Jenkins, GitHub Actions, GitLab CI/CD, and automation pipelines."},
    {"step": "Learn Containerization", "details": "Study Docker and container orchestration with Kubernetes."},
    {"step": "Understand Cloud Platforms", "details": "Familiarize yourself with AWS, Azure, or Google Cloud."},
    {"step": "Infrastructure as Code (IaC)", "details": "Learn Terraform, Ansible, and CloudFormation."},
    {"step": "Monitoring & Logging", "details": "Understand Prometheus, Grafana, ELK Stack, and Datadog."},
    {"step": "Security & Best Practices", "details": "Explore DevSecOps, security policies, and compliance."}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Lifecycle & Learning Path</title>
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            text-align: center; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #1e3c72, #2a5298); 
            color: white;
        }
        h1, h2 { 
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
        .stage, .learning-step { 
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px; 
            padding: 20px; 
            width: 280px; 
            transition: transform 0.3s, background 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
            position: relative;
        }
        .stage:hover, .learning-step:hover {
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

    <h2>How to Learn DevOps</h2>
    <div class="container">
        {% for step in learning_steps %}
            <div class="learning-step">
                <div class="number">{{ loop.index }}</div>
                <h3>{{ step.step }}</h3>
                <p>{{ step.details }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, stages=DEVOPS_STAGES, learning_steps=LEARNING_STEPS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
