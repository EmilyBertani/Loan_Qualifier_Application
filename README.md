# Loan Qualifyer Analyzer

## What this program does

This program allows a customer to input their financial data to determine if they qualify for a loan based on a list of banks with given loan requirements. The financial data includes the customers *credit score*, *montly debt* and *monthly income*, the *loan amount* they are requesting, and the *value* of their home.

This project was created to allow a more user friendly application that allows repeated use with any of the above given data. It also allows the customer to save their data in an easy-to-read spreadsheet if they choose.

---

## Technologies

This program can be run with Mac or PC with the following requirements:

Python 3.7.1

Questionary 0.2.5

Fire 1.15.0

---

## Installation Guide

To install fire, enter in the following prompt in your command line:

`pip install fire`   

More information can be found at [Python-fire](https://github.com/google/python-fire)



To install questionary, enter the following prompt:

`pip install questionary`

More information can be found at [Questionary](https://pypi.org/project/questionary/)

---

## Usage

To run this program, first navigate to your command line.

Type in `conda activate dev` to make sure you are in the dev environment to run the program.

You will then be prompted to enter in the file path to a rate sheet:


![Imgur](https://i.imgur.com/ZvIJZp1m.png?1)

*Hint: If you right click on the file you want to use, you can copy the path and paste into the command line*

Once you have entered in your path, you will be prompted with a series of questions:

![Imgur](https://i.imgur.com/qAlle5qm.png)

This will then calculate your debt-to-income ratio, loan-to-value ratio and the number of loans you qualify for.



You will then be prompted to decide if you would like to save your data as a CSV file, and if so, the desired location you would like:

![Imgur](https://i.imgur.com/cdebtd8m.png)

You can use tab and return/enter, which will show a pop up of your folders to chose the desired location:

![Imgur](https://i.imgur.com/hLgjpgp.png)


Once you have entered in the location, you should then have a CSV file with your qualifying loans!

![Imgur](https://i.imgur.com/iSmLgzgl.png)

---

## Contributors

Emily Bertani

Emily.Bertani.MD@gmail.com

[LinkedIn](https://www.linkedin.com/feed/)

---

## License

MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
