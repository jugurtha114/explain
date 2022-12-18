# explain

Explain your error message in plain English using ChatGPT. Just run your file with the `explain` command.

![Demo](demo.gif)

## Installation

You can install `explain` with pip:

```bash
$ pip3 install explain
```

## Usage

Running a file with `explain` is just as easy as running it normally:

```bash
$ explain [file_path]
```

This will execute the file and, if an error is thrown, send the stack trace to ChatGPT and display its explanation in your terminal.

Note that when you first use `explain`, you'll be asked to enter your OpenAI credentials.

__Supported file types:__ Python, Node.js, Ruby, Golang, and Java.
