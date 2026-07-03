# Steps to setup the application

Hello fellow contributors! If you feel lost, or hesitate to ask me and Tejal, you can see it here.

Once you clone the repository (the good looking guy conducting the workshop would have explained you how by now) you can do the following to setup the application.

> make sure you read the setting up WSL on your system doc and also make sure you are doing all this INSIDE WSL.

Once you are in the repository's folder, quicky create a virtual environment for Python:

```bash
python -m venv .venv
```

`source` your virtual environment into the shell:

```bash
source .venv/bin/activate
```

Once that's done, install the required dependency libraries for the application:

```bash
pip install -r requirements.txt
```

Once that's done, go ahead with running the application:

```bash
python app.py
```
The site will be accessible at [http://localhost:5000](http://localhost:5000)
## Docker Image creation
Build the image
```bash
docker build -t first-contribution:v1 .
```
and run it
```
docker run -p 5000:5000 --name workshop-app first-contribution:v1
```
execute `docker ps` and see if the container is running. If yes, the site will be accessible at [http://localhost:5000](http://localhost:5000). If not, call me :).

## GitHub CLI installation and Git auth setup
Use the following command to install GitHub CLI (copy paste the full code block)

```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

Once you do that, login to GitHub with this
```bash
gh auth login
```
It will show you a link to login. Open it, login with your GitHub account and setup Git to use the same account.
```bash
gh auth setup-git
```
Now your Git credentials and set.

Now you can proceed with creating a branch, committing your changes, and pusing to the origin in your branch.

All the best.