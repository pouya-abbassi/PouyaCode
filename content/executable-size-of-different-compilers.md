Title: Executable size of different compilers
Description: A comparison of different programming languages' output
Date: 2021-07-13 10:07:45
Modified: 2021-07-14 23:40:23
category: Programming
tags: technology, computing, languages, ritchie, mccarthy, russell
icon: far fa-save
image: executable-size-of-different-compilers.jpg


Usually when we compare Programming Languages, we tend to compare their speed and working environment, then we may put their community and library availability into account; But rarely compare different Languages or Compilers on their execution size, unless it's a matter of Kernel Development or Embedded Systems.

Here I'd like to write some very simple projects in different Languages, and see what compiler generates smaller binary. I try Static and Dynamic linking where possible, plus all the ways I know we can strip the executable output of the compilers.

Here we only examine compilers that produce *native code*, not the ones with *bytecode* output.

This article is not original. I saw the same written by Artem on dev.to website, but his post is somehow removed and it's now a 404 page and I couldn't contact him to ask for the fix. (You can still see his work on [Wayback Machine](https://web.archive.org/web/20210508020101/https://dev.to/aakatev/executable-size-rust-go-c-and-c-1bna))

I made this content because I think we need some reference for future articles on PouyaCode.net.


### System configuration
* OS: Debian Sid
* Architecture: x86_64
* gcc/g++: 10.2.1
* clang: 13.0.0
* glibc: 2.31-12
* rustc: 1.53.0
* go: go1.15.9
* sbcl: 2.1.1
* ccl: 1.12

My original plan was to write more complex programs, but that would introduce complexity and right now, all I need is a simple comparison for different languages and their compilers. I might add more projects for each language in the future.

All source codes, plus a `makefile` is available on [my github account](https://github.com/pouya-abbassi/executable-size).

Every programmer starts their carrier with the good old `hello world` program. So let's dig in.


### C - GCC
A de facto standard of kernel development, with simple design and zero unnecessary features. C must be winner here.

Its original goal was to help Unix developers "write once and compile everywhere", because our guy, [Dennis Ritchie](/pages/jedi-order.html) (May the Source be with him) was tired of the fact that each CPU has its own machine instruction set and they had to rewrite Unix for all targeted CPUs.

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
Binary size: `782768 Bytes`

Just for fun, let's compile the same code with dynamic linking:
```bash
gcc hello.c -o hello
```
Binary size: `16608 Bytes`


### Clang
As a drop-in replacement for GCC, and a totally different compiling cycle, I think LLVM's Clang should be included in our tests. Spoiler alert: the outcome is very close to our test with GCC!

Compile options:
```bash
clang hello.c --static -o hello
```
Binary size: `786936 Bytes`

Let's do it dynamically this time:
```bash
clang hello.c -o hello
```
Binary size: `16496 Bytes`

It is worth mentioning Alibaba Tech's [In-Depth Comparison of C/C++ Compilers](https://alibabatech.medium.com/gcc-vs-clang-llvm-an-in-depth-comparison-of-c-c-compilers-899ede2be378) regarding performance of these two compiles. Another spoiler alert: it's a close competition!

### C++
AFAIK, they used to call it "C plus class" before the change the name to C++, but we're gonna keep it simple and more C-like.

C++ was designed to be a "better C", so let us first try its native library: `iostream`
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
Binary size: `2199656 Bytes`

Once again, with dynamic linking:
```bash
g++ hello.cpp -o hello
```
Binary size: `17248 Bytes`

The executable output was way bigger than I expected!

But C++ can also use C libraries, so let's try using `printf` instead of `cout`:
```
#include <cstdio>

int main(int argc, char** argv) {
	printf("Hello, World!\n");
	return 0;
}
```
Compile options:
```bash
g++ hello-stdio.cpp --static -o hello
```
Binary size: `782776 Bytes`

Dynamic:
```bash
g++ hello-stdio.cpp -o hello
```
Binary size: `16616 Bytes`

The reason behind this huge difference in output size, is that `iostream` contains a lot of type conversion, exception handling, localization and probably other stuff under the hood. Also it's a bit slower than `cstdio` because of the exact same reasons.

So for performance critical I/O, or writing a library that needs to be accessed withing C, C++ programmers may use `cstdio` instead of native `iostream`; Otherwise I can't think of any reason why anyone should use `cstdio` in their C++ code.


### Clang++
GCC and Clang had a real competition there, let's see if Clang++ can match the mighty G++ compiler.

Compile options:
```bash
clang++ hello.cpp --static -o hello
```
Binary size: `2236584 Bytes`

Now dynamic:
```bash
clang++ hello.cpp -o hello
```
Binary size: `17072 Bytes`

And using `cstdio`:
```bash
clang++ hello-stdio.cpp --static -o hello
```
Binary size: `786944 Bytes`

Dynamic use of `cstdio`:
```bash
clang++ hello-stdio.cpp -o hello
```
Binary size: `16504 Bytes`

Again the difference is microscopic between G++ and Clang++.

## Rust
A modern programming language, developed by Mozilla with low-level control over performance and guarantee for safety; It certainly looks an attractive replacement for C.
```rust
fn main() {
  println!("Hello, World!");
}
```
Compile options:
```bash
rustc -C target-feature=+crt-static main.rs
```
Binary size: `4775696 Bytes`

Dynamic linking:
```bash
rustc -C target-feature=-crt-static hello.rs
```
Binary size: `3259488 Bytes`

Rust also supports some size optimizations!

Size optimization:
```bash
rustc -C opt-level=s -C target-feature=+crt-static hello.rs
```
Binary size: `4774864 Bytes`

Also we can ask `rustc` to make it more dynamic than default. So dynamic + size optimization:
```bash
rustc -C opt-level=s -C prefer-dynamic -C target-feature=-crt-static hello.rs
```
Binary size: `17272 Bytes`


## GO
Google's Go Lang was not initially designed with performance in mind, but mostly just to get things done. But as a fast and powerful compiled programming language, I think it deserves to be here.

Although there's no way (that I know of) to link it dynamically.
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
Binary size: `2034781 Bytes`

Without [DWARF](https://tip.golang.org/pkg/cmd/internal/dwarf/) and striped:
```bash
go build -ldflags "-s -w" hello.go
```
Binary size: `1535069 Bytes`


## Common Lisp
Designed as just a theory, not practice; It was never intended to solve any problem. "this eval is intended for reading, not for computing." was what [John McCarthy](/pages/jedi-order.html) told [Steve Russell](/pages/jedi-order.html) (May the Source be with both of them).

Maybe if computers were designed based on [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus) rather than Turing Machine, Common Lisp would be their de facto standard programming language everywhere and we'd be living in a world with far more advanced technologies.

But right now, it gives us the worst result for this particular "executable size" test. It's partially SBCL's fault, but we'll discuss this on later articles, in more depth.

Although the resulting binary is already huge, I don't know how to compile it with static linking.
```clojure
(defun main ()
  (format t "Hello, World!~%"))
```
Compile using SBCL:
```bash
sbcl --load hello.lisp --eval "(sb-ext:save-lisp-and-die \"hello\" :toplevel #'main :executable t)"
```
Binary size: `38739616 Bytes`

Compile using CCL:
```bash
ccl --load hello.lisp --eval "(save-application \"hello\" :toplevel-function #'main :prepend-kernel t)"
```
Binary size: `27214064 Bytes`


## Conclusion
| Language                       | Static (Bytes) | Dynamic (Bytes) |
|--------------------------------|----------------|-----------------|
| C                              | 782768         | 16608           |
| Clang                          | 786936         | 16496           |
| C++                            | 2199656        | 17248           |
| C++ (with stdio)               | 782776         | 16616           |
| Clang++                        | 2236584        | 17072           |
| clang++ (with stdio)           | 786944         | 16504           |
| Rust                           | 4775696        | 3259488         |
| Rust (size optimization)       | 4774864        | 17272           |
| Go                             | 2034781        |                 |
| Go (without DWARF and striped) | 1396736        |                 |
| Common LISP, SBCL              |                | 38739616        |
| Common Lisp, CCL               |                | 27214064        |

As I expected, C yields the smallest binary size, mostly because the compiler trusts us, programmers, to handle run-time check and memory management and tries to stay out of our way and just translates our code (almost) straight to assembly. And it's not just about GCC, even with Clang we get roughly the same result!

It's not just the compiler, it's the philosophy!

C++ on the other hand, if used with its native libraries, adds some run-time tests and other features to our program, so it produces a bit bulkier executable output.

It's worth mentioning that both Clang and Clang++ yield smaller binary output when *dynamically linked*. With my current knowledge of underlying structure of GCC and LLVM, it's a bit puzzling for me.

Rust is the heaviest of them all, even if you link the libraries dynamically. That's probably because of its "Lifetime feature" which is packed in our programs. It's very handy and interesting feature of Rust programming language. (At least on paper. In my experiment, it gets in the way and is a bit annoying)

Go isn't a system programming language and they probably pack too much run-time stuff that makes the output a bit bulky. And I don't expect to get small binary output since Go's goal is not system programming.

Same thing for SBCL and CCL, which are not built for low level system programming, and they pack too much power under the hood to fit in a minivan. Stay tuned, we'll discuss Common Lisp in more detail in the future, but to tame your curiosity: SBCL and CCL dumps everything you have in your development machine, inside your executable binary, including but not limited to the compiler itself!

Again. Let me rephrase that:
>It's not just the compiler. it's the philosophy, packed inside our program!


---
*Image by myself, using Blender
