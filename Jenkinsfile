pipeline {
    agent any
    
    stages {
        stage('Code Checkout') {
            steps {
                git url: 'https://github.com/berezovsky13/python.git', branch: 'main'
            }
        }
        stage('Docker Build'){
            steps{
                sh 'docker build -t test:1.0 .'
            }
        }
    }
}
