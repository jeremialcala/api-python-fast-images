pipeline {
    agent any
    stages {

        stage('Build image') {
            agent any

            steps {
                script {
                    docker.withRegistry('https://rgx01.web-ones.com', 'RGX01_WEBONES') {
                        dockerImage = docker.build("api-python-fast-images:latest")
                    }
               }
            }
        }
    }

    post {
        always {
            // Clean up any temporary files
            sh 'echo "DONE"'
        }
    }
}