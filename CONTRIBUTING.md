# Contributing to this document.

To allow for crowdsourcing the curation we have created a [git repository](https://github.com/internetsociety/IETF-Ornithology/) for the document.

The source for this document can be found in the [src directory](https://github.com/InternetSociety/IETF-Ornithology/tree/main/src) of the 
[https://github.com/internetsociety/IETF-Ornithology/](https://github.com/internetsociety/IETF-Ornithology/) repository. Readers are encouraged to contribute by opening [issues](https://github.com/InternetSociety/IETF-Ornithology/issues) or, for those experienced with github, issuing pull requests.


## Technical details
### Local building

For local development: The web and PDF version of this document can be created locally. To generate these from their markdow source use [mdBook](https://rust-lang.github.io/mdBook/cli/init.html) with the [mdbook-pandoc](https://github.com/max-heller/mdbook-pandoc) extension. This tooling is dependent on having [LuaTeX](https://www.luatex.org/), [pandoc](https://pandoc.org/), and the [Hind-Light font](https://fonts.google.com/specimen/Hind) installed. 

On OSX you can set up the environment, assuming you installed [homebrew](https://brew.sh/), by executing the following commands.

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

The workflow is mostly manual, with a few tools that will help you identify new groups and  update the times that groups meet. 


* The markdown files are created with the working group acronym as their name. Their content follows the following template.
```
# The Title of the document

<IETFschedule>Content update by script below</IETFschedule>
* [About GROUP](https://datatracker.ietf.org/group/group/about/)
* keywords: keywords, and trigger words.
* Of interest because: <reason>

Description with an indication of elements 
that may be noteworthy
```




* Remember that for mbook documents `SUMMARY.md` contains the  document structure. Update that document to remove and add content. 
* `./src/IETF/NewWG.md` is updated every meeting using the utility scripts below as a starting point.
* The document only contains information about groups that meet. (That may change in the future.) Files for groups that do not meet are moved to the `src/archive` folder.
* A github action will push the document to the [internetsociety.github.io](https://internetsociety.github.io/IETF-Ornithology/) location.


### Utility Scripts

These are a few quick and dirty python scripts to scrape the datatracker.

#### AgendaUpdate.py

You can run the AgendaUpdate.py tool to update the agenda information between the &lt;IETFschedule&gt; XML elements. Type `AgendaUpdate.py -h` for usage information. A quick and dirty approach to updating the meeting information could be:

`find src/IETF   -name "*.md"  -exec  ./AgendaUpdate.py 120 America/Vancouver {} \;`

similarly the  &lt;IETFschedule&gt; information can be cleared using a command like

`find src -name "*.md" -exec sed -i .bak 's/.*<IETFschedule>.*<\/IETFschedule>/<IETFschedule>* Schedule Unknown<\/IETFschedule>/' {} \;`

#### NewWGs.py

NewWGs.py can be used to figure out which working group are rechartered since last IETF. The following command could be used to generate a list of new working groups since IETF 120 that can be pasted into src/IETF/NewWG.md 


`./NewWGs.py 120  | sort ` 

Note that e.g. AD changes will trigger WGs to be reported as new. Check the history of the group for details.

#### ProposedWG.py

ProposedWGs.py scrapes the datatracker for working groups that are currently being charted, also to be used for content to be copied into src/IETF/NewWG.md

`./ProposedWGs.py | sort `