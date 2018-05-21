# Website for DrAdrian.com

All the code and media files for http://dradrian.com.

## Project setup

**Virtual env**
Make your virual environment. There are some ansible playbooks that make this easy with:

```shell
bash bin/setup.sh
```

That will create a virtual environment called dradriancom.

**Install requirements**
```shell
pip install -r requirements.txt
```

## Build project

Build site with hot reloading:

```shell
python build.py
```

The site will be built into site/index.html

Docs for the static site generator: http://staticjinja.readthedocs.io/en/latest/
