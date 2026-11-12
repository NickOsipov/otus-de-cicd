#!/bin/bash

ruff check src config tests
isort --check-only --profile black src config tests
black --check src config tests
