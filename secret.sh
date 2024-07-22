#!/bin/bash
# ensure that python environment is setup correctly

python ./airesumeeditor/main_server.py &
python ./airesumeeditor/featureextractors/embedderserver.py &
python ./airesumeeditor/latexeditor/resume_server.py &
python ./airesumeeditor/llmserver/llm_server.py &
