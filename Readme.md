# Playstation Bot

It is really getting hard to get hands on a PlayStation 5 these days. The stock sells over in a second or never appears on any retailer's website.

This bot is designed to scan for stock inventory on targetted websites and add the console to a cart. Then it will alert the user to check out the product and vola!!!

## Pipeline

1. Setup basic project structure on GitHub.
2. Get a framework ready which covers all the priorities.
3. Test API vs Web scrapping for targetted websites.
4. Setup both API scrapping and web interaction to add the product to cart.
5. Setup quality unit tests that check the required functions.
6. Test the entire bot over different products on each of the retailers websites.


## Setting up development environment

* Setup the recommended extensions for the workspace. These are included as a part of workspace recommendations in VS Code.
* Setup Python 3.6 and above on your windows system.
* Running powershell scripts might be disabled by default in Windows 10. In that case, open cmd as Administrator and enter ``powershell Set-ExecutionPolicy RemoteSigned``.
* Select base python interpreter as the default interpreter in VS Code.
* Open a new VS Code terminal.
* Type ``C:\Users\<username>\.virtualenvs`` in the terminal.
* Type ``python -m venv <name of the environment>`` in the terminal.
* This will create a python virtual environment at standard virtual environment folder in Windows.
* If the above location is already added to list of folders where to look for venv in Python extensions, the newly created venv should be listed when attempting to selct a virtual environment.
* Close the VS Code terminal and open a new terminal. This time it should open with the activated environment in the terminal window.
* On the activated environment, run ``python -m pip install –-upgrade pip`` to upgrade the version of pip.
* All the project dependencies are listed in requirements.txt file at the project root. Use ``pip install -r requirements.txt`` to install all the dependencies at the same time.
* Use ``pip list`` to check if all the required packages are installed successfully.
