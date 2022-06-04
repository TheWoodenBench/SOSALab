pipline {
    agent any

    stages {
        stage('Test') { 
            mkdir 'E:\\Dev\\Uni\\SOSA\\lab3\\test'
            
            git branch: 'main', changelog: false, poll: false, url: 'https://github.com/TheWoodenBench/SOSALab.git'
        }
    }
}
