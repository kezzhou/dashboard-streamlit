# Streamlit Dashboard
HHA 507 // Week 12 // Assignment 10

## Description:

In this repository we create a basic example dashboard using Streamlit. Streamlit is one of many sites that allow for convenient dashboard deployment with an easily installed module.

For installation:
- Connect via ssh to your virtual environment of choice (for us, it's Azure)
- $ sudo apt-get update (this is best practice when booting up the vm)
- $ pip3 install streamlit

Once we have installed streamlit in our vm, we can move to VS Code or a coding environment of choice. Here, using the inhouse terminal, we can install streamlit as well for when we import it within our python script. However, this isn't necessary as long as we have streamlit in our testing environment. We can work with pandas as per usual, and framing dataframes and text within simple commands provided by Streamlit's API Reference when creating dashboard elements of choice.

For running the dashboard (in Azure vm):
- $ git clone https://github.com/kezzhou/dashboard-streamlit
- $ cd dashboard-streamlit/
- $ streamlit run streamlit.py
- Navigate to your browser of choice and type your vm's public IP address followed by ":8501"
- Press enter and view your dashboard

We have included screenshots of the running dashboard within the photos folder.

Common issues are addressed in the notes section.


## Resources:

[Department of Health & Mental Hygiene Dog Bite Dataset](https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg)

[Streamlit API Reference](https://docs.streamlit.io/library/api-reference)

## Requirements:

- VS Code/Python Program of Choice
- Chrome/Safari/Browser of Choice
- Azure/GCP/Virtual Machine Service of Choice

For package requirements and dependencies, please refer to requirements.txt and the notes section below.

## Notes:

Many issues can be solved by simply updating and restarting the terminal or creating a new one.

On occasion, when streamlit or mysql or other modules are pip installed, they aren't placed in the correct directory to be accessed from the base directory. When this is the case, users can modify a bash profile, which is a document of commands that is run when the terminal is first booted up. If the terminal is telling the user that streamlit is not found despite successful installation, users can try to modify this bash profile.

Users can do so by:
- $ nano ~/.bashrc
OR
- $ nano ~/.bash_profile
- add "export PATH=$HOME/.local/bin:$PATH" to the end of the document
- restart the terminal
- $ source ~/.bashrc
OR
- $ source ~/.bash_profile

If the user chooses to remedy the issue in this manner, they must always run the source command after booting up their terminals (unfortunately).