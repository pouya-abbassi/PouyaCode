Title: Signing WebPages
Description: Signing HTML documents using PGP.
Date: 2021-01-09 21:20
Modified: 2021-01-12 01:55
category: Security
tags: computing, technology, encryption, pgp, sameer
image: signing-webpages.jpg
icon: fas fa-shield-alt


A while ago, I shared [my PGP key](/pages/pgp.html) with you, "for more secure connections in future"; And I'm glad to announce that all `HTML` pages of this website are now signed by my PGP key.

Of course web-browsers are not built for this, I don't know any web-browser that can verify the signature of a web page; Even if you write a plugin, it should re-download the page for verification, because JavaScript doesn't have access to the whole document, it can only read what's inside `<html>` tag (`document.getElementsByTagName`). But you can always verify the signature manually in commandline:

```bash
curl https://pouyacode.net/webpage-signature.html | gpg -v
```

Anyway, I used a simple trick to make this happen; To sign pages the way that it's readable for web-browsers and also GnuPG (and other PGP clients).

So let's dig in.

## Here's how to sign webpages using PGP
I assume you're using GnuPG, because why not? (Everything should work fine in any PGP implementation)

Of course, we need to `--clearsign` the  page; so that browsers can read the content. PGP clients, tends to look for a line like:

```text
-----BEGIN PGP SIGNED MESSAGE-----
```

And ignore what came before. While web-browsers tend to ignore whatever you put inside `<!--` and `-->`.

Sounds like an easy puzzle! We can put these simple rules together in a way that both applications can access the content they want, without interruption.

It's actually pretty simple, you can do it using a text-editor. As I said earlier, we're using `--clearsign` option, so that the textual context is intact and readable to browsers, while there's signature *inside* the same file for our PGP client to read.

The `--clearsign` option, creates a bit of text, at the beginning and the end of our original content. We need to put those parts inside a `HTML` comment so web-browsers don't see/process it. But any kind of modification in the signed file, would revoke the signature; So we can't comment this part after creating the signature. We need to add the required parts (parts that would end-up inside the signature) before actually signing the page.

It's easier to understand if I show you how:

* Prepend `-->` to the file, so that what comes before, will be comment. PGP will prepend something just before this line. (Optionally put a space before this line so the result to looks a bit nicer.)
* Append `<!--` to the file, so that whatever comes next, will be comment. PGP will append the actual signature after this.

Now your page looks like this:
```html
 -->
<!DOCTYPE html>
<head>
...
</head>
<body>
...
</body>
</html>
<!--
```
* Run `gpg --clearsign <filename>.html`. The result would be a file called `<filename>.html.asc`. Which is our signed web page and looks like this:
```html
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

 -->
<!DOCTYPE html>
<head>
...
</head>
<body>
...
</body>
</html>
<!--
-----BEGIN PGP SIGNATURE-----
***signature data***
-----END PGP SIGNATURE-----
```
* Now we have an `HTML` file that is signed, but the extension is `.html.asc`. Rename the file `mv <filename>.html.asc <filename>.html`
* Remember the "closing comment" at the beginning and "opening comment" at the end of the file, let's complete them. Prepend `<!--` and append `-->` to the file so that the signature part is inside comments. (these new lines and whatever comes before and after them, is **not** part of the PGP signature.)

Result:

```html
<!--
Hash: SHA512

 -->
<!DOCTYPE html>
<head>
...
</head>
<body>
...
</body>
</html>
<!--
-----BEGIN PGP SIGNATURE-----
***signature data***
-----END PGP SIGNATURE-----
-->
```

Now you're web page is as awesome as mine! Browser gets the `HTML` part, GnuPG gets the signature part, everyone's happy!

### Talk is cheap, show me the code
To automate these steps, I wrote a simple bash-script which was super messy! [Sameer](/pages/jedi-order.html) (May the Source be with him) helped me clean up the mess.

Result:
```bash
#! /bin/bash

find public -name '*.html' -exec sh -c '
    echo "Signing ${1%}";
    sed -i -e "1i\ -->" -e "$ a <!--" "${1%}";
    gpg -u 8CC7EB1535634205E9C2AAD9AF5A5A4AD4FD8797 --clearsign "${1%}";
    mv "${1%}.asc" "${1%}";
    sed -i -e "1i <!--" -e "$ a -->" "${1%}";
  ' sh {} \;
```
Special thanks to [ShellCheck](https://www.shellcheck.net) team for this excellent tool.

This cute little bash-script searches inside the current directory and does everything needed to `--clearsign` `HTML` files. Make sure to replace `public` in third line with the directory you want to crawl and of course replace my PGP fingerprint with your own.

If you know any way I could improve this code, please contact me via email, I would really appreciate it.

### Issues
* As I mentioned earlier, whatever comes before and after, is not part of the content or the signature. So attacker can still prepend and append things to this file; But that would be visually obvious and recognizable. This could be fixed with a `--detach-sign`, but I wanted to keep the signature inside the `HTML` file.
* Since the PGP signature includes multiple hyphens inside our `HTML` comments, it's not W3C standard, but not an issue either. It's a small price to pay.

"But it's already over SSL/TLS! Why do you need to sign it too?" you might say, but sometimes I like to wear my til foil hat and don't put my trust in host providers or CDNs. You know, for Geek's sake!


*Image from [Freepik](https://www.freepik.com/free-vector/smart-contract-web-banner_5902294.htm).*
