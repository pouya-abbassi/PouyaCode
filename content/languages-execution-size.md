Title: Execution size of programming languages
Description: A comparison of different compilers' output
Date: 2021-07-18 20:01:55
category: Programming
tags: technology, computing
icon: far fa-save
status: draft


Usually when we compare Programming Languages, we tend to compare their speed and working environment, then we may put their community and library availability into account; But rarely compare different Languages or Compilers on their execution size, unless it's a matter of Kernel Development or Embedded Systems.

Here I would like to write some very simple projects in different Languages, and see what compiler generates smaller binary.


### System configuration
* OS: Debian Sid
* Architecture: x86_64
* GCC: 10.2.1
* C++: 10.2.1
* rustc: 1.53.0
* go: go1.15.9

Every programmer starts their carrier with the good old `hello world` program. So let's dig in.

### Good old C
```c
#include <stdio.h>

int main(int argc, char** argv) {
	printf("Hello, World!\n");
	return 0;
}
```

Compile options:
```bash
gcc hello.c --static -o hello
```
Binary size: `782768 bytes`

Just for fun, let's compile the same code with dynamic linking:
```bash
gcc hello.c -o hello
```
Binary size: `16608 bytes`


### Our dear C Plus Class
```c++
#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	cout << "Hello, World!" << endl;
	return 0;
}

```
Compile options:
```bash
g++ hello.cpp --static -o hello
```
Banary size: `2199656 bytes`

Once again, with dynamic linking:
```bash
g++ hello.cpp -o hello
```
Binary size: `17248 bytes`


### C++ using C's stdio
C++ can also use C libraries, so let's try using `printf` instead of `cout`:
```
#include <stdio.h>

int main(int argc, char** argv) {
	printf("Hello, World!\n");
	return 0;
}
```
Compile options:
```bash
g++ hello-stdio.cpp --static -o hello
```
Binary size: `782776 bytes`

Dynamic:
```bash
g++ hello-stdio.cpp -o hello
```
Binary size: `16616 bytes`

## Modern Rust
```rust
fn main() {
  println!("Hello, World!");
}
```
Compile options:
```bash
rustc -C target-feature=+crt-static main.rs
```
Binary size: `4775696 bytes`

Size optimization:
```bash
rustc -C opt-level=s -C target-feature=+crt-static hello.rs
```
Dynamic + size optimization:
```bash
rustc -C opt-level=s -C target-feature=-crt-static hello.rs
```
Binary size: `3258648 bytes`


## The language of GO
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```
Compile options:
```bash
go build hello.go
```
Binary size: `2034781 bytes`

Without [DWARF](https://tip.golang.org/pkg/cmd/internal/dwarf/):
```bash
go build -ldflags=-w hello.go
```
Binary size: `1535069 bytes`
