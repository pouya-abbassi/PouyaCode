title: Will Rust replace C?
description: I sure as hell hope not!
date: 2021-09-23 23:14:46
category: Programming
tags: technology, computing, languages, ritchie, thompson
icon: fas fa-laptop-code
image: will-rust-replace-c.jpg
image_info: Image by me, made with Blender.


We recently had a long discussion on [Dev Heroes Club](https://devheroes.club/t/rust-c/5152/) about whether Rust will replace C in kernel development, considering its speed and efficiency and how fast it's growing.

Like any other nerd, I like to try new things first-hand, so I already had some experience with Rust, while C was my second programming language (after C++), so I joined in!

Rust is a cool new programming language with excellent execution-time and a promise for memory safety. The ownership principle is really attractive!

But like anything else, there's a catch! We'll get to it later.


### Let's talk Assembly before we dig into C
Assembly is exactly Machine Code, it's just more human readable than Zeros and Ones. And Assembler just turns our code directly into binary (with a few exceptions). My point is that Assembly isn't actually a programming language. It's just a human-readable representation of our CPU's Machine Code.

The main problem with coding in Assembly, besides the fact that we need to manually fidget with our registers and RAM, is that every CPU has its own set of instructions. So we need to learn them before even thinking of porting our program to that architecture. That's a real bummer!


## Reasons behind C's Awesomeness
C was *invented* by Dennis Ritchie for two main reasons:

* He is awesome!
* He had a bit of a problem developing UNIX kernel.

Back then in the 1970s, if you wanted to build a kernel, you had to write machine code, or learn the language that has compiler for this specific CPU architecture; So you had to learn your CPU's specific language or its Assembly (if there was no other option for low-level programming for that architecture). If you wanted your kernel on another type of CPU, you had to rewrite everything (or at-least most of it)

If course there were a few High-Level programming languages (anything higher that Assembly, is High-Level) as well, but their compilers couldn't generate multiple Machine Codes, and they weren't optimized for low-level operations. Or perhaps they didn't measure up to Dennis' standards!

So Dennis tried to address these issues and with [Ken Thompson](/pages/jedi-order.html)'s help (May the Source be with him) designed a language and compiler capable of generating multiple machine codes from a language specially designed for High and Low-level operations that does *exactly* what you say. A language with a small core and just enough functionalities to lay the groundwork for anything you want to implement; Even if you want to print something on screen, you need to import a library.

I know it's not 100% true, but I like to think that C is just like Assembly, in the sense that it doesn't add anything to our code if we don't say so. It trusts us to do the right thing when it comes to Memory Management or any other low-level operations.

That comes with an advantage and a price!

On the plus side, as I said earlier, compiler does exactly what you ask and doesn't add anything to the resulting executable file; check out my previous article about [Executable Size of Different Compilers](/executable-size-of-different-compilers.html).

On the other hand, we (programmers) are responsible to optimize our code & free allocated memory when it's not needed. So our carefully designed software is prone to bugs as it grows in size or team or just because time has passed, and we forgot some tiny details about some functions' workflow!

Such things probably was part of the reason why some programmers and computer scientists felt the need to create new programming languages.


## Here comes the Almighty Rust
A language designed by Mozilla, Rust is made with near-c performance and a promise for Memory Safety; And actually it held its promise by introducing the Ownership principle.

I'm not sure if it's an old theory or something that Rust's developers came up with, but it's just awesome! (at least in theory. It totally depends on your use-case)

Ownership in a nutshell is assigning one function and _only_ one function as the owner of each variable. In other words, when you create a variable, the function which surrounds this variable becomes its owner. So when the execution of this function ends, Rust removes the variable from memory without much thinking.

That's an amazing approach to Memory Management because compared to other methods that I know of, it takes very few CPU & RAM cycles to manage memory on run-time, and virtually no decision should CPU make in order to determine whether we will need this Var; All decisions are made in Compile-Time and your Rust compiler just adds some machine code to the end of each function to free all the memory used inside that function.

Sounds cool! The only exception would be when a function wants to return something. In that case, the other function would become the owner of this Var and therefore responsible for managing its memory.

Bottom line: Rust makes some automatic decisions in compile-time and _adds_ some functionalities to our code. (I don't want to get into details of why this sucks in practice and ramble on about irritating Lifetime Notations, that's not the main concern of this article)

That's true for other languages as well. Not necessarily about memory management, but every time a programming language decides to make our life easier. It writes some codes on our behalf, to automate some otherwise dull and repetitive tasks. Something that would be boring for us, or we might overlook.

It's useful and common practice if you like (need) to enjoy some levels of abstraction and not deal with hardware's stupidity.

Correct me if I'm wrong, but isn't that exactly what we should do when we build a kernel (or modules for it)?

By handing over the control of low-level decisions to the compiler, we make our life easier, but the price is to lose control over optimization!

Language designers and compiler programmers are genius people, you can't really appreciate their work unless you build a compiler yourself! But the compiler itself can't really understand our code and our workflow. When we let compiler make some decisions, we are telling it to "run some automatic tasks whenever you see this specific pattern".

We can't ask a compiler to see the big picture, because it just can't!


## It all comes to use-case
C, definitely passed the test of time; but Rust is here to stay too!

IMHO, Rust is at the peak of its Inflated Expectations stage (Hype Chart metaphor). Developers and companies are investing on this attractive asset, and after a while, like any trend in programming world, people will realize it's not a one-size-fit-all and I think it'll lose its fans after a while, 'till eventually Rust becomes yet another tool in our toolbox; A perfect tool for certain tasks, not every task.

Rust or any other programming language will never replace C. Mostly because of its special design, it's practically irreplaceable, at least as long as our computers are designed based on Turing Machine.

C trusts programmers to be smart enough to do the right thing and doesn't make any decision on our behalf; Not in run-time and not even in compile-time (except to run some optimizations). If you take a look at the table in [Executable size of Different Compilers](/executable-size-of-different-compilers.html) article, you'll see what I mean. Every other language (even C++ which is a close competitor and also a direct descendant of C) adds some extra functionalities to our code, which might not be what we want/need for certain tasks.


## But isn't it time for more abstraction?
There's no doubt that Programmers and Tech Companies of today are lazier that the ones in the 1900s. We simply don't care much about CPU cycles and RAM usage of our programs since we're not limited to few kHz CPU and few kBytes of RAM anymore; Even user doesn't care if their favorite music player runs on 2 MB or 200 MB RAM!

Instead of weighing bits and bytes, "we want this feature yesterday" or else we lose the market to our competitors! So we chose higher-level programming languages and through in a bunch of libraries, then Docker the thing up and upload it to our favorite PaaS.

But in Kernel Space it's a different story. Every byte matters, every CPU cycle, every RAM access and even every single bit in our registers is precious.

I don't know any other programming language, capable of producing a simpler assembly than C. For example in Rust, even if we know a better way of optimizing our code, there's no way (that I know of) we can do that. At least I couldn't figure out Rust's assembly output, it's just gigantic!

To give you a better idea of why we shouldn't trust compiler to optimize our code, please check out one of the most useful articles I've ever read: [The compiler will optimize that way](https://blog.royalsloth.eu/posts/the-compiler-will-optimize-that-away/)
