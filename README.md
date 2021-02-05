<h1 align="center">Welcome 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> An ICD API Endpoint Application (PYTHON)

### ✨ [Demo](http://157.230.189.70:8000/admin)
### ✨ [API] http://157.230.189.70:8000

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Essential](#essential)

## About The Project

- RESTful API that can allow us to utilize an internationally recognized set of diagnosis codes.
- ● Create a new icd version
- ● Create a new diagnosis code record
- ● Edit an existing diagnosis code record
- ● List diagnosis codes in batches of 20 (and paginate through the rest of the record)
- ● Retrieve diagnosis codes by ID
- ● Delete a diagnosis code by ID

### Built With

This project utilizes the following underlisted technologies

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)
- [Postgresql](https://www.postgresql.org/)

<!-- GETTING STARTED -->

## Getting Started

To get up and running with the project follow the instructions below

### Prerequisites

- Python - download the latest version of python from the official documentation depending on your os
  NB: use python version greater than 3

- Pip, Pipenv

```sh
pythom3 -m install pip pipenv
```

- Postgres - Required if you want to access database. Visit https://www.postgresql.org/download/macosx/ to download
### Installation

```sh
brew install postgres
```

1. Clone the repo

```sh
git clone https://github.com/xelahaippa/icdapp.git
```

2. Install all general dependencies

```sh
cd icdapp
pipenv shell
pip install requirements.txt
```

2. Migrate DB

```sh
pythom3 manage.py makemigrations
python3 manage.py migrate
```

## Usage

- Once everything is done properly run `npm start`
- Successful running of this command should spill out `Starting development server at {url}` in your terminal
