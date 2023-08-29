pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-acces')
	}

	stages {
		
	      stage('gitclone') {

			steps {
				git 'https://github.com/marwenerzig1/TurboTUBE.git'
			}
		}

		stage('Build') {

			steps {
				bat 'docker build -t myapp https://github.com/marwenerzig1/TurboTUBE.git'
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
