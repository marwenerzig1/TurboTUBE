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
        bat 'docker push marwenerzig1/turbotube:v1'
      }
    }
  }
  post {
    always {
      bat 'docker logout'
    }
  }
}
