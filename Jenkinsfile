pipeline {
    agent any

    stages {
        stage('Test') { 
            steps {
                dir ('test') {
                    checkout scm
                }

                dir ('logs') {
                    bat 'python ../test/tests.py >> unittest.log'
                    bat 'bandit -r ../test/dodatak_A.py >> bandit.log'
                }
            }
        }

        stage('Production') {
            steps {
                dir ('production') {
                    bat "cp '../test/*' '.'"
                }
            }
        }
    }
}
