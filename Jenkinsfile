pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-acces')
	}

	stages {
	    
		stage('Build') {

			steps {
				bat 'docker build -t turbotube:v1'
			}
		}

		stage('Login') {

			steps {
				bat "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
			}
		}

		stage('Push') {

			steps {
				bat "docker image push "
			}
		}
	}

	post {
		always {
			bat "docker logout"
		}
	}

}
