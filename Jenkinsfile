pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
         stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                sh 'pip install -r requirements.txt' // Install dependencies if needed
                sh 'python -m unittest test_pet.py' // Replace with your test command
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