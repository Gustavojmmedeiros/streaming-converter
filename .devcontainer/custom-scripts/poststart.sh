#!/usr/bin/env bash
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # No Color

echo -e "\n${YELLOW}Running Post Start Commands...${NC}"

echo -e "\n${BLUE}Upgrading Packages...${NC}"
apt update
apt upgrade -y

echo -e "\n${BLUE}Upgrading Python Packages...${NC}"
export PATH=$HOME/.local/bin:${PATH}
poetry install

echo -e "\n${BLUE}Setup Pre-Commit...${NC}"
poetry run pre-commit install
