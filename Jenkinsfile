pipeline {
  agent any
  stages {
    stage('docker-run') {
      when {
        branch 'dev'
      }
      steps {
        bat 'docker-compose up -d'
      }
    }
    
    stage('docker-deploy') {
      when {
        branch 'main'
      }
      steps {
        bat 'docker-compose up -d'
      }
    }

    stage('wait-for-deployment') {
      when {
                branch 'dev'
            }
      steps {
        waitUntil(initialRecurrencePeriod: 15000) {
          script {
            try {
              def response = httpRequest 'http://127.0.0.1:5000/api/toxicity'
              return (response.status == 200)
            }
            catch (exception) {
              return false
            }
          }

        }

      }
    }

    stage('docker-down') {
      when {
                branch 'dev'
            }
      steps {
        bat 'docker-compose down'
      }
    }
  }
}
