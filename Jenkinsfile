pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                withPythonEnv('/usr/bin/python3.5') {
                    pysh 'pip install --no-cache-dir -r requirements.txt --break-system-packages'
                    pysh 'pytest --disable-warnings'
                }
            }
        }
        stage('Build image') {
            agent any
            steps {
                script {
                    docker.withRegistry('https://rgx01.web-ones.com', 'RGX01_WEBONES') {
                        def image = docker.build("api-python-fast-images:latest")
                        image.push()
                    }
               }
            }
        }

        stage('Deployment') {
            agent any
            steps {
                script {
                    sh 'echo Deploying to K8s'
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