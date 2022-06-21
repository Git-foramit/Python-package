# Documentation

The documentation for this project is written
using [Material](https://squidfunk.github.io/mkdocs-material/getting-started/)
for [MkDocs](https://www.mkdocs.org/) is a theme for MkDocs, a static site generator geared towards (technical) project
documentation.

The packages for documentation are already installed. What you need to do is to place your documentation in the
folder `docs` in form of Markdown files `.md`.

As a part of the CI/CD pipeline, the documentation is then build and published for in the github pages
https://pages.github.com/bosch-top98-ai-know/your-project/.

To see your documentation in action execute the following script from the root of your project:

<div class="termy" data-ty-typeDelay="10">

```console
$ make serve-docs

mkdocs serve
<span style="color: green;">INFO</span>    -  Building documentation...
<span style="color: green;">INFO</span>    -  Cleaning site directory
<span style="color: green;">INFO</span>    -  Documentation built in 4.63 seconds
[I 210427 13:29:41 server:335] Serving on http://127.0.0.1:8000
<span style="color: green;">INFO</span>    -  Serving on http://127.0.0.1:8000
[I 210427 13:29:41 handlers:62] Start watching changes
<span style="color: green;">INFO</span>    -  Start watching changes
[I 210427 13:29:41 handlers:64] Start detecting changes
<span style="color: green;">INFO</span>    -  Start detecting changes

```

</div>

and open you browser at: [http://localhost:8000/](http://localhost:8000/).

We use [mike](https://github.com/jimporter/mike) to deploy different versions of the documentation. This is already
setup as github actions, so you don't need to configure anything else.

!!! info If building and deploying documentation with github fails with error like this:
```
error: failed to push branch gh-pages to origin: "To https://github.boschdevcloud.com/<org>/<your-project>
! [rejected]        gh-pages -> gh-pages (fetch first)
error: failed to push some refs to 'https://github.boschdevcloud.com/<org>/<your project>'
hint: Updates were rejected because the remote contains work that you do hint: not have locally. This is usually caused by another repository pushing hint: to the same ref. You may want to first integrate the remote changes hint: (e.g., 'git pull ...') before pushing again. hint: See the 'Note about fast-forwards' in 'git push --help' for details."
make: *** [Makefile:47: publish-docs] Error 1
```
Just restart the github actions job, or commit a new version with something changed in the `docs/` directory. This
should fix the problem.
