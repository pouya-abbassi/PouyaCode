title: Bulma CSS Framework
description: When to use and when not
date: 2022-07-11 06:49:33
category: Programming
tags: design, ui/ux, appearance
icon: fab fa-sass
image: bulma-css-framework.jpg
image_info: Image by me, made with Blender.


Sometimes perfection isn't your #1 priority, you just want to get started and get things done; It's OK! Sometimes!

That's why I chose Bulma CSS Framework for my website. Bulma is great framework. In my opinion, far better than Bootstrap and Foundation. I will definitely use it again for future projects; If you never had a chance before, I suggest you give it a try. You'll love it even if (like me) you're not a front-end developer.

I can go on about how awesome Bulma is, but it's out of scope of this article and you really must see for yourself.

But like all general-purpose frameworks, there's a catch: Optimization!

Compiled version of my Bulma stylesheet was 208 KB. Not too much if you consider what's the norm in year 2022, but big enough to annoy a perfectionist. On top of that, there was 534 instances of `!important` in the stylesheet! That's way too much for my taste!


## Something has to be done

I cleared a week on my schedule to rewrite the stylesheet from scratch and to my surprise, it took less than two days and I learned a few corners of CSS3 that I never had a chance to take a peak. Yay me!

Resulting Sass file was compiled to 11 KB of CSS with zero `!important`s. Website looks exactly the same; Actually I decided to change the colors, but that doesn't have anything to do with Bulma.

Something else that I can't measure as easily, is Style Override. The "C" in CSS stands for Cascading. Right? When the style of an element (say, its color) can be set by its distant parent element, and then be overridden by its immediate parent and then it can have a style of its own which actually is the only thing that matters. And browser has to process all that mess just to discard the non-essential ones and only apply one that matters.

Nerd Alert. I know! But I'm a nerd. One that cares about perfection, even if no one notices the imperfection.


### Lines of Code

Before, I had to write 356 lines of sass, to override and customize Bulma to my needs. Now that I rewrote everything, the whole thing is just 632 LoC.

It's funny (and not entirely true) but almost as if I only used ~300 LoC from Bulma!

See what I mean when I say Frameworks are not always the answer? Even a pretty good one like Bulma, forces you to write some code to do what you want from it, that if you were willing to double that, you wouldn't need that framework in the first place!


### Conclusion

Of course, take my words with a grain of salt. It's not always like this. Sometimes it's nearly impossible to do something without standing on the shoulders of who came before. But keep that in mind that for every task, you can re-think and make specific decisions that suits your specific purpose.

| Property       | Before | After       |
|----------------|--------|-------------|
| CSS Size       | 208 KB | 11 KB       |
| !important     | 534    | 0           |
| Style Override | a lot  | almost none |
| Sass LOC       | 356    | 627         |
