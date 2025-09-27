# 🚀 Telegram Userbot + Web Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)](https://fastapi.tiangolo.com/)  
[![Render](https://img.shields.io/badge/Deploy-Render-black)](https://render.com/)  
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)  
[![CI](https://github.com/JAY01-CYBER/Web-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/JAY01-CYBER/Web-bot/actions)

A professional Telegram **Userbot** powered by **Telethon** + **FastAPI Web Dashboard**.  
Deploy on **Render**, **Docker**, **Railway**, **Fly.io**, **Heroku**, or **Kubernetes/Helm** for 24/7 hosting.  

---

## ✨ Features
- 🤖 Responds to `!ping` in Telegram chats.  
- 🌍 REST API endpoints:  
  - `GET /` → Status  
  - `GET /send/{chat_id}/{msg}` → Send a message  
  - `POST /broadcast/` → Broadcast to multiple chats  
- 💻 Web Dashboard:  
  - `GET /dashboard` → User-friendly broadcast page  

![Dashboard Preview](docs/preview.png)

---

## ⚡ Local Setup

```bash
# Clone repo
git clone https://github.com/JAY01-CYBER/Web-bot
cd Web-bot

# Install dependencies
pip install -r requirements.txt

# Export env vars
export API_ID=your_api_id
export API_HASH=your_api_hash
export SESSION=your_session_string

# Run
python main.py
```

Open `http://localhost:8000/dashboard` in your browser.

---

## ☁️ Deploy on Render

1. Push repo to GitHub.  
2. Click the button below 👇  

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

3. Render will detect `render.yaml`.  
4. Add env vars:  
   - `API_ID`  
   - `API_HASH`  
   - `SESSION`  

✅ Done! Userbot runs 24/7.

---

## 🐳 Run with Docker

```bash
# Build Docker image
docker build -t web-bot .

# Run container with environment variables
docker run -d   -e API_ID=your_api_id   -e API_HASH=your_api_hash   -e SESSION=your_session_string   -p 8000:8000   web-bot
```

Now open in browser:  
```
http://localhost:8000/dashboard
```

---

## 🚄 Deploy on Railway

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Init project
railway init

# Set environment variables
railway variables set API_ID=your_api_id API_HASH=your_api_hash SESSION=your_session_string

# Deploy
railway up
```

Open the app URL given by Railway 🚀  

---

## ✈️ Deploy on Fly.io

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch app
fly launch --name web-bot --no-deploy

# Set environment variables
fly secrets set API_ID=your_api_id API_HASH=your_api_hash SESSION=your_session_string

# Deploy
fly deploy
```

Fly.io gives global fast performance 🌍  

---

## ☁️ Deploy on Heroku

1. Install Heroku CLI → https://devcenter.heroku.com/articles/heroku-cli  
2. Login:  
```bash
heroku login
```

3. Create an app:  
```bash
heroku create web-bot-app
```

4. Push code:  
```bash
git push heroku main
```

5. Set environment variables:  
```bash
heroku config:set API_ID=your_api_id API_HASH=your_api_hash SESSION=your_session_string
```

6. Scale dynos:  
```bash
heroku ps:scale web=1
```

App will be live at:  
```
https://web-bot-app.herokuapp.com/dashboard
```

---

## ☸️ Deploy on Kubernetes (Manifest)

1. Build and push Docker image to DockerHub/GHCR:  
```bash
docker build -t your-dockerhub-username/web-bot:latest .
docker push your-dockerhub-username/web-bot:latest
```

2. Apply Kubernetes manifest:  
```bash
kubectl apply -f k8s-deployment.yaml
```

3. Check status:  
```bash
kubectl get pods
kubectl get svc web-bot-service
```

4. Access app via LoadBalancer URL:  
```
http://<EXTERNAL-IP>/dashboard
```

---

## 🧭 Deploy with Helm

```bash
# Install via local chart
helm install web-bot ./chart

# To upgrade
helm upgrade web-bot ./chart

# Uninstall
helm uninstall web-bot
```

Customize `chart/values.yaml` (image repo/tag, env values, replicaCount) before install.

---

## 🔥 API Examples

**Send Message**  
```bash
curl "http://localhost:8000/send/123456789/Hello%20World"
```

**Broadcast**  
```bash
curl -X POST "http://localhost:8000/broadcast/?msg=Hello%20everyone" -H "Content-Type: application/json" -d "[123456789, 987654321]"
```

---

## 📂 Project Structure

```
Web-bot/
 ├── main.py          # Telegram Userbot + FastAPI
 ├── frontend.html    # Web dashboard
 ├── requirements.txt # Dependencies
 ├── render.yaml      # Render deploy config
 ├── Dockerfile       # Docker support
 ├── .gitignore
 ├── README.md        # Docs
 ├── tests/           # Basic tests
 │   └── test_app.py
 ├── .github/
 │   └── workflows/
 │       └── ci.yml   # CI workflow
 ├── k8s-deployment.yaml
 ├── chart/           # Helm chart for k8s
 │   └── ...
 └── docs/
     └── preview.png  # Dashboard screenshot (replace with your own)
```

---

## 🛠️ Built With
- [Telethon](https://github.com/LonamiWebs/Telethon)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Render](https://render.com/)  
- [Docker](https://www.docker.com/)  
- [Railway](https://railway.app/)  
- [Fly.io](https://fly.io/)  
- [Heroku](https://www.heroku.com/)  
- [Kubernetes](https://kubernetes.io/)  
- [Helm](https://helm.sh/)  
- [GitHub Actions](https://github.com/features/actions)  

---
Made with ❤️ by [JAY01-CYBER](https://github.com/JAY01-CYBER)
