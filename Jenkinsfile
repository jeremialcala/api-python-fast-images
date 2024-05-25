pipeline {
    agent any
    stages {

        stage('Build image') {
            agent any

            steps {
                script {
                    dockerImage = docker.build("api-python-fast-images:latest")
               }
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