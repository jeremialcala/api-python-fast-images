pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh 'docker build -t api-python-fast-images:latest .'
                sh 'docker run -it -p 5004:5002 --name api-python-fast-images --restart unless-stopped -d api-python-fast-images'
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