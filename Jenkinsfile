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
        bat 'docker build -t marwenerzig1/turbotube:v2 .'
      }
    }
    stage('Login') {
      steps {
        bat 'docker login -u=%DOCKERHUB_CREDENTIALS_USR% -p=%DOCKERHUB_CREDENTIALS_PSW%'
      }
    }
    stage('Push') {
      steps {
        bat 'docker push marwenerzig1/turbotube:v2'
      }
    }
    stage('Pull') {
      steps {
        bat 'docker pull marwenerzig1/turbotube:v2'
      }
    }
  post {
    always {
      bat 'docker logout'
    }
  }
}
