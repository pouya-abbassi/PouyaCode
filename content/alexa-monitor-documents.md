title: Alexa Monitor Documents
description: You can't write a beginner-friendly project without documents
date: 2021-06-27 12:56:16
category: Programming
tags: clojure, beginner-friendly, knuth
icon: fas fa-spider
image: alexa-monitor-documents.jpg
image_info: Image by me, made with Blender. You can 3D model is available <a href="(https://mega.nz/folder/dcs2FR7K#3_N28U-vC7dLa9vF90kaxA" rel="nofollow" target="_blank">here</a>.

As usual, every project starts with a try-and-fail phase; In other words: little-to-no comment and rapid change in the code-base. But now, I have a solid ground to work on, so spent some time writing comments and found an amazing tool to build a [pretty nice api-doc](https://alexa-monitor.pouyacode.net).

I used a Leiningen plugin called [Marginalia](https://github.com/gdeer81/marginalia); Kudos fellas!

There are similar tools for many other languages; It's not a Clojure-specific thing.


## Writing documents
There's an old saying:
> If the code was hard to write, it should be hard to understand.

If you know the origin of this quote, please report them to the Galactic High Court; They should be sentenced to lifetime of code review and writing documents :)

In my humble opinion, [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming) as described by [Donald Knuth](/pages/jedi-order.html) *(May the Source be with him)* is overkill, but we need to make our codes as close to it as possible and write a good enough comment, to cover beginners and experts. Most programmers write comments for themselves (and their like-minded colleagues) and if you're new in their Tech Stack or industry, you'll be lost!

In this project I tried to explain my thoughts as much as possible; I try to explain things to "Pouya from 2018". And I think the most important part of every file should be the explanation of Data Flow: The main function of each namespace and the flow of data through that namespace.

At least in Clojure and Functional Programming!


### What's new?
I wrote an article in DevHeroes.club (in Persian) and introduced Alexa Monitor to my friends there. You can [check it out](https://devheroes.club/t/topic/5091?u=pouya-abbassi).

Today I also added this project to [BraveClojure's Open Source projects list](http://open-source.braveclojure.com/projects/alexa-monitor). I hope newcomers find it there and join the fun!


### URLs
The documents generated for alexa-monitor are available [here](https://alexa-monitor.pouyacode.net).

Previous article in this series: [Alexa Monitor]({filename}/alexa-monitor.md).
