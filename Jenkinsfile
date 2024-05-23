pipeline {
    def app

    stages {
        stage('Deploy') {
            steps {
                app = docker.build("getintodevops/hellonode")
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