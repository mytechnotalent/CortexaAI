![image](https://github.com/mytechnotalent/CortexaAI/blob/main/CortexaAI.jpg?raw=true)

# CortexaAI
An open-source Automation Engine that can perform full Front-End Automation for scraping data in addition to Test Automation.

## Install Docker Desktop
Docker Desktop [Instructions](https://docs.docker.com/desktop/mac/install)

## Setup Local Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## OPTIONAL: Setup Voice Recognition (MAC Only)
Use Voice Control On MAC [Instructions](https://support.apple.com/en-us/HT210539).

## Run Docker Compose
```bash
docker-compose up --scale chrome=1 -d
```

## Observe Selenium Grid Run (Including Built-In VNC Viewer)
```
http://localhost:4444/ui/index.html#/sessions
```

## Run
```bash
export BROWSER=chrome && python cortexaai_cli.py
```

## Tests
```bash
export BROWSER=chrome && python -m unittest discover
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
