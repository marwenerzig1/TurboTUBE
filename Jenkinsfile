pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-hub')
  }
  stages {
    stage('Build') {
      steps {
        bat 'docker build -t marwenerzig1/turbotube:v1 .'
      }
    }
    stage('Login') {
      steps {
        bat 'docker login -u=%DOCKERHUB_CREDENTIALS_USR% -p=%DOCKERHUB_CREDENTIALS_PSW%'
      }
    }
    stage('Push') {
      steps {
       // bat 'docker push marwenerzig1/turbotube:v1'
          echo 'test'        
      }
    }
    stage('Pull') {
      steps {
        bat 'docker pull marwenerzig1/turbotube:v1'
      }
    }
    stage('Run') {
      steps {
         bat 'docker run -p 5000:5000 --name TurboTube -d marwenerzig1/turbotube:v1'
      }
    }
  }
  post {
    always {
      bat 'docker logout'
    }
  }
}
