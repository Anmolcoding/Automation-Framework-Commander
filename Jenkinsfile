pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        REPORT_DIR = 'reports'
        ALLURE_RESULTS = "${REPORT_DIR}/allure-results"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '${PYTHON} -m pip install --upgrade pip'
                sh '${PYTHON} -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '${PYTHON} -m pytest -n auto --alluredir=${ALLURE_RESULTS} --html=${REPORT_DIR}/report.html --self-contained-html'
            }
        }

        stage('Publish Reports') {
            steps {
                archiveArtifacts artifacts: '${REPORT_DIR}/report.html', fingerprint: true
                archiveArtifacts artifacts: '${ALLURE_RESULTS}/**/*', fingerprint: true
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: '**/TEST-*.xml'
        }
    }
}
