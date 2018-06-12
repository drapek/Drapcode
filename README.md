# Drapcode
Own compiler of Drapcode language. This project is developed by ANTLR as frontend (parser and lexer) and LLVM as backend. 
This project is only for educational purposes and will be not developed to stable version. 

## Description
This is compiler implementation of own language called Drapcode. To get used to it I recommend to look into _examples_ folder

# Constrains
* there can't be blank lines between statements
* in math operation of int and double, the int is automatically converted into double 
* conditions are ints only to make the problem simpler
* scope cohesion is guarantee only for 1-nested scope (rest will be developed in the future)

# Features
- [x] IO operations
- [x] int and real numbers
- [x] math operations
- [x] if statements
- [x] scopes
- [x] while loop
- [x] functions

# How to use
```bash
python main.py <drapcode_file> out.ll
clang-6.0 -o <output_filename> out.ll
```

## Requirements
* Python >= 3.6 (f-strings are used)
* packages from requirements.txt (pip install -r requirements.txt)
* llvm >= 6.0


## TLDR Usage Guide

### comments
```python
# this is comment
x = 1 # this is as well a comment
```

### simple assigment
```python
x = 2
y = 2 + 4

```

### Print value
```python
x = 1
shout x
```

### Get value from user
```python
gimme x
```

### mathoperations
available operands:
* "+"
* "-" 
* "/" 
* "*"

example:
```python
x = (2 + 2) * 2
```

### If statement
```python
if x == 4:
    x = -1
    shout x
endif
```

### While statment
```python
var = 2
while var > 3:
    shout var
    var = var - 1
endwhile
```

### Functions
```python
func tmp:
    b = 2
    shout b
endfunc

# execute the function
tmp()
```

## Examples
### Integer IO operations:
```drapcode
x = 2
gimme x
shout x

```

will transform to:
```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [3 x i8] c"%d\00"
@str.2 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 2, i32* %x
%1 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str.1, i32 0, i32 0), i32* %x)
%2 = load i32, i32* %x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), i32 %2)
ret i32 0 }
```

### Float IO operations:
```drapcode
x = 2.0 
gimme x
shout x

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%lf\00"
@str.2 = constant [4 x i8] c"%f\0A\00"
define i32 @main() nounwind{
%x = alloca double
store double 2.8, double* %x
%1 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), double* %x)
%2 = load double, double* %x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), double %2)
ret i32 0 }

```
## Arithmetic on int 
In this case dividing will loose int real part. 
```drapcode
x = 4 + 2 - 3
shout x
y = 6 / 2
shout y
z = 5 / 2
shout z
a = 3 + 2 - 4 / 2
shout a
b = (2 + 2) * 2
shout b

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%d\0A\00"
@str.2 = constant [4 x i8] c"%d\0A\00"
@str.3 = constant [4 x i8] c"%d\0A\00"
@str.4 = constant [4 x i8] c"%d\0A\00"
@str.5 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%1 = sub i32 2, 3
%2 = add i32 4, %1
%x = alloca i32
store i32 %2, i32* %x
%3 = load i32, i32* %x
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), i32 %3)
%5 = sdiv i32 6, 2
%y = alloca i32
store i32 %5, i32* %y
%6 = load i32, i32* %y
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), i32 %6)
%8 = sdiv i32 5, 2
%z = alloca i32
store i32 %8, i32* %z
%9 = load i32, i32* %z
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.3, i32 0, i32 0), i32 %9)
%11 = sdiv i32 4, 2
%12 = sub i32 2, %11
%13 = add i32 3, %12
%a = alloca i32
store i32 %13, i32* %a
%14 = load i32, i32* %a
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.4, i32 0, i32 0), i32 %14)
%16 = add i32 2, 2
%17 = mul i32 %16, 2
%b = alloca i32
store i32 %17, i32* %b
%18 = load i32, i32* %b
%19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.5, i32 0, i32 0), i32 %18)
ret i32 0 }
```

## Arithmetic on double
In this case all calculation will still its precision.
```drapcode
x = 4.0 + 2.5
shout x
y = 5.0 / 2.0
shout y

```

