pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                bat "rd /S /Q test"
                bat "rd /S /Q production"
            }
        }

        stage('Test') { 
            steps {
                script {
                    DATETIME = new Date().format("yyyyMMddHHmmss", TimeZone.getTimeZone('UTC'))
                }

                dir ('test') {
                    checkout scm
                }

                dir ('logs') {
                    bat "python ../test/tests.py 2> unittest_${DATETIME}.log"
                    bat "bandit -r ../test/dodatak_A.py > bandit_${DATETIME}.log"
                }
            }
        }

        stage('Production') {
            steps {
                dir ('production') {
                    bat "xcopy ..\\test ."
                }
            }
        }

        stage('Cleanup') {
            steps {
                bat "rd /S /Q test"
            }
        }
    }
}
