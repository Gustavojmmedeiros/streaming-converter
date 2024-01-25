# Contributing Guide

Thanks to be interested in contributing! If not already, we encourage you to look into our
[README](README.md) for some overview of the project. The next sections will guide you on how to better
contribute with this project.

1. [Style Guide](#style-guide)
1. [Best Practices](#best-practices)
1. [References](#references)

## Style Guide

This project follows the styleguides for each tool as listed below. These guides have precedence over any
other rule written here:

- For **Markdown** and **Shell Scripts** we follow Google's Styleguide as described on
[Google's Markdown Style Guide](https://google.github.io/styleguide/docguide/style.html) and
[Google's Shell Style Guide](https://google.github.io/styleguide/shellguide.html);
- For **YAML** the rules are automatically evaluated on pre-commit as described on
[yamlint configuration](.yamllint). You can read
[yamlint: rules](https://yamllint.readthedocs.io/en/stable/rules.html) for details about each rule.
- For **Python** we follow [PEP8](https://peps.python.org/pep-0008/) rules and for docstrings we adopted the
Google's convention as described on
[Google Python Style Guide: 3.8 Comments and Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

For any other case, the following rules apply:

- Use **kebab-case** when naming folders and files;
- No more that **110 characters** per line, this is to ensure a good readability of the code. URLs and tables
are the only exception for this rule;
- No **Trailing whitespaces** on the end of the lines;
- Always end the file with a **blank line**;
- When writing documentation use angled brackets ("<>") for places where the user needs to interact. For
For example, `command <PARAMETER>`;
- Always set **fixed versions** for packages, tools and anything that could be versioned;

## Best Practices

Below are some references for best practices from tools, languages and related technologies of this project.

- [Docker: Development best practices](https://docs.docker.com/develop/dev-best-practices/)
- [Docker: Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker: Security best practices](https://docs.docker.com/develop/security-best-practices/)

## References

- [Wrangling Web Contributions: How to Build a CONTRIBUTING.md](https://mozillascience.github.io/working-open-workshop/contributing/)
- [Awesome Guidelines](https://github.com/Kristories/awesome-guidelines)
- [Github: Contributing Guide](https://github.com/github/docs/blob/main/CONTRIBUTING.md)
