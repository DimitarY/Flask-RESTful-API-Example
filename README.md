# Flask RESTful API with version

 RESTful API for...

# Introduction

In this example, you'll see how to write an API in Flask and different ways to handle requests.

## Features:

- Simple flask application using application factory, blueprints
- Authentication using [Flask-JWT-Extended](http://flask-jwt-extended.readthedocs.io/en/latest/) including access token and refresh token management
- Configuration using environment variables
- OpenAPI Swagger UI

Used packages :

- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
- [flask-swagger-ui](https://github.com/sveint/flask-swagger-ui)
- [cryptography](https://cryptography.io/en/latest/)

# Installation

This project requires the use of the Python environment, which allows us to create a consistent and isolated environment for the project. So we will install Python with Anaconda and create virtual envierment, in witch we will save our envierment variables and install specific python packeges.

### Install Python

#### Windows

1. Go to the [Python](https://www.python.org/downloads/windows/) download page for Windows
2. Click on the latest version of Python.
3. Open the installer and follow the instructions. Make sure to select the **Add Python to PATH** option during the installation process.

#### Linux

1. Open a terminal window.
2. Enter the following command to update the package list:
   ```
   sudo apt-get update
   ```
3. Enter the following command to install Python:
   ```
   sudo apt-get install python3
   ```

#### macOS

1. Go to the [Python](https://www.python.org/downloads/mac-osx/) download page for macOS
2. Click on the latest version of Python.
3. Open the installer and follow the instructions. Make sure to select the **Install for all users** and **Add Python to PATH** options during the installation process.

### Install Anaconda

#### Windows

1. Go to the [Anaconda](https://www.anaconda.com/products/distribution) download page.
2. Select the latest version of Anaconda for Python 3.x for Windows and click on the "Download" button.
3. Open the downloaded executable file and follow the instructions in the Anaconda installer.
4. During the installation process, you can choose whether to add Anaconda to your system path and whether to make Anaconda your default Python distribution. Choose Anaconda to your system path.

#### Linux

1. Go to the [Anaconda](https://www.anaconda.com/products/distribution) download page.
2. Select the latest version of Anaconda for Python 3.x for Linux and click on the "Download" button.
3. Open a terminal window and navigate to the directory where the Anaconda installer was downloaded.
4. Use the following command to install Anaconda:
   ```
   bash Anaconda[version]-Linux-x86_64.sh
   ```
   Replace [version] with the version number of the Anaconda installer you downloaded.
5. Follow the instructions in the Anaconda installer.

#### macOS

1. Go to the [Anaconda](https://www.anaconda.com/products/distribution) download page.
2. Select the latest version of Anaconda for Python 3.x for macOS and click on the "Download" button.
3. Open the downloaded executable file and follow the instructions in the Anaconda installer.
4. During the installation process, you can choose whether to add Anaconda to your system path and whether to make Anaconda your default Python distribution. Choose Anaconda to your system path.

### Set Up a Virtual Environment

1. Open the Terminal app.
2. Navigate to the directory where you want to create the virtual environment (project directory).
3. Create a new virtual environment for your project by running the command:
   ```
   conda create --name my_env
   ```
   Replace "my_env" with the name you want to give to your virtual environment.
4. Activate the virtual environment by running the command:
   ```
   conda activate my_env
   ```
   Replace "my_env" with the name of your virtual environment.
5. Once you're done working with your project and want to deactivate the virtual environment, you can run the command:
   ```
   conda deactivate
   ```

# Configuration

1. Activate the environment in which you want to add the environment variable. You can do this by running the following command in the terminal or command prompt:
   ```
   conda activate my_env
   ```
   Replace "my_env" with the name of your environment.
2. Run the following command to install the packages specified in the requirements.txt file:
   ```
   conda install --file requirements.txt
   ```
   This will read the requirements.txt file and install all the packages listed in it.
3. After the installation is complete, verify that the packages are installed by running the following command:
   ```
   conda list
   ```
4. Run the following command to set the environment variables:
   ```
   conda env config vars set SSL_CERTIFICATE_PATH=/path/to/directory
   ```