Title: Quantum Computing
Description: Is this an evolution?
Date: 2019-12-19 10:42
category: Technology
tags: quantum, computer, technology
image: quantum-computing.jpg
icon: fas fa-atom


## A short history of quantum computers
Quantum computing is a -relatively- new buzz-word. If you have followed news, it seems like we reached "Quantum supremacy", but is it true? Are quantum computers here to take over? Should we all expect a new paradigm shift? Is this the next industrial revolution?

Well, yes and no. Quantum computers are different kind of species, they're *not* to take over the classical computers much like quantum physics which completed the classical physics and never disproved it.
There are just some flaws is classical computers (much like classical physics) that we hope quantum computers would fill in.

Let's discuss this in more details here.


### About classical computing
A long time ago, there were people called "computers". It was an actual job title! The person was is charge of doing calculation.

Then came electrical computers, somewhere in 1940s in hope to do precise calculations, faster than human being. And as we can see, that was a success.

This new electrical computers were designed out of Math and (classical) Physics, by people who we were used to call "computers"! (from now on, let's call these people "mathematicians" and the machines "computers")

Over the years, computers became smaller and faster, now your smartwatch is much faster than the computer that put man on the moon. But rules of physics are cruel. Somewhere in computers' history, we reached the point where adding processor power required more electrical power than we could provide.

Here came multi-core processors. But don't get too excited, even that stopped somewhere around a decade ago. It was a big hope, it helped a lot. But still, a dead-end. No significant improvement since early 2010s.


### Quantum computing to the rescue!
![Schrodinger's cat](/theme/images/articles/quantum-computing/schrodinger.png)
(Schrodinger's cat is both dead and alive. Image from [wikipedia](https://commons.wikimedia.org/wiki/File:Schrodingers_cat.svg))

Unlike classical computers, quantum computers don't rely on "binary" phases. They still have *bits* but a different kind of them, called "qubit" (short for QUantum BIT).
As the basic unit of information, qubits can be either 0 or 1 or **both** (the superposition)! That's where all the magic comes from.

Qubits can store 2^n states, exactly same as good old bits, but:

> When you have an array of 8 bits in your computer, it can store from 0 to 256 but can only have **one correct state at any given time**.

> 8 qubits in a quantum computers can also store 0 to 256 (no more than that), but they can have **all possible states simultaneously**.

It's a common mistake that some people think "It can have 3 states, so its 3^n states." but that's not true. There is no "3 states", it's just 2 states but before we see it, it's both of them. Three-state logic is totally different and has nothing to do with quantum mechanic.

After you create qubits and right before you detect them, they are in some special state called "superposition". Just like Schrodinger's cat, it can be both 0 (dead cat) and 1 (alive cat) at the same time, but when we detect it and see its properties (open the cat's box) it takes one of these forms and become just like a normal binary bit.
You can think of it as a coin that you flip. While it's in the air (spinning around itself) it is both *heads* and *tails*, when you capture and look at it, it definitely has one of those states.

Rules of classical physics and quantum physics are totally different. We can't combine them or use one to describe the other. Both Schrodinger's cat and the coin, are hypothetical examples to help our brain -which is used to classical physics- to grasp the rules of quantum world.

Sounds great, right? Keep on reading...


### How does it actually works?
Entangling these qubits (in their superposition) with other objects helps quantum computers solve some real-world problem. But relationship between qubits and the outside world is too technical and I'm not an expert, so let's talk about the interesting parts of the magic.

> "Science is magic that works." ― Kurt Vonnegut, Cat's Cradle

A qubit in superposition, can be 1 and maybe 0, or less 1 with a little more 0 or vice versa. Now Imagine we have more of these qubits in relationship with each other. We know they are in all possible states right now, when we measure them, they collapse into their best-fit position (each one of them will be definite 0 or 1, just like classic bits). So when we read them, **they are the solution to our problem**.

In classical computing world, we have to try every possible state of the system to guess the answer, but in quantum world, since qubits can be at *all possible states simultaneously*, we get the answer in seconds instead of years! (for big difficult problems)

Sounds great; It's a dream that actually works! But don't put your hopes too high.


### Why does quantum computing grow so slowly?
![IBM Q 2018](/theme/images/articles/quantum-computing/ibm-q.jpg)
(Guts of IBM Q, a quantum computer. Image from [flickr](https://www.flickr.com/photos/feuilllu/46700983592))

10 years ago, I was on my way home from programming class, one of my friends said:

> Hay! Did you know that scientists are designing new form of computers? They're called "Quantum computer". They said that it'll be super small and super fast. When those computers reach the market everything we're learning right, will be obsolete.

Well, first drafts about quantum computation were released in 1980s, and still we're trying to make it real. Sounds like something's wrong. Everything seems just fine, we have qubits with their strange superposition, very few of them can perform almost impossible tasks. But what's taking them so long to build a working, industrial-ready, revolutionary quantum laptop or maybe even smartphone?

While superposition is super cool, creating qubits is difficult and managing them is super hard.

Ever heard of circuit noise? Guess what! Quantum computers experience noise too! In more sensitive and annoying way.

Small change in environment's temperature (thermal vibration) is a big noise. So we need to keep our system is the most stable environment we can design.

Also did you notice, our subatomic particles are made out of an atom? And everything including our computer's parts are made out of atoms. So we need to keep our qubits isolated from external world including our device, while keeping it safe and secure there so we can measure and observe its state. Anything can make the whole system unstable.

We have some options for that, but they're expensive and not 100% effective (what is?) like trapping our qubits in strong electromagnetic fields so they can't escape and keep them in ultra-cold and in a super-vacuum environment, isolated from outside world and even from other parts of the computer.

See? It's not as easy when it comes to practice. That's what took them so long to perfect their design.

### Data transmission, faster than the speed of light
![Observing superpositions](/theme/images/articles/quantum-computing/superposition.jpg)
(Observing particles' superposition. Image from [needpix](https://www.needpix.com/photo/download/1766307/physics-quantum-mechanics-quantum-physics-theory-eye-perception-overlay-atomic-atom))

Let's say we create two entangled qubits (quantum entanglement), keep both of them in superposition and send one to the other side of the world or even another planet. If we detect (read) one of them, both particles' superposition would collapse and they'll get a normal bit-wise state.

Seems like two entangled qubits share some information about their state, in **real-time**. Before a beam of light could even start its way from one's location to the other.

That's really strange and disproves Einstein's theory of relativity (that nothing could travel faster than light). We can't put that into practice yes, but it seems true.

Guess who made this theory and disproved relativity! Einstein himself! He got very mad about it and tried to prove his second theory wrong!

So in theory, we can achieve not only *faster than light*, but **really instant data transfer**. It's not an advertisement, so when I say "real-time" I don't mean 5ms delay.

Using today's computers we have like 200ms delay across the globe, but with quantum computers, that's down to zero in universal scale. But as always, there's a downside to that. Keeping subatomic particles in superposition is super difficult, transferring them to another location (even another room) is almost impossible with today's technology.

Are you thinking of 0ms ping from here to your friend on Ursa Minor? Well, think of ways to send them there, because we already know how to write a quantum messaging app :)

Big (but theoretically achievable) goal for quantum computers.


### How far did we get?
![EAI 580 analog computer plugboard at CHM](/theme/images/articles/quantum-computing/EAI-580.jpg)
(EAI 580 analog computer plugboard at CHM. Image from [wikimedia](https://commons.wikimedia.org/wiki/File:EAI_580_analog_computer_plugboard_at_CHM.jpg))

Well there are lots of things in quantum mechanics that we can't explain and we're building these computers on some theories, guesswork and lucky practices.

But:

* We did manage to build them, they're super expensive and big, much like computers of 1950s.
* We even ran some small, specific programs that were just made for these devices.

So they are still at early stages. Like early military computers. Big, power hungry, expensive, and faulty. Something that only a big organization could operate.

And exactly like vacuum tube computers, at any time we expect a new revolutionary invention like transistor to show up and boost everything.

But for now, we can't build any multi-purpose quantum computer. Just some laboratory experiments and a couple of single-purpose programs. Exactly like plug-board computers which required you to manually rearrange cables every time you want to run a single and simple program on it.


### Quantum supremacy. Are we there yet?
![xkcd Random Number](/theme/images/articles/quantum-computing/random.png)
(Random number generator function. Image from [xkcd](https://www.xkcd.com/221/))

First quantum mechanical model of Turing machine was published in 1980s. Probably some years after that, governments and organizations start investing on building them and trying to solve real-world problem. Their ultimate goal is to solve problems faster than a classical computer.

That's called quantum supremacy. When a quantum computer can perform a task, faster than classical computers and also when we can run multiple programs on it, not just one, hard-coded algorithm.

Couple of months ago, google announced that they used 53 qubits to build a "true random number generator" and prediction algorithm.

Classical computers are good for precise tasks, like calculating 5+12. But for some applications like cryptography, we need random numbers. But generating random numbers are difficult task and making sure it *is* random is almost impossible.

Google engineers claim that they used 53 qubits to do the job in 200 seconds. A job that would take a supercomputer about 10,000 years to accomplish.

Well, they did the job. They finally did something with quantum computers that was almost impossible for a classical supercomputer (even a server farm).

But that's not really as useful as they claim. You can buy a random number generator USB device for $50.

If you're on Unix, you can rely on `/dev/random`. You can even write your own random number generator in your favorite language and read user's mouse move, thermal information of motherboard and some other sources, add Unix timestamp to this chaos and then apply a hash algorithm on it (don't do that. there are cryptography libraries for that, much better than what you and I can write). 

We already have free random number generators! Good enough that our life already depends on it.

I think it's safe to say that they just wasted $100M. It's kind of a supremacy, but a very useless one.

The only good news is we are laying foundation for future projects. We might be in the right track, but maybe we need to change our perspective towards the use-case of quantum mechanics. Maybe we need to redesign the whole thing. Maybe (and i hope I'm wrong) we need to shut it down and stop wasting resources.


### Where does it belong?
![DNA strand construction](/theme/images/articles/quantum-computing/dna.jpg)
(DNA strand construction. Image from [pixfuel](https://www.pxfuel.com/en/free-photo-jqksj))

Quantum computers are different kind of computers. They are good at different kind of tasks. I certainly hope we reach the moment when they can do a real job. Some industries really need this way of revolution.

Take for example *artificial neural networks*. Right now, we build a software, we input our data and our good old computer tries all possible patterns to find a path between our input and our expected output. That's where a quantum computer with its superpositioned qubits can help a lot. Qubits can take all possible patterns at the same time and give us the best match just when we detect them. That sounds like a job made for this weird quantum behavior.

Another example would be Pharmaceutical industries and Cryptography.


### Did you just said Crypto?
Quantum supremacy is kinda scary. If they can break cryptographic algorithms like RSA and SHA, no one would be safe from big brother. (Are we safe even now?)

But there are some good news too. Cryptographic algorithms based on quantum mechanic have been designed already (since 1970s and 1980s). They can provide security and privacy far better than anything we already have.

I don't want to talk about it right now. That's a lot of information to cover. Let's first build a usable quantum computer, then we'll talk about security. Just don't panic yet. Quantum cryptography and quantum crypto-currency are on their way to help us live a more secure and private life.


### Could all of us afford one?
I don't think so. I don't think quantum computers would be something you can have in your house. It's not even something you need on your day-to-day life. Most of our tasks can be safely handed to classical computers. Tasks that are simple for our present technology and really difficult for quantum computers.

You don't need ultimate probability to browse Instagram and watch a movie on Netflix.

Maybe you'll work on some industries where you need to work with them. Maybe some day they find a way to build super-cheap, super-awesome quantum computers, but I don't think it'll ever gonna be useful enough for everyone.


### Be prepared for quantum powered world
![Hype cycle of quantum computing](/theme/images/articles/quantum-computing/hype-cycle.png)
(Hype cycle chart. Quantum computers are somewhere near that red dot. Image (without the dot) from [wikipedia](https://en.wikipedia.org/wiki/File:Hype-Cycle-General.png))

I'm pretty sure when industrial-ready quantum computers come to our neighborhood, some great programmers already made a LISP compiler for it. We'll have macros for flipping quantum states 0:)

Also a Unix operating system would be pre-installed. Probably a GNU/Linux distro or maybe even GNU Hurd.

Why LISP and Unix? Because these are some of the most flexible pieces of software ever designed. When facing new opportunity, your best bet is to be flexible.

All we have to do, is to **Learn how to learn**. We are human, we're good at adopting to changes; That's what kept us away from extinction.

I think as "the most dominant species on the planet" we should all practice the art of adoption. It's not good enough to learn a new programming language, it's not good enough to learn how to cook a new dish. We sould learn how to learn.

Learn how to explore new systems, new rules. Experience new ways of something and analyze outcomes. Then you'll be ready for anything; Be it a quantum computer, alien invasion or zombie apocalypse.

That's how scientists lived their life since the beginning. Look what they brought us: Everything.


---
*Image from [Unsplash](https://unsplash.com/photos/UgNjyPkphtU).*
