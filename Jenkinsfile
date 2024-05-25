pipeline {
    agent any
    stages {

        stage('Build image') {
            agent any
            environment {
                HOME = "${env.WORKSPACE}"
            }
            steps {
                script {
                    dockerImage = docker.build("api-python-fast-images:latest:${env.BUILD_ID}")
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