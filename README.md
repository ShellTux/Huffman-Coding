# Huffman Coding

## Developing

### Built With

- matplotlib==3.8.0
- numpy==1.26.1
- openpyxl==3.1.2
- pandas==2.1.1
- PyQt5==5.15.10

### Prerequisites

These codebase is written in python with use of python virtual environment
so you need to make sure you have these installed on your system.

#### Installing Python and Python virtual environment

##### Linux

Distro | Command
--- | ---
`Ubuntu/Debian` | `apt install python3 python3-venv pipenv`
`CentOS/Fedora` | `dnf install python python3 pipenv`
`Arch Linux` | `pacman -S python python-virtualenv python-pipenv`

### Setting up Dev

First clone the repo

```shell
git clone git@github.com:ShellTux/Huffman-Coding.git
cd Huffman-Coding
```

To contribute, it's recommended to not commit directly
to the `develop` branch.

Instead branch of the `develop` branch and implement
your feature in that branch.
When you are done, feel free to make a pull request
to merge your feature branch into the `develop` branch

```shell
# Make sure you place yourself in the `develop` branch
git switch develop

# Make sure you have the last updates
git pull

git switch --create your-feature-branch
```

#### Python virtual environment

Next, make sure your are using the python virtual environment.
The virtual environment used in the development of our codebase is called `venv`

##### Using Python environment

Make sure you run these commands in the root of the repo

```shell
virtualenv venv
source venv/bin/activate
```

Or a single command

```shell
virtualenv venv && source venv/bin/activate
```

##### Installing Python Virtual Environment Requirements

All required python packages are listed in the `requirements.txt`

To installed them, simply run the following command:

```shell
pip install --requirement requirements.txt
# Or
pip install -r requirements.txt
```

When done installing,
there is no need to repeat this command to develop to our codebase.

#### Editorconfig

The last step, is to make sure you have the editorconfig
plugin installed in your IDE or text editor of choice.

For our codebase, we take advantage of [`.editorconfig`](https://editorconfig.org/)
file to help maintain consistent coding-style guidelines.

> Now you are ready to go.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the terms of the license.

## Acknowledgements

