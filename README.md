# cyberion
AI voice assistant powered by ChatGPT

---

## Getting started
On your first run...
```bash
python manage.py migrate 
```

To create a superuser (optional).
```bash
python manage.py createsuperuser 
```

To run the server locally...
```bash
python manage.py runserver
```

---

## Development

If you are using VS code, it is recommended to use the settings below in your `launch.json`.
This file should be placed within the `.vscode` directory.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "debugpy",
            "request": "launch",
            "cwd": "${workspaceFolder}",            
            "program": "${workspaceFolder}\\manage.py",
            "python": "${workspaceFolder}\\venv\\Scripts\\python.exe",
            "console": "integratedTerminal",
            "args": ["runserver", "--noreload"],
            "envFile": "${workspaceFolder}\\.env\\dev.env",
            "django": true,
            "justMyCode": true
        },
        {
            "name": "Celery",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "cwd": "${workspaceFolder}",            
            "console": "internalConsole",
            "args": ["-A", "cyberion", "worker", "-l", "info", "-P", "solo"],
            "envFile": "${workspaceFolder}\\.env\\dev.env",
        },
        {
            "name": "Beat",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "cwd": "${workspaceFolder}",            
            "envFile": "${workspaceFolder}\\.env\\dev.env",
            "console": "internalConsole",
            "args": ["-A", "cyberion", "beat", "-l", "info"]
        }
    ],
    "compounds": [
        {
            "name": "Django-Celery",
            "configurations": ["Django", "Celery"],
            "stopAll": true
        },
        {
            "name": "Django-Celery-Beat",
            "configurations": ["Django", "Celery", "Beat"],
            "stopAll": true
        }
    ]    
}
```

Create a file named `dev.env` and place it within the directory `.env`
You can use the file `example.env` in there as a template.