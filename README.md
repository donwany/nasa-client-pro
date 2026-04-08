## Prepare environment
```bash
mkdir nasa-client
cd nasa-client
uv init --package nasa-client-pro --python=3.14
uv venv
source .venv/bin/activate
```

```bash
touch main.py  
```
## Create .env file
```bash
touch .env .gitignore

# Add your NASA_API_KEY API key to the .env file
echo "NASA_API_KEY=your_api_key_here" >> .env
```

```bash
cd src/nasa_client_pro
touch client.py
```

### Add packages
 - https://github.com/Delgan/loguru.git
 - https://github.com/psf/black.git
 - https://github.com/theskumar/python-dotenv.git
```bash
uv add requests python-dotenv loguru black
```

####  `from .client import NASAClient`
  - makes it easy to `import`
  - . means from the current package
  - go inside client.py and import NASAClient
  - without it, users would have to write
    - `from nasa_client_pro.client import NASAClient`
  - with it, users can simply write
    - `from nasa_client_pro import NASAClient`
 
#### `__all__=[NASAClient]`
  - this controls what gets exported publicly from your package
  - think of it like a `public API whitelist`
  - if someone does `from nasa_client_pro import *` (cleaner, more user-friendly API)
    - only things listed in `__all__` will be imported

### Bonus: what happens without `__all__`?

### Format code
```bash
black main.py
black src/nasa_client_pro/*.py
```

## Git
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<USERNAME>/nasa-client-pro.git
git push -u origin main
```

## Run Locally
```bash
uv run main.py 
```

## Build Package
```bash
uv add build twine
```

## Build and Publish to PyPI
- Go to: https://pypi.org/manage/account/token/
```bash
# build project
uv build

# publish project
export UV_PUBLISH_USERNAME="__token__"
export UV_PUBLISH_PASSWORD="pypi-AgEIcHlwaS5vcmcCJ..."
uv publish

# another
export PYPI_TOKEN="pypi-AgEIcHlwaS5vcmcCJ..."
uv publish --username __token__ --password $PYPI_TOKEN

# another
uv publish --username __token__ --password "pypi-AgEIcHlwaS5vcmcCJ..."

# using twine: https://twine.readthedocs.io/en/stable/
export TWINE_USERNAME=__token__
export TWINE_PASSWORD="pypi-AgEIcHlwaS5vcmcCJ..."
twine upload  dist/*

twine upload dist/* --verbose --username __token__ --password "pypi-AgEIcHlwaS5vcmcCJ..."

# debug trick
uv publish https://test.pypi.org/legacy/ --username __token__ --password $PYPI_TOKEN
```

## Install Wheel Files
```bash
pip install dist/nasa_client_pro-0.6.0-py3-none-any.whl
uv tool install dist/nasa_client_pro-0.6.0-py3-none-any.whl
```

## USAGE
 - `pip install nasa-client-pro` or `uv add nasa-client-pro --upgrade`
 - export NASA_API_KEY=tYYvy2MZehnbOAY5t...
```python
import os
from nasa_client_pro import NASAClient
from dotenv import load_dotenv
from loguru import logger

# load_dotenv(".env", override=True)
NASA_API_KEY = os.getenv("NASA_API_KEY")

def main():
    # --- Usage (Clean and simple) ---
    nasa = NASAClient(api_key=NASA_API_KEY)

    # 1. Get the cool space photo of the day
    logger.info("Fetching APOD...")
    pods = nasa.get_apod(start_date="2026-04-01", end_date="2026-04-06")
    # print(pod)
    for pod in pods:
        print(f"Today's Title: {pod['title']}")
        print(f"Today's URL: {pod['url']}")
        print(f"Today's Explanation: {pod['explanation']}")
        print(f"Date: {pod['date']}")
        print("-"*100)

    print("-" * 100)
    # 2. Check for "Space Rocks" near us
    logger.info("Searching for asteroids...")
    asteroids = nasa.search_asteroids("2026-04-01", "2026-04-06")
    print(f"Found: {asteroids['element_count']} asteroids this week!")

if __name__ == "__main__":
    main()
```
