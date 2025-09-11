# Local LLM
This project will run a local LLM model on your own Macbook, using Apple's MLX framework for utilizing the hardware inference, GPU, and unified memory available to it. 

# Prerequisites
Ensure you have Python installed (validated version: 3.13.2). If you have homebrew, you can do this with `brew install python@3.13`

# Setup
0. Review the code in [local-llm.py](local-llm.py), to understand what is about to happen. Comments explain at a high level what is happening, even if you are not familiar with the python language. 
1. Download the files [HERE](/zipball/master) and open the unzipped folder in a terminal. 
2. Optionaly, but recommended: Create a python virtual environment with `python3 -m venv .venv` and then activate it `source .venv/bin/activate`
3. Install the required libraries with `pip install -r requirements.txt`
4. Run the python project: `python3 local-llm.py`
5. Open your web browser to [http://localhost:7860](http://localhost:7860) and chat with the AI.