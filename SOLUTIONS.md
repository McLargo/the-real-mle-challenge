# The real MLE challenge

This challenge is my first ML project, the start of my training as a Machine
Learning Engineering.

I've got couple of jupyter notebooks created by DS, the data and the model
used. With that, I need to accomplish the tasks mentioned in the
[README file](README.md).

This challenge will be reviewed by others MLEs, so it can be improved in the future.

## Challenge 1 - Refactor DEV code

As jupyter notebooks are not the best way to run a production code, I need to
refactor the code into python scripts. The idea is to create different modules
to manage each of the notebooks, so they can be used in pipelines in production.

### Preprocessing module

This module is responsible for preprocessing the data. It contains the code to
read raw data, preprocess and save it in a format that can be used by the model.

I've created few interfaces and at least one implementation, to split the code
into different parts. This way, it can be reused in the future and add more
implementation without major changes in the code. The classes are:

- `DataLoader`: to read the data from the source. It can be used to read the
  data from different sources. Current implementation: `CSVDataLoader`.
- `DataPreprocessor`: to preprocess the data. It contains the code to preprocess
  the data. Current implementation: `AirbnbDataPreprocessor`.
- `DataSaver`: to save the data in a format that can be used by the model. It
  contains the code to save the data in different formats. Current
  implementation: `CSVDataSaver`.

### Train module

Coming soon

## Challenge 2 - Build an API

Coming soon.

## Challenge 3 - Dockerize your solution

Coming soon.

## Getting started

### Requirements

- Python 3.10
- Poetry 2.1.1

### Modules

The project is divided into different modules, each one with its own
responsibility and configuration. The modules are:

- `preprocessing`: the module responsible for preprocessing the data. It
  contains the code to read raw data, preprocess and save it in a
  format that can be used by the model.
- `train`: the module responsible for training the model. It contains the code
  to train the model and save it in a format that can be used by the API.

### Usage

Each module have their own `Makefile` to manage the commands. You can use the
`make` command to run the commands in the `Makefile`. The commands are:

- `make install`: to install the dependencies of the module. It will create a
  virtual environment with poetry and install the dependencies in it.
- `make run`: to run the module. It will run the module in a virtual environment
  with poetry.
- `make test`: to run the tests of the module. It will run the tests in a
  virtual environment with poetry.

## Contribution

Use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) to
your commit messages.

Trunk-based development vs Gitflow.

## Testing

I do believe that unit test are the most important part of a project, to keep
the code clean, and avoid adding breaking code to a piece of software that is
working. A good coverage of the application indicates that services are robust.

Each module has its own tests. The tests are managed by `TODO`.

## CI/CD

TBD.

## Monitoring

TBD.

## Performance

TBD.

## License

TBD.
