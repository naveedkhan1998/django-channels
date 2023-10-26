## Step 1: Check for Git Installation

First, check if Git is already installed on your system:

```bash
git --version
```

If Git is not installed, you can download and install it from the official website: [Git Downloads](https://git-scm.com/downloads).

## Step 2: Clone the Git Repository

```bash
git clone https://github.com/naveedkhan1998/django-channels.git
```

## Step 3: Install `virtualenv`

```bash
pip install virtualenv
```

This command installs the `virtualenv` package, which is necessary for creating isolated Python environments.

## Step 4: Create a Virtual Environment

```bash
python -m venv venv
```

This command sets up a new virtual environment in a directory named `venv`.

## Step 5: Activate the Virtual Environment

### On Windows

```bash
. venv\Scripts\activate
```

### On macOS and Linux

```bash
source venv/bin/activate
```

Activating the virtual environment isolates your Python environment and ensures that you use the packages installed within the environment.

## Step 6: Install Project Dependencies

```bash
pip install -r requirements.txt
```

This command installs the required packages listed in your `requirements.txt` file.

## Step 7: Run Your Project

```bash
python manage.py runserver 0.0.0.0:5000
```
## Additional Notes:

- To run the project, follow the instructions you have for starting the application, which might involve Docker Compose, as indicated in your provided notes.
- You can access the live site using the following link: [Live Site](https://application-fc.18klajjho232.ca-tor.codeengine.appdomain.cloud/)

