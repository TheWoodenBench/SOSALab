pipeline {
    agent any

    stages {
        stage('Test') { 
            steps {
                sh "mkdir 'E:\\Dev\\Uni\\SOSA\\lab3\\test'"

                dir ('E:\\Dev\\Uni\\SOSA\\lab3\\test') {
                    checkout scm
                }
            }
        }
    }
}
