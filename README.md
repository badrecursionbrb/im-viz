# IM-Viz Web-app
Processmining web application for displaying internal steps of the Inductive Miner

The tool is publicly accessible here: https://im-viz.informatik.uni-mannheim.de

# README

# TODO CHECK FOR PRODUCTION
1. set logging level accordingly (front-end and back-end)
2. set debug = False in flask app 
3. set new secret key in python flask main.py
4. When cloning from github onto a server change the constants in `/im-app/src/assets/constants.js` according to your set up, i.e. most importantly IP address / domain name and the port.  
5. Assure the firewall is configured properly (e.g. firewalld or ufw), also that CORS (in the back-end) is configured properly

# How to install? 
1. Having npm / node.js installed: 
Manual:
```
https://kinsta.com/blog/how-to-install-node-js/
```

**Download & install node js from here**
```
https://nodejs.org/en/download
```
2. verify node / npm (node package manager)
```
npm --version
Node --version
```

3. check-out (clone) this project to the folder of your choice 

4. Have Python version 3.9+ installed (3.8+ may also be fine)
5. In the venv folder in 
```
im-viz/pythonproject/venv/Script/
```
execute the **activate** file to activate the virtual environment (venv)
select the venv python executable in ...../venv/Scripts/ and execute the setup.py like in the following line: 
```
python setup.py install
```
**OR**
run the setup.py file in the pythonproject folder manually using the venv python.exe

When navigated into the folder of the python.exe: 
```
.\python.exe ..\..\setup.py install
```

6. Clone the contained project (pm4py fork) with the venv:
```
pip install -e git+https://github.com/badrecursionbrb/pm4py-core.git#egg=pm4py
```
7. Execute the flask_app.py using the venv 

## Now back to the front-end: 
8. Open another terminal instance, as the old one is now running the back-end (can already be tested using Postman)
9. navigate to 
*im-viz/im-app/*

10. then, to install the node modules, execute:
```
npm install 

or 

npm i
```


11. Run the production build with: 
```
npm run build
```
then follow the instructions: https://cli.vuejs.org/guide/deployment.html


12. To compile the fron-end and start the app run (this always has to be run when the app is (re)started, otherwise autocompiles if front-end is changed): 
```
npm run serve
```

13. Lints and fixes files
```
npm run lint
```

14. Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Vue dependencies

The following list is listed here for the sake of completeness. The application should install with the provided package list in the package.json
```

####
npm i @fortawesome/fontawesome-free

npm i --save @fortawesome/fontawesome-svg-core

#### Free icons styles
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/free-regular-svg-icons
npm i --save @fortawesome/free-brands-svg-icons

npm i --save @fortawesome/vue-fontawesome@latest-3
npm install @mdi/font
#### More dependencies


npm install @mui/material @emotion/react @emotion/styled
npm install @fontsource/roboto 
npm install @mui/icons-material

npm install webcola --save
npm install -g grunt-cli
npm install -g http-server

also needed for material ui: 
npm init @eslint/config

npm install d3

npm install axios

npm install vuetify
npm install html2canvas
npm install jspdf --save

npm install vue3-picture-swipe
```

## How to install the Python back-end: 

Run the *setup.py* in the subfolder *pythonproject* (if not already done in the previous steps above)

 if the installation of the contained modified PM4PY project does not work, try: pip install -e git+https://github.com/badrecursionbrb/pm4py-core.git#egg=pm4py

*Is also for editing the contained modified pm4py forked project* 

## How to debug Flask: 

Two ways: 
1. set debug=True in flask_app.run() call in flask_app.py (reloads if code is changed! --> good)
2. set debug=False in flask_app.run() call in flask_app.py AND then debug with vscode, enables breakpoints! 


## How to extend the Application? 

1. There are two projects actually: 
    - First there is this main project having the python back-end using a Flask API running on Gunicorn 
        and the front-end using Vue with Vuetify and Axios for requests  
    - Second there is the project that is a fork of PM4PY. Within that project the changes that 
        are needed on the inductive miner implementations are done. 

2. The second project is contained as a package in the src folder in the virtual environment (venv)
    - To extend the project to more algorithms additionally to the changes that might be needed in 
    the front-end, e.g. like parameter settings, there need to be changes in the backend. 
    - It may be necessary to add a json file to have other cases of the inductive miner algorithm 
        or a different description of the algorithm. This description is then edited in a json file 
        in the assets folder.  
    - Firstly in the API so the flask_app.py file, to unpack parameters. 
    - Secondly in the main.py file a case for the new algorithm variant is needed   
    - Most importantly then in the second project (the fork of the PM4PY project) the 
        algorithm_modified_v2.py file has to be modified.
        - a new Variant has to be added to the Enum 
        - the case has to be handled in the apply function of that file 
    - Then a modified version of the algorithm has to be created like the imf_custom.py or 
        im_custom.py, there it is necessary to look for all the places where the algorithm descends
        into the tree i.e. a step is done, at each step a pt_node attribute is written in the 
        ProcessTree object that is created and returned by the IM algorithm implementations
        It is very important to write the DFG in the parameters. 
    - It may also be that there are changes needed in the visualization data objects. That depends 
        on the requirements of the IM algorithm algorithm. 

