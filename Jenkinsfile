pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="240068248627"
        AWS_DEFAULT_REGION="ap-south-1" 
        IMAGE_REPO_NAME="jenkins-assignment"
        IMAGE_TAG="v1"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {
        
         stage('Logging into AWS ECR') {
            steps {
                script {
                    withAWS(credentials: 'AWS_CREDENTIALS', region: 'ap-south-1') {
                        sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                    }
                }
                 
            }
        }

        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/gauravraj01/practice']]])
            }
        }
        
        // Building Docker images
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
        }
      }
    }
   
    // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
     steps{  
         script {
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
         }
        }
      }
      // Deployment
      stage('Deployment') {
       steps{
       	   script {
       	   	  sh "kubectl create deployment app --image=240068248627.dkr.ecr.ap-south-1.amazonaws.com/my-repo:v1 --replicas=1 --port=80"
       	   }
          }
       }
       // List
       stage('List') {
        steps{
            script {
                sh "kubectl get po"
                sh "kubectl get nodes"
                sh 'aws ecr list-images --repository-name "$IMAGE_REPO_NAME"'
            }
        }
       }
    }
}
