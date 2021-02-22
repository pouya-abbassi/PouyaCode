#! /bin/bash

find public -name '*.html' -exec sh -c '
    echo "Converting ${1%}";
    sed -i -e "1i\ -->" -e "$ a <!--" "${1%}";
    gpg -u 8CC7EB1535634205E9C2AAD9AF5A5A4AD4FD8797 --clearsign "${1%}";
    mv "${1%}.asc" "${1%}";
    sed -i -e "1i <!--" -e "$ a -->" "${1%}";
  ' sh {} \;


cp static/* public/
cp public/404.html public/404.shtml
