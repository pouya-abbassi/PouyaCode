def create():
    with open('output/robots.txt', 'w') as robots:
        robots.write('User-agent: *\nAllow: /\n\nSitemap: https://pouyacode.net/sitemap.xml')
        robots.close()

    with open('output/.htaccess', 'w') as htaccess:
        htaccess.write('#Comment | Force all URLs to https WITHOUT www\nRewriteCond %{SERVER_PORT} 80\nRewriteRule ^(.*)$ https://pouyacode.net/$1 [R,L]\n\n#Comment | Force all URLs to https WITH www\nRewriteCond %{SERVER_PORT} 80\nRewriteRule ^(.*)$ https://pouyacode.net/$1 [R,L]')
        htaccess.close()

if __name__ == '__main__':
    create()
