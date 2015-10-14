DLBB
====
:book: :hammer: DLBook Builder

Tired of manually printing every *.html page from the [DLBook](http://www.iro.umontreal.ca/\~bengioy/DLbook/) webpage? 
Here is your python script. It's like printing by hand, except you don't have to :smile:

This script will generate a full local pdf version of the DLBook just for you.

Requirements
------------
>* wget (1.13.4)
>* pdftk (1.44)
>* beautifulsoup4 (4.4.1)
>* cmdlnprint (0.6.1) Firefox Add-on

- to install cmdlnprint, open latest *.xpi from [Torisugari](https://github.com/Torisugari/cmdlnprint) with your Firefox and allow the installation of not signed Add-ons.
- to improve printed outcome, remove entries for *print_headerleft*, *print_headerright*, *print_footerleft* and *print_footerright* in the **about:config** in Firefox

Tested with
------------
>* Ubuntu 12.04
>* Firefox 41.0
>* Python 2.7.3

Terminal
----------------------

```
python bookbuilder.py --webpage=http://www.iro.umontreal.ca/~bengioy/DLbook/
```

Use commandline arguments to adjust the time between prints e.g.

```
--seconds=20
```
