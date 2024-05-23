pipeline {
    agent { dockerfile true }

    stages {
        stage('Deploy') {
            steps {
                sh 'echo "Deploying"'
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