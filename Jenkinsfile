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
      steps {
        sh 'docker -v'
      }
    }

  }
}