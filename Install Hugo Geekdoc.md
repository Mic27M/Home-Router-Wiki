Install Hugo: Geekdoc

1. 

​	just:  

```bash
sudo apt install hugo
```

​		or

​	Install Homebrew:

1.1 Install Requirements

```bash
sudo apt-get install build-essential procps curl file git
```

1.2 Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

1.3 add Homebrew to your PATH and to your bash shell profile script

```bash
test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
test -r ~/.bash_profile && echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bash_profile
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.profile
```

1.4 Install Hugo

```bash
 brew install hugo
```





2.  InstallWebpack

​	2.1 Install Requirements

```bash
sudo apt install npm
```

3.2 install Webpack

```bash
mkdir webpack-demo
cd webpack-demo
npm init -y
npm install webpack webpack-cli --save-dev
```



https://geekdocs.de/usage/getting-started/
