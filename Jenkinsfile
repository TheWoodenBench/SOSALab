pipeline {
    agent any

    stages {
        stage('Test') { 
            steps {
                dir ('test') {
                    checkout scm
                }

                bat 'bandit -r test/dodatak_A.py >> logs/bandit.log'
            }
        }
    }
}
