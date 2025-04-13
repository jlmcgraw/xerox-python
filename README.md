> [!IMPORTANT]
> I'm looking for a job right now! If you know of any openings that match my skill-set,
> please let me know! You can read my resume over at [resume site](https://cv.dusktreader.dev). Thanks!!

# xerox-python

[//]: # (Add an asciicast)

`xerox-python` is a project template for me to spin up new python projects in about a minute.

> [!WARNING]
> This template is _extremely_ opinionated. It creates a Python project just the way I like.
> It might not be _immediately_ useful for anyone else unless they adapt it to their needs.


## Usage

There are two branches available that each build a different project type:

- `main`: Builds a basic python project
- `fastapi`: Builds a basic FastAPI python project


## Local

Clone this repo:

```
git clone git@github.com:dusktreader/xerox-python
```

Checkout the branch you want (if not main), and then just run `make`:

```bash
make
```


## One line

You can use the following one-line commands to build a project from the selected branch


### `main` branch

```bash
uvx copier copy --trust gh:dusktreader/xerox-python .
```


### `fastapi` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=fastapi .
```


### `flask` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=flask .
```