will transform to:
```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%f\0A\00"
@str.2 = constant [4 x i8] c"%f\0A\00"
define i32 @main() nounwind{
%1 = fadd double 4.0, 2.5
%x = alloca double
store double %1, double* %x
%2 = load double, double* %x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), double %2)
%4 = fdiv double 5.0, 2.0
%y = alloca double
store double %4, double* %y
%5 = load double, double* %y
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), double %5)
ret i32 0 }
```

## Arithmetic for mixin int and double
In that case int value will be converted into double.

```drapcode
x = 5.0 / 2
shout x
y = 2.0 + 5
shout x
a = 1 * 5.0
shout a
b = 5 - 2.1 + 2
shout b

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%f\0A\00"
@str.2 = constant [4 x i8] c"%f\0A\00"
@str.3 = constant [4 x i8] c"%f\0A\00"
@str.4 = constant [4 x i8] c"%f\0A\00"
define i32 @main() nounwind{
%1 = fdiv double 5.0, 2.0
%x = alloca double
store double %1, double* %x
%2 = load double, double* %x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), double %2)
%4 = fadd double 2.0, 5.0
%y = alloca double
store double %4, double* %y
%5 = load double, double* %x
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), double %5)
%7 = fmul double 1.0, 5.0
%a = alloca double
store double %7, double* %a
%8 = load double, double* %a
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.3, i32 0, i32 0), double %8)
%10 = fsub double 5.0, 2.1
%11 = fadd double %10, 2.0
%b = alloca double
store double %11, double* %b
%12 = load double, double* %b
%13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.4, i32 0, i32 0), double %12)
ret i32 0 }
```

## Arithmetic of variable and int value
```drapcode
x = 6
y = x + 4
shout y

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 6, i32* %x
%1 = add i32 6, 4
%y = alloca i32
store i32 %1, i32* %y
%2 = load i32, i32* %y
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), i32 %2)
ret i32 0 }
```

### If statement
Simple example. See that there are present scopes.
```drapcode
x = 5
if x == 5:
    x = 10
    shout x
endif
shout x

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%d\0A\00"
@str.2 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 5, i32* %x
%1 = icmp eq i32 5, 5
br i1 %1, label %true1, label %false1
true1:
store i32 0, i32* %x
store i32 10, i32* %x
%2 = load i32, i32* %x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), i32 %2)
br label %false1
false1:
store i32 5, i32* %x
%4 = load i32, i32* %x
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), i32 %4)
ret i32 0 }

```

Output:
```output
10
5
```

### If statement with user interaction
```drapcode
x = 1
gimmme x
if x == 5:
    x = 10
    shout x
endif

```


will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [3 x i8] c"%d\00"
@str.2 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 1, i32* %x
%1 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str.1, i32 0, i32 0), i32* %x)
%2 = icmp eq i32 %x, 5
br i1 %2, label %true1, label %false1
true1:
store i32 10, i32* %x
%3 = load i32, i32* %x
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), i32 %3)
br label %false1
false1:
ret i32 0 }

```

Output when inputed *1*:
```output
 <no output>
```

Output when inputed *5*:
```output
 10
```

### While loop
This loop will iterate only once
```drapcode
a = 99
x = 1
while x == 1:
    y = x - 1
    x = y
    shout a
endwhile

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%a = alloca i32
store i32 99, i32* %a
%x = alloca i32
store i32 1, i32* %x
%1 = icmp eq i32 1, 1
br label %while1
while1:
br i1 %1, label %true1, label %false1
true1:
%2 = sub i32 1, 1
%y = alloca i32
store i32 %2, i32* %y
store i32 0, i32* %x
store i32 %2, i32* %x
%3 = load i32, i32* %a
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), i32 %3)
br label %while1
false1:
store i32 1, i32* %x
ret i32 0 }
```

Output:

```output
99
```

### Functions

```drapcode
func tmp:
    b = 2
    shout b
endfunc

x = 1
shout x
tmp()

```

will transform to:

```llvm
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@str.1 = constant [4 x i8] c"%d\0A\00"
define i32 @tmp() nounwind {
%b = alloca i32
store i32 2, i32* %b
%1 = load i32, i32* %b
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.1, i32 0, i32 0), i32 %1)
ret i32 %2
}
@str.2 = constant [4 x i8] c"%d\0A\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 1, i32* %x
%1 = load i32, i32* %x
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str.2, i32 0, i32 0), i32 %1)
ret i32 0 }
```

otuput:

```output
1
2
```