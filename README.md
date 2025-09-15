# Local LLM
This project will run a local LLM model on your own Macbook, using Apple's MLX framework for utilizing the hardware inference, GPU, and unified memory available to it. 

# Prerequisites
### MacOS
This code uses frameworks only available on Apple Silicon based macs (M1, M2, etc). This will not work on Intel based macs.
Update to the latest available MacOS version (validated Version: 15.6.1). Minimum MacOS Version: 14.0.

### Python
Ensure you have Python installed (validated version: 3.13.X). If you have homebrew, you can do this with the below command:
```bash
brew install python@3.13
```

# Setup
1. Review the code in [local-llm.py](local-llm.py), to understand what is about to happen. Comments explain at a high level what is happening, even if you are not familiar with the python language. 
2. Download the files [HERE](../../zipball/master) and open the unzipped folder in a terminal. 
3. Optionaly, but recommended: Create a python virtual environment and then activate it.
```bash
python3 -m venv .venv
source .venv/bin/activate
```
4. Install the required libraries.
```bash
pip install -r requirements.txt
```
5. Run the python project.
```bash
python3 local-llm.py
```
6. Open your web browser to [http://localhost:7860](http://localhost:7860) and chat with the AI.