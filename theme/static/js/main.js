document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach( el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});


function imageshow(){
    document.getElementById('imagemodal').style.display = 'flex';
}


function imagehide(){
    document.getElementById('imagemodal').style.display = 'none';
}



document.onreadystatechange = function () {
    if (document.readyState == "complete") {
        // Defer loading FontAwesome css
        var fa = document.createElement('link');
        fa.rel = 'stylesheet';
        fa.type = 'text/css';
        fa.href = '/theme/css/font-awesome.min.css?v=0';
        var fa_defer = document.getElementsByTagName('link')[0];
        fa_defer.parentNode.insertBefore(fa, fa_defer);

        try{
            // Set event for show/hide modal image on article page.
            document.getElementById('show').addEventListener("click", imageshow);
            document.getElementById('hide').addEventListener("click", imagehide);
            document.getElementById('modalx').addEventListener("click", imagehide);
        }catch(_){}

        try {
            // Email obfuscation using ROT13 for navbar.
            let rot13 = document.getElementById('email').href.replace(/[a-zA-Z]/g,function(c){return String.fromCharCode((c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);});
            document.getElementById('email').href = rot13;

            // Email obfuscation using ROT13 for articles.
            let subject = document.getElementsByClassName('article-title')[0].innerHTML;
            subject = subject.substr(subject.search('&nbsp')+6);
            rot13 += '?subject=' + subject;
            document.getElementById('feedback').innerHTML = '<a href="' + rot13 + '"><i class="fas fa-at"></i>&nbsp;Send feedback</a>';
        }catch(_){}
    }
};
