Title: Alexa Monitor
Description: A beginner friendly Clojure app
Date: 2021-06-17 18:55:14
Modified: 2021-06-27 10:05:34
category: Programming
tags: clojure, beginner-friendly
icon: fas fa-spider
image: alexa-monitor.jpg


I was experimenting with some Clojure libraries and decided to write a simple web crawler, one thing led to another and now, I think it would be a good opportunity to make it public and help new Clojure programmers take their first steps by contributing to it.

It's not gonna be anything special or groundbreaking. My goal is to build a tiny community and help new people; Teaching what I know and learning what they have to offer.

Newcomers from all backgrounds are welcome; Of course some knowledge of Clojure or any other LISP and Functional Programming is a required to understand the code, but feel free to ask any question, even if you think it's a simple one.


## About the project
Alexa doesn't provide public API, so we'll lazily crawl Alexa`s [Mini Siteinfo](https://www.alexa.com/minisiteinfo/pouyacode.net) page and collect information regarding the given domain. Contents are updated every 24h so we don't need to revisit the page very often.

It's publicly accessible and used inside Alexa's browser extension. So I don't think they mind if we send a `GET` request couple of times a day!

The result would be collected and stored in a SQLite database. In the future, we might add some ways to export the collected data and create some reports.

I would probably write more about this project, and maybe a few Clojure Tutorials to cover some problems we solve along the way.


### How to contribute
Whenever I find something that's not too difficult to fix (or implement) I'll create an issue with `good first issue` tag and explain the challenge.

Also I'll try to keep everything well written and well documented, so it'd be easy to read and understand. But if something wasn't clear enough, you can just ask me (or someone else in the community) to explain it in more detail and probably refactor the code to make it more readable for humans.

> Programs must be written for people to read, and only incidentally for machines to execute.
> — Harold Abelson; Structure and Interpretation of Computer Programs

We write code for people, computers can catch up!

The goal is to learn and to teach, so well documented contributions are most welcome.

Before writing a new feature or fixing any issue, please first discuss with others.


### URLs
The project is hosted on [GitHub](https://github.com/pouyacode/alexa-monitor).

Documents available [here](https://alexa-monitor.pouyacode.net).

Discussions take place at [Gitter](https://gitter.im/pouyacode/alexa-monitor).

Next article in this series: [Alexa Monitor Documents]({filename}/alexa-monitor-documents.md).

---

*Image by myself, using Blender; You can also [download the 3D model](https://mega.nz/folder/dcs2FR7K#3_N28U-vC7dLa9vF90kaxA).*
