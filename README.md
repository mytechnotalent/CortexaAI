![image](https://github.com/mytechnotalent/CortexaAI/blob/main/CortexaAI.jpg?raw=true)

# CortexaAI
An open-source Python Selenium Test Automation framework with Docker and Kubernetes integration.

<br>

## Step 1: Install Docker Desktop
Docker Desktop [Instructions](https://docs.docker.com/desktop)

## Step 2: Install Helm
Helm [Instructions](https://helm.sh/docs/intro/install)

## Step 3a: Setup Local Environment MAC/LINUX [OPTION 1]
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3b: Setup Local Environment Windows [OPTION 2]
```bash
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Step 4: Deploy & Run App to Kubernetes via Helm
```bash
cd app
helm install website .
kubectl -n default get service website-cortexaai
```

## Step 5: Run Selenium Grid
```bash
docker compose up --scale chrome=2
```

## Step 6: Observe Selenium Grid
```
http://localhost:4444/ui
```

<br>

# Run Front-End Tests MAC/LINUX [OPTION 1]
```bash
export BROWSER=chrome 
URL=http://localhost:<PORT>
python -m unittest discover
```

# Run Front-End Tests Windows [OPTION 2]
```bash
$env:BROWSER="chrome"
$env:URL="http://host.docker.internal:<PORT>"
python -m unittest discover
```

<br>

# License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
