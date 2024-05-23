pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'docker build -t my-python-app .'
                sh 'docker run -p 8000:8000 my-python-app'
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