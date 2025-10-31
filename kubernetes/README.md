#  Wisecow Application Deployment

This repository demonstrates a complete **CI/CD pipeline** for deploying the **Wisecow application** using **Docker**, **Kubernetes**, **TLS certificates**, and **ArgoCD** for GitOps-based Continuous Delivery.

---

##  1. Docker Build and Push (CI)

This phase packages the application and makes it available for deployment.
![Build Success](/project-demo/githubactions.png)

###  Build Docker Image

The Wisecow application source code is containerized using Docker and Pushed into Dockerhub registry.

---

## 2.  Application Deployment (CD - Initial Kubernetes Setup)

This phase covers deploying the foundational Kubernetes resources


``` kubectl kustomize kubernetes/argocd | kubectl apply -f -
kubectl kustomize kubernetes/certmanager | kubectl apply -f -
kubectl kustomize kubernetes/ingress | kubectl apply -f -
kubectl kustomize kubernetes/manifests | kubectl apply -f -
kubectl apply -f Kubernetes/argocd/application.yaml
 ```
---

## 3.  TLS Certification using Cert-Manager

This phase secures the application endpoint with HTTPS.
![tls Certificate](/project-demo/CertificateViewer.png)

---

## 4.  ArgoCD Image Update (Continuous Delivery Loop)

This phase automates the final step, ensuring new images are rolled out without manual intervention.
![Argocd](/project-demo/argocd-ui1.png)
![Argocd](/project-demo/iamge-updater.png)

