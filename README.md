# Payment calculator
Payment calculator script in python for hourly based salaries employees

## Introduction

This repository contains a script to help users calculate the exact payment thatr should be made to employees with flexible working hours based on the day of the week and hour of the day. 

### Requirements

* You only need python 3.7 or greater installed

# Sample Execution & Output

You can import from another script, also use it from command line with or without arguments

Importing from another script/calling as a module

```python
import payment_calculator

# ...
payment_calculator.process_file('example.txt')
# ...
```

If run without command line arguments, using

```
python main.py
```

The script will ask you to input the .txt filename

```
Please input the .txt filename
txt file should be in the same folder of this script.
filename: 
```

If run using file name as first argument

```
python main.py example.txt
```

output should be *simliar* to

```
The amount to pay NAME is: XX USD
The amount to pay NAME is: YY USD
```

### Development Requirements

* To run test you will need pytest installed
```bash
pip install pytest
```

## Development
To run test just run this command in your Console
```bash
$ pytest
```

## Author
- [Cesar Terrero](https://github.com/cesar128)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.