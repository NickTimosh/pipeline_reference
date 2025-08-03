# pipeline_reference
Code from Data Pipeline Pocket Reference

### 🔧 Project Setup

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate

# Ignore the virtual environment in Git
echo venv/ > .gitignore

# Install necessary Python packages
pip install configparser
pip install boto3

# Create an empty configuration file
echo. > config.conf
```

### Extract From MySQL

```bash
# Install library
pip install pymysql
```