# PeleScript to MaradoScript
This project is a transpiler from PeleScript to MaradoScript.
Working on the Zig version.[^1]

## PeleScript
PeleScript is a programming language designed by the creators of MaradoScript.  
It extremy minimalist and easy to learn.  
IT ONLY HAS ONE KEYWORD:
- `print`

## PeleScript syntax
Here's an example of a PeleScript program:
```pelescript
print "Hello, World!\n"
print "Goodbye, World!"
```
## Requirements
- `python3`
- `maradoscript` [MaradoScript](https://github.com/matteac/maradoscript) 

## Usage
Clone the project:
```bash
git clone https://github.com/matteac/maradoscript_transpiler.git
```
and then you can run it with python3:
```bash
cd maradoscript_transpiler
python3 main.py --input hello.pls --output hello.mrs
```
and now you can run MaradoScript:
```bash
maradoscript -i hello.mrs
```
