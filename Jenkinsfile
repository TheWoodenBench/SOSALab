pipeline {
    agent any

    stages {
        stage('Test') { 
            steps {
                script {
                    DATETIME = java.time.LocalDateTime.now()
                }

                dir ('test') {
                    checkout scm
                }

                dir ('logs') {
                    bat "python ../test/tests.py > unittest_${DATETIME}.log"
                    bat "bandit -r ../test/dodatak_A.py > bandit_${DATETIME}.log"
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
