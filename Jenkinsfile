pipeline {
  agent any
  stages {
    stage('docker-run') {
      steps{
          bat 'docker-compose up -d'
      }
    }
    stage ('wait-for-deployment') {
        bat 'bash wait_5000.sh > statusBack'
        waitUntil(initialRecurrencePeriod: 15000) {
            script {
                def status = readFile(file: "statusBack")
                if (status =~ "ready"){
                    return true
                }else {
                    echo "not ready"
                    return false
                }
            }
        }
    }
    stage ('docker-down') {
      steps{
      bat 'del statusBack'
	  bat 'docker-compose down'
      }
    }
  }
}