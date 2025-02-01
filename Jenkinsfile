pipeline{
    agent any
    environment{
        IMAGE_NAME = '22monk/flaskkubernetesjenkins'
        IMAGE_TAG = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        KUBECONFIG = credentials('kubeconfig')

    }
    stages{

        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stages {
        stage('Setup') {
            steps {
                sh 'ls -la $KUBECONFIG'
                sh 'chmod 644 $KUBECONFIG'
                sh 'ls -la $KUBECONFIG'
                
            }
        }
        stage('login to docker hub'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin"
                    echo "Logged in to docker hub securely"
                }

            }
        }
        stage('Build Docker Image'){
            steps{
                sh "docker build -t ${IMAGE_TAG} ."
                echo "Docker image built successfully"
                sh "docker image ls"
            }
        }
         stage('Push Docker Image')
        {
            steps
            {
                sh 'docker push ${IMAGE_TAG}'
                echo "Docker image push successfully"
            }
        }
        stage('Configure Kubernetes Cluster') {
    steps {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
            script {
                sh """
                mkdir -p /var/lib/jenkins/.kube
                cp ${KUBECONFIG} /var/lib/jenkins/.kube/config
                chmod 644 /var/lib/jenkins/.kube/config
                export KUBECONFIG=/var/lib/jenkins/.kube/config
                kubectl cluster-info
                """
            }
        }
    }
}
stage('Apply Kubernetes Manifest') {
            steps {
                script {
                    sh """
                    
                    sed -i 's|<IMAGE_TAG>|${env.IMAGE_TAG}|g' deployment-service.yaml
                    kubectl apply -f deployment-service.yaml
                    """
                }
            }
        }
    }
                
  }
}
