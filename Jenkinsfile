pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'pip install -r requirements.txt' // Install dependencies if needed

            }
        }
         stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat 'python -m unittest test.test_pet' // Replace with your test command
                echo 'test_pet run successfuly..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}