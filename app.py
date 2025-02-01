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
<html>
<head>
    <title>DevOps Lifecycle</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #4CAF50; }
        .stage { border: 1px solid #ddd; padding: 15px; margin: 10px; border-radius: 8px; display: inline-block; width: 250px; }
    </style>
</head>
<body>
    <h1>DevOps Lifecycle</h1>
    {% for stage in stages %}
        <div class="stage">
            <h3>{{ stage.name }}</h3>
            <p>{{ stage.description }}</p>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, stages=DEVOPS_STAGES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
