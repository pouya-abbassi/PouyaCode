def create():
    with open('output/robots.txt', 'w') as robots:
        robots.write('User-agent: *\nAllow: /\n\nSitemap: https://pouyacode.net/sitemap.xml')
        robots.close()

    with open('output/.htaccess', 'w') as htaccess:
        htaccess.write('<ifModule mod_headers.c>\n  # 1 Day for html, xml and txt\n  <filesMatch ".(html|htm|shtml|xml|txt)$">\n  Header set Cache-Control "max-age=86400, public, must-revalidate"\n  </filesMatch>\n\n  # 1 Month for most static assets\n  <filesMatch ".(css|js|svg|jpg|jpeg|png|gif|ico)$">\n  Header set Cache-Control "max-age=2592000, public"\n  </filesMatch>\n\n  # 1 Year for fonts\n  <filesMatch ".(woff|woff2|ttf|otf|eot)$">\n  Header set Cache-Control "max-age=31104000, public"\n  </filesMatch>\n</ifModule>\n\nRewriteEngine On\nRewriteCond %{HTTPS} off [OR]\nRewriteCond %{HTTP_HOST} ^www\. [NC]\nRewriteCond %{HTTP_HOST} ^(?:www\.)?(.+)$ [NC]\nRewriteRule ^ https://%1%{REQUEST_URI} [L,NE,R=301]')
        htaccess.close()


if __name__ == '__main__':
    create()
