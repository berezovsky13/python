pipeline {
    agent any
    environment{
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "berezovsky8/january2025coursecicd"
    }
    
    stages {
        stage('Code Checkout') {
            steps {
                git url: 'https://github.com/berezovsky13/python.git', branch: 'main'
            }
        }
        stage('Docker Build'){
            steps{
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }
    }
}
