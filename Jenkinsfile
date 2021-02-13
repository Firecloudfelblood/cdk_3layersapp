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

    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'cat versionImage | xargs ./scripts/build.sh'
          }
        }

        stage('message') {
          steps {
            echo 'compilando'
          }
        }

      }
    }

    stage('container runner') {
      parallel {
        stage('container runner') {
          steps {
            sh '''/usr/local/bin/docker stop proyectoApi || true
/usr/local/bin/docker rm proyectoApi || true
/usr/local/bin/docker run --name proyectoApi -itd -p 3001:3001  grimripper/app3layer:9.9 '''
          }
        }

        stage('error') {
          steps {
            echo 'corriendo'
          }
        }

      }
    }

    stage('docker ps') {
      steps {
        sh '/usr/local/bin/docker ps'
      }
    }

  }
}