import json
import os

notebook_path = "/home/mahmoud-elassy/projects/chinook-dwh/explore_notebook.ipynb"

if os.path.exists(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Define the new cell source loading from .env
    cell_source = [
        "import os\n",
        "import pandas as pd\n",
        "from sqlalchemy import create_engine\n",
        "from sqlalchemy import inspect\n",
        "\n",
        "# Load environment variables from .env file if it exists\n",
        "if os.path.exists(\".env\"):\n",
        "    with open(\".env\") as f:\n",
        "        for line in f:\n",
        "            if \"=\" in line and not line.strip().startswith(\"#\"):\n",
        "                key, val = line.strip().split(\"=\", 1)\n",
        "                os.environ[key] = val\n",
        "\n",
        "USER = os.getenv(\"USER\")\n",
        "PASSWORD = os.getenv(\"PASSWORD\")\n",
        "HOST = os.getenv(\"HOST\")\n",
        "PORT = os.getenv(\"PORT\")\n",
        "DATABASE = os.getenv(\"DATABASE\")\n",
        "\n",
        "engine = create_engine(\n",
        "    f\"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}\"\n",
        ")"
    ]
    
    data["cells"][0]["source"] = cell_source
    
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    print("Notebook updated successfully!")
else:
    print("Notebook not found.")
