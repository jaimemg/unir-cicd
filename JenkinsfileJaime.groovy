pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/jaimemg/unir-cicd.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
            post {
                always {
                    junit 'results/api_result.xml'
                }
            }
        }
        stage('E2E tests') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
            post {
                always {
                    junit 'results/e2e_result.xml'
                }
            }
        }
    }
    post {
         failure {
            emailext body: 'El pipeline ha fallado. Por favor, revisa los registros para obtener más detalles.',
                     subject: 'Fallo en la ejecución del pipeline',
                     to: 'jaimeunir@example.com'
        }
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
    }
}
