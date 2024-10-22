Facundo Mala Ingenieria Informatica UM

# Ajedrez-2024-facundomala1

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-facundomala1/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-facundomala1/tree/master)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/be821d44247a5ef3296b/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-facundomala1/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/be821d44247a5ef3296b/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-facundomala1/test_coverage)

## How to Play Using Docker
### Prerequisites
- You need to have Docker installed.

- Steps to Run the Game in Docker.

Clone the repository:

git clone https://github.com/um-computacion-tm/ajedrez-2024-facundomala1.git

-Build docker image:
docker buildx build -t game-chess .

-Run the game:
docker run -it --name prueba game-chess

-Test:
coverage run -m unittest && coverage report -m && python -m main