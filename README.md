# 🚀 Flask CI/CD Pipeline with Docker, Jenkins & Ansible

A step-by-step, production-ready **CI/CD pipeline** demonstration for a Flask web application, using **Docker** for containerization, **Jenkins** for automation, and **Ansible** for seamless remote deployments. Automate your workflow from code commit to live deployment, all in one repository!

---

## 🛠️ Tech Stack

- **Python Flask** — User login & feedback web app
- **Docker** — Containerization
- **Docker Hub** — Image registry
- **Jenkins** — CI/CD orchestration
- **Ansible** — Automated deployment
- **GitHub** — Source control

---

## 📂 Project Structure

```
flask-ci-cd/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── login.html
│       └── feedback.html
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── ansible/
│   ├── hosts
│   └── deploy.yml
```

---

## 🚦 Prerequisites

- Docker installed (locally and on remote server)
- Jenkins server (with Docker & Ansible installed)
- Remote server (Ubuntu recommended, Docker installed, SSH access)
- Docker Hub account (for pushing images)
- Git (on local and Jenkins machine)

---

## 🖥️ Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Alok77it/CI-CD-Pipeline-for-Flask_Django-App.git
   cd CI-CD-Pipeline-for-Flask_Django-App
   ```

2. **Set up Python virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```
   Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🐳 Docker Usage

- **Build the Docker image**
  ```bash
  docker build -t flask-ci-cd .
  ```
- **Run a Docker container**
  ```bash
  docker run -p 5000:5000 flask-ci-cd
  ```

---

## ⚙️ Jenkins Pipeline Setup

### 1. Add Docker Hub Credentials

- Go to **Manage Jenkins → Credentials → System → Global credentials**
- Add:
  - Type: Username with password
  - Username: *your Docker Hub username*
  - Password: *your Docker Hub password or access token*
  - ID: `docker-hub-creds`

### 2. Create a Jenkins Pipeline Job

- Go to **New Item → Pipeline**, name it (e.g. `flask-ci-cd-pipeline`)
- Under **Pipeline**, select **Pipeline script from SCM**
- SCM: **Git**
- Repo URL: *your GitHub repo URL*
- Branch: `main` or your default
- Script Path: `Jenkinsfile`
- **Save**

### 3. Make Sure Jenkins Node Has Docker & Ansible

```bash
docker --version
ansible --version
```

### 4. Test SSH from Jenkins to Remote Server

```bash
ssh ubuntu@<your.remote.server.ip>
```
Ensure the Jenkins user has SSH keys set up and authentication works.

---

## 🤖 Ansible Deployment

- **Edit `ansible/hosts`**  
  Specify your remote server and SSH user:
  ```
  [web]
  <your.remote.server.ip> ansible_user=ubuntu
  ```

- **(Optional) Run playbook manually**
  ```bash
  ansible-playbook -i ansible/hosts ansible/deploy.yml
  ```
  This will:
    - Stop any running Docker container for the app
    - Pull the latest image from Docker Hub
    - Start the container, exposing port 80

---

## 🔁 Full Pipeline Workflow

1. **Push code to GitHub**
2. **Jenkins job triggers** (manually or via webhook)
3. **Pipeline stages:**
   - Checkout code
   - (Optionally) Run tests
   - Build Docker image
   - Push image to Docker Hub
   - Run Ansible playbook for deployment

---

## 🌐 Access Your Application

Visit:  
```
http://<your.remote.server.ip>
```
You should see the Flask login page live and running!

---

## 🛠️ Troubleshooting

- **Check Docker status on remote:**
  ```bash
  sudo systemctl status docker
  ```
- **See running containers:**
  ```bash
  docker ps
  docker logs flask-ci-cd
  ```
- **Jenkins logs:**  
  Review the Jenkins job console output for errors.

- **Firewall/Security Groups:**  
  Ensure port 80 is open on your remote server.

- **SSH Issues:**  
  Confirm Jenkins has correct SSH keys and permissions.

---

## 💡 Tips & Improvements

- Add test/lint stages in the Jenkinsfile
- Set up SSL (e.g., Nginx reverse proxy) for production
- Secure Jenkins and Ansible secrets
- Expand Flask app features as needed

---

## 🤝 Contributing

Pull requests and issues are welcome!  
For suggestions, improvements, or questions, please open an issue.

---

## 📬 Contact

**Author:** [Alok Kumar](https://github.com/Alok77it)

---

<p align="center">
  <b>Thank you for exploring this project! Happy DevOps-ing! 🚀</b>
</p>
