pipeline {
  agent any
  stages {
    stage('Inicio_Environment') {
      steps {
        echo 'Iniciando contruccion de proyect'
        sh 'env'
      }
    }

    stage('docker Env') {
      parallel {
        stage('docker Env') {
          steps {
            sh '/usr/local/bin/docker -v'
          }
        }

        stage('Images from docker') {
          steps {
            sh '/usr/local/bin/docker images'
          }
        }

      }
    }

  }
}