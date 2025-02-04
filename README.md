<img alt='banner.png' src='./banner.png' width="100%">

```txt
An app that contains manga and stories from some sources in one place!
```

## Table of Contents
- [Important Notes](#important)
- [Features](#features)
- [Python Setup](#python-set-up)
- [Set-up](#set-up)
- [Running Project](#running)
- [Creating an Admin User](#admin-user)
- [Contributions](#contributions)
- [License](#license)

## Important
### This is a Django application
> [!IMPORTANT]
> It is recommended that the user is familiar with Django framework.
>
> Check out https://www.djangoproject.com/start/ for more.

### Redis caching is used
> [!IMPORTANT]
> It is *required* to know how to set-up a Redis server up-and-running, as the app **won't** run
> correctly.
> 
> Check out https://redis.io for more.

## Features
Here are some of the features that this app is capable of:
- Get details about indivitual series
- Preview chapters of multiple series
- Download individual chapters onto your system
- Login / Sign up on a personal account
- Track your most recently visited series
- Re-visit already visited series
- Use URLs to extract a series
- Search keywords and obtain results
- Currently works with **bato.to** and **MangaDex**

## Python Set-up
> [!NOTE]
> This app supports Python version **3.10** and above.
> 
> Latest version of PIP is recommended for requirement installation.

Here are instructions for installation on a **Linux** machine.

### Linux
#### Install using APT installer
1) Open the Linux Terminal by pressing **CTRL - ALT - T**, or typing `terminal` in the system search.

2) Start by updating the list of available packages by typing
```bash
$ sudo apt update
```

3) Install your preferred version of Python **[3.10+]** by typing
```bash
$ sudo apt install python3.10
```

4) To make sure that Python downloaded correctly:
```bash
$ python3
```

If this doesn't work, explicitly type the Python version you downloaded
```bash
$ python3.10
```

The interactive Python shell should open in the terminal, if it does then Python is installed correctly.

Press **CTRL - C** to close the shell.

5) Install PIP
- If you haven't done so, type `sudo apt update`
- Then, to install the PIP installer type
```bash
$ sudo apt install python3-pip
 ```

## Set-up
### Installations
- Make sure that Python is installed on your machine, check *<a href="#python-set-up">here</a>* if it isn't.

    - Make sure `virtualenv` is installed on your machine, to install type
        Open up the terminal, type
        ```bash
        $ pip3 install virtualenv
        ```

        If this doesn't work, follow the steps in this [*website*][2].
    
    - Navigate into your desired directory, then create a new virtual environment by typing
    ```bash
    $ virtualenv --python3 [name-of-env-here]
    ```

    - Activate the environment in the *current* terminal, type
    ```bash
    $ source [name-of-env-here]/bin/activate
    ```

- Install Git, follow the steps [here for Linux][5].

- Install Redis, follow the steps [here for Linux][7].

> [!IMPORTANT]
> Any further installations are to be within the recently created **environment**.
>
> Whenever the developement server is run, it **must** from the **same** environment that will be setup now.

- Install Django, type
    > [!NOTE]
    > (env-name) here will be with same name as your environement *if activated*.

    ```bash
    (env-name)$ pip3 install Django
    ```

    If you encounter any issues, visit the official Django [*installation guide*][3].

- Install required libraries/dependancies, type
```bash
(env-name)$ pip3 install -r requirements.txt
```

- Start a new Django project
    - Navigate to the directory that you want the project to be contained in
    - Type
        ```bash
        (env-name)$ django-admin startproject [project-name-here]
        ```
    - Navigate into the project
        ```bash
        (env-name)$ cd [project-name-here]
        ```

- Clone app from repository (Example using SSH)

    Make sure that you have navigated **inside** the project directory, type 
    ```bash
    (env-name)$ git clone git@github.com:acskii/comfy-reader.git
    ```

### Settings
1) Navigate to `reader/`, and open up `settings.py` in a code editor of your choice.
2) There are **three** that need to be checked
    - **Database**
        During development, the app used a **local SQLITE3** database, which could be left unchanged. \
        Another option is to replace the information in this section to accomodate a cloud database e.g. Postgre server \
        Instructions on how to setup a cloud database with be added soon, but if you already have previous knowledge on this technology then feel free to implement it.

    - **Caching**
        After running a Redis server (instructions found <a href="#running">*here*</a>), add in the local address and port in this setting.
        ```python
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.redis.RedisCache',
                'LOCATION': 'redis://127.0.0.1:6379',       # change based on local host 'redis://{host}:{port}'
            }
        }
        ```
        > [!IMPORTANT]
        > **DON'T** use browser cache/cookies, as cache data is larger than the maximum limit of **>4KB**\
        > Redis was the solution to this problem.
    
    - **Internationalization**
        Edit the `TIME_ZONE` variable into your prefered timezone.

## Running
1) Start up the Redis server
```bash
$ sudo systemctl start redis-server
```
> [!NOTE]
> To close the local server:
> ```$ sudo systemctl stop redis-server```

2) Navigate to the project directory, type
```bash
(env-name)$ python3 manage.py runserver
```

3) Open up your browser, and type in the URL provided in the terminal screen (*likely* `127.0.0.1:8000`)

## Admin User
Navigate to the project directory, type
```bash
(env-name)$ python3 manage.py createsuperuser
```
Type in your username, email, and password.\
You can use them to login on the app.

## Contributions
This is a personal project of mine, but feel free to suggest improvements, share insights, or discuss challenges.

## License
This repository is licensed under the **GNU General Public License v3.0**.

[1]: https://www.python.org/downloads/windows/
[2]: https://virtualenv.pypa.io/en/latest/installation.html#via-pip
[3]: https://docs.djangoproject.com/en/5.1/topics/install/#installing-an-official-release-with-pip
[4]: https://git-scm.com/downloads/win
[5]: https://git-scm.com/downloads/linux
[6]: https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
[7]: https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/