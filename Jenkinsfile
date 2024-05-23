pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sh 'pip install -r requirements.txt'
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