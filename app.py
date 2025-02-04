from flask import Flask, render_template_string

app = Flask(__name__)

DEVOPS_STAGES = [
    {"name": "Plan", "description": "Define requirements and strategies."},
    {"name": "Develop", "description": "Write, review, and manage source code."},
    {"name": "Build", "description": "Compile and package source code."},
    {"name": "Test", "description": "Perform automated and manual testing."},
    {"name": "Release", "description": "Prepare release notes and approvals."},
    {"name": "Deploy", "description": "Deploy applications to production."},
    {"name": "Operate", "description": "Manage infrastructure and availability."},
    {"name": "Monitor", "description": "Collect logs, metrics, and feedback."}
]

LEARNING_STEPS = [
    {"step": "Learn Linux & Shell", "details": "Get comfortable with basic Linux commands."},
    {"step": "Master Git", "details": "Understand version control systems like Git & GitHub."},
    {"step": "CI/CD Basics", "details": "Learn Jenkins, GitHub Actions, and automation."},
    {"step": "Understand Containers", "details": "Docker and Kubernetes basics."},
    {"step": "Explore Cloud", "details": "Familiarize with AWS, Azure, or Google Cloud."},
    {"step": "IaC & Automation", "details": "Terraform, Ansible, and scripting."},
    {"step": "Monitoring & Logging", "details": "Prometheus, Grafana, and ELK stack."},
    {"step": "Security & Best Practices", "details": "Learn DevSecOps and compliance."}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Lifecycle & Learning</title>
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            text-align: center; 
            margin: 0; 
            padding: 20px; 
            background: linear-gradient(135deg, #1e3c72, #2a5298); 
            color: white;
        }
        h1, h2 { 
            margin: 10px 0; 
            font-size: 2em; 
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 15px;
            padding: 10px;
            max-width: 90%;
            margin: auto;
        }
        .card { 
            background: rgba(255, 255, 255, 0.15);
            border-radius: 10px; 
            padding: 15px; 
            transition: transform 0.3s, background 0.3s;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            position: relative;
            font-size: 1em;
        }
        .card:hover {
            transform: scale(1.05);
            background: rgba(255, 255, 255, 0.25);
        }
        h3 { 
            margin-bottom: 5px; 
            font-size: 1.2em;
        }
        p { 
            font-size: 0.9em; 
            opacity: 0.9; 
            margin: 5px 0;
        }
        .number {
            position: absolute;
            top: -10px;
            left: -10px;
            background: #FFD700;
            color: #333;
            font-size: 1em;
            font-weight: bold;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0px 3px 8px
