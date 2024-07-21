#!/bin/bash

PROJECT_NAME="JobSyncer" 

# ---- Check and Install Prerequisites ----
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Please install Docker."
    git pull
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Please install Python 3."
    git pull
    exit 1
fi

python ./airesumeeditor/main_server.py &
python ./airesumeeditor/featureextractors/embedderserver.py &
python ./airesumeeditor/latexeditor/resume_server.py &
python ./airesumeeditor/llmserver/llm_server.py &