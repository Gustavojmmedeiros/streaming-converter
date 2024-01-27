# Streaming Converter

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Gustavojmmedeiros/streaming-converter/total)
![Python Version](https://img.shields.io/badge/Python-3.12-blue)
<!-- TODO: Add this badge with Github Actions: https://shields.io/badges/git-hub-actions-workflow-status -->

This project aims to be a simple way to help people transfer playlists between the main music streaming
platforms out there.

## Features

- Transfer musics between Spotify, Deezer and Youtube Music
- Dry-run option in order to understand if is worth to change the provider

## Running the application

TODO

## Contributing and Feedback

Contributions on this project are always welcome. There are many ways we can help evolve this project.

1. You can file a BUG to report any problem that you find in the application;
2. You can also create any discussion on the proper tab, this will be the place that things will be discussed
before project maintainers create the appropriate issue.
3. You can also create a pull request implementing changes from an issue.

We suggest reading our [CONTRIBUTING guide](CONTRIBUTING.md) for more information about how to contribute
properly.

## Roadmap

See our _projects_ board in order to understand more about the next steps of the project.

## Setup your local environment

For those who want to contribute, this project comes with a full featured Development Container that can be
used in any IDE that supports this feature. If you don't know about DevContainers please
read [Development Containers](https://containers.dev/) for an overview and specification. You can also use
the Docker container within the [.devcontainer](.devcontainer/) folder.

In case you want to run this project without this feature you will need to have Python installed. We
recommend the use of PyEnv in order to better manage your Python Version. See
[Pyenv: Installation](https://github.com/pyenv/pyenv#installation). For dependency management
[Poetry](https://python-poetry.org/), please follow
[Poetry: Installation](https://python-poetry.org/docs/#installation) to setup on your machine.

With everything installed, you just need to install the dependencies, this can be done by running the
following command:

```shell
poetry install
```

## Running Tests

To run tests, run the following command

```bash
  make test
```
