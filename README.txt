1. Create a git repo
2. Write a python code to print Hello world in starting & then print CPU, Mem usage of the pod in every 10 sec
3. Commit the code to feature/git-jenkins branch in Github
4. Create a PR of feature/git-jenkins branch to the main branch
5. Approve the PR


Write an automated pipeline to perform the below steps -
(you can use GCP or AWS or minikube )

1. Use the above code of the main branch from GitHub to build its docker image.
2. Build the docker image with the name jenkins-assignment and tag v1. Push the docker image to GCR/ECR
3. Use the image pushed to GCR/ECR from (step 2) to deploy to a Kubernetes cluster GKE/EKS
4. List images in GCR/ECR, pods, and deployments in GKE/EKS
5. Pipeline should trigger an email to your Sigmoid's email ID on success or failure of the pipeline
