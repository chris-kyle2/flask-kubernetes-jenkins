pipeline{
    agent any
    environment{
        IMAGE_NAME = '22monk/jenkins-pipeline'
        IMAGE_TAG = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        KUBECONFIG = credentials('kubeconfig')

    }
    stages{
        stage('Hello world'){
            steps{
                echo 'Hello world'
                
            }
        }
        stage('login to docker hub'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin"
                    echo "Logged in to docker hub"
                }

            }
        }
    }
                
}