pipeline {
    agent any

    stages {
        stage('Test') { 
            steps {
                new File('test').mkdir()

                dir ('test') {
                    checkout scm
                }
            }
        }
    }
}
