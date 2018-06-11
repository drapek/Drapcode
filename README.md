# Drapcode
Own compiler of Drapcode language. 

## Description
This is compiler implementation of own language called Drapcode. To get used to it I recommend to look into _examples_ folder

# Errors
* there can't be blank lines between statements

# Features
[/] IO operations
[x] int and real numbers
[x] strings
[x] math operations
[x] if statements
[x] while loop
[x] functions with scope variable
[x] arrays

# How to use
```bash
python main.py <drapcode_file> out.ll
clang-6.0 -o <output_filename> out.ll
```

## Requirements
* Python >= 3.6 (f-strings are used)
* packages from requirements.txt (pip install -r requirements.txt)
* llvm >= 6.0

## Example usage
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
