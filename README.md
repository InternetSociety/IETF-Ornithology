# The IETF Ornithology

The IETF Ornithology is an effort to allow crowdsourcing  the identification of public policy issues in IETF work.

You can read the Ornithology through as a [web page](https://kolkman.github.io/IETF-ornithology/) or as a [pdf](https://kolkman.github.io/IETF-ornithology/IETF-Ornithology.pdf)

The source for this document can be found in the [src directory](gitub.com/kolkman/ornithology/src) of the 
[gitub.com/kolkman/ornithology/]() repository. Readers are encouraged to contribute. 

For local development: The web and pdf version of this document need to be created locally and pushed to the GitHub repository. The web and PDF versions can be created from their source with
[mdBook](https://rust-lang.github.io/mdBook/cli/init.html) using the
[mdbook-pandoc](https://github.com/max-heller/mdbook-pandoc)
extension. This tooling is dependent of having
[LuaTeX](https://www.luatex.org/),  [pandoc](https://pandoc.org/), and
the [Hind-Light font](https://fonts.google.com/specimen/Hind) installed. 

On OSX you can set up the environment, assuming you installed
homebrew, by executing the following commands.

``` 
brew install rust pandoc mdbook mactex

# make sure the mactex paths are set:
eval "$(/usr/libexec/path_helper)"

cargo install mdbook-pandoc
echo 'PATH="/Users/olaf/.cargo/bin:$PATH"' > ~/.zshrc 
export PATH="/Users/olaf/.cargo/bin:$PATH"

```

The Hind font you have to install through the font install tools of your OS.

Once that is done - you can just run ```mdbook build``` from the root of this directory.


### Tools and conventions

Files are usually created as follows:


````
# The Title of the document

<IETFschedule>  * IETF120: Mon 22 Jul 2024 13:00 - Regency E/F</IETFschedule>
* [GROUP](https://datatracker.ietf.org/group/group/about/)
* keywords: keywords, and trigger words.

Description with an indication of elements that may be noteworthy


```


You can run the AgendaUpdate.py tool to update the agenda information between the <IETFschecule> XML elenments. A quick and dirty approach could be:

``` find src/IETF  -type file  -exec  ./AgendaUpdate.py 120 America/Vancouver {} \;```