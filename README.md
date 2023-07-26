# E-commerce Site Test Framework - Base

This repository contains an automated test framework base, designed for an e-commerce site built with WordPress and WooCommerce. The site utilizes the StoreFront theme and features both frontend and backend tests.

This repo is to serve as a base to write add more tests and practice QA Automation.

There are only 16 automated tests included in this base repo.

## Features

- **Python:** The tests are written in Python using the pytest framework.
- **Frontend Testing:** Selenium WebDriver is employed for frontend testing, allowing comprehensive validation of the user interface.
- **Backend Testing:** Backend tests are included to ensure the proper functioning of the WooCommerce API and other backend functionalities.
- **WordPress & WooCommerce:** The framework is tailored specifically for WordPress websites integrated with WooCommerce, enabling seamless testing of e-commerce site features.


## Prerequisites to run the tests
* You must have the E-Commerce site running
* The site must be created with WordPress & WooCommerce
* The site must be using the "StoreFront" theme
* For a tutorial on how to create a site to run these tests on, watch these videos
  * [Creating Ecommerse Site for Testing - Part 1](https://www.youtube.com/watch?v=KhLGXIxeJLI&t=1s&ab_channel=SuperSQA)
  * [Creating Ecommerse Site for Testing - Part 2](https://www.youtube.com/watch?v=w47JR3aoTNw&ab_channel=SuperSQA)
  * [Creating Ecommerse Site for Testing - Part 3](https://www.youtube.com/watch?v=qwCY8UEWqqM&ab_channel=SuperSQA)

## Steps for setting up the framework and running tests

### Clone the code
```
git clone https://github.com/supersqa1/demostore-pytest-base.git
```

Navigate to the cloned directory
```
cd demostore-pytest-base
```

### Create virtual environment and install requirements
Create a virtual environment
```
python3 -m venv ssqatest_venv
```

### Activate the virtual environment 
  - On Mac/Linux
    ```commandline
    $ source  ssqatest_venv/bin/activate
    ```

  - On 'Windows CMD'
    ```commandline
    C:\..\Scripts\activate.bat
    ```

  - On 'Windows PowerShell'
    ```commandline
    C:\..\Scripts\Activate.ps1
    ```
### Install requirements in the virtual environment
```commandline
python3 -m pip install -r requirements.txt
```

### Set environment variables
There are variables required by the framework. 
The Easiest way to set the variables is to set them in a file and source the file.

For 'Mac/Linux' systems, update and run the 'variables_local.env' file for your own site.

```
source <path to file>/variables_local.env
```

For 'Windows' using 'CMD' run the 'variables_local.bat' file.
```commandline
<path to file>\variables_local.bat
```

Here are the variables that must be set
(For Windows on CMD replace 'export' with 'set')
```commandline
# BASE_URL is 'localhost' if you are running on your machine. 
# If running tests in Docker container use your local ip address instead of localhost. 
# And make sure you update you site's url at "WordPress > Settings > General"
export BASE_URL=<your website url> 
export BROWSER=<browser type>
export DB_PORT=<your database port, if using MAMP most likely 8889 or 3306>
export DB_HOST=<your database host, usually localhost if running on local>
export DB_DATABASE=<data base name. you usually create this when you created your wordpress site>
export DB_TABLE_PREFIX=<your site's database tables prefix. Usualy _wp if you left it defaut

# credentials (these should not be kept in source controle like GitHub)
export WOO_KEY=<your woocommerce api key>
export WOO_SECRET=<your woocommerce api secret>
export DB_USER=<your database user>
export DB_PASSWORD=<your database password>
```

Example:
```commandline
export BASE_URL=http://localhost:8888/localdemostore/
export BROWSER=chrome
export RESULTS_DIR=$(pwd)/results
export DB_PORT=8889
export DB_HOST=localhost
export DB_DATABASE=localdemostore
export DB_TABLE_PREFIX=wp_
# credentials (these should not be kept in source controle like GitHub)
export WOO_KEY=ck_173049470988979798abedf1b34979a6fc437bd2da634
export WOO_SECRET=cs_38fc1985b37f17ffcoi987adf098adf65adf01c347
# credentials for the wordpress/mysql database
export DB_USER=root
export DB_PASSWORD=root
```

## Run tests
#### To run all tests
** Make sure virtual environment is active
** Set PYTHONPATH variable
** Explore the 'runner.sh' (For Mac/Linux) and consider using it.

```commandline
export PYTHONPATH=/<path>/<to>/demostore-pytest-base
cd demostore_automation
python3 -m pytest tests
```
Try the runner.sh script.
```commandline
bash runner.sh demostore_automation/tests
```
#### To run frontend tests
```commandline
cd demostore_automation
python3 -m pytest tests/frontend
```
#### To run backend tests
```commandline
cd demostore_automation
python3 -m pytest tests/backend
```

#### To run specific test by id
```commandline
cd demostore_automation
python3 -m pytest tests -m tcid33
```
