pipeline {
    agent any
    stages {

        stage('Build image') {
            steps {
                sh 'docker build -t api-python-fast-images:latest .'
            }
        }
    }

    post {
        always {
            // Clean up any temporary files
            sh 'rm -rf target/'
        }
    }
}