# [LevantaRequisitos][1]

This is a simple weekend project used as an aid for a complex university project. We, a group of students, needed to raise different requirements for a project in our Software Engineering class. Time went on and nobody decided on how the requirements would be divided, so my proposed solution was to create a small web application where each one picks which requirements they want to do, which are then no longer available for the others. Thus, the work is not divided in a biased way, only those who arrive first can choose to do the ones they prefer.

In addition to that, it also served to facilitate the process of rewriting all the data in LaTeX, since this was the format used for the final report, but only I knew how to use it, so programmatically generating the LaTeX representation of the requirements saved me a lot of work.

## Table of contents

- [LevantaRequisitos](#levantarequisitos)
  - [Table of contents](#table-of-contents)
  - [Technologies used](#technologies-used)
  - [File tree](#file-tree)
- [Usage](#usage)
- [Contributing](#contributing)

## Technologies used

- HTML
  - Bootstrap
- Python
  - Django
- RegEx

## File tree

```
LevantaRequisitos
 ┣ base/                `base` app.
 ┃ ┣ migrations/        `base` app migrations.
 ┃ ┃ ┣ 0001_initial.py  Initial migration.
 | ┃ ┗ __init__.py      Treat this directory as a package.
 ┃ ┣ templates/         `base` app templates.
 ┃ ┃ ┗ base/            `base` app templates.
 ┃ ┃   ┣ index.html     Template for index page.
 ┃ ┃   ┗ latex.html     Template for LaTeX page.
 ┃ ┣ __init__.py        Treat this directory as a package.
 ┃ ┣ admin.py           Model registration for `base` app.
 ┃ ┣ apps.py            App configuration for `base` app.
 ┃ ┣ forms.py           Forms for `base` app.
 ┃ ┣ models.py          Models for `base` app.
 ┃ ┣ urls.py            URL patterns for `base` app.
 ┃ ┗ views.py           Views for `base` app.
 ┣ levanta-requisitos/  Main project folder.
 ┃ ┣ __init__.py        Treat this directory as a package.
 ┃ ┣ asgi.py            ASGI configuration.
 ┃ ┣ settings.py        Main project settings.
 ┃ ┣ urls.py            Main project URL patterns.
 ┃ ┗ wsgi.py            WSGI configuration.
 ┣ templates/           Main project templates.
 ┃ ┗ main.html          Main page template.
 ┣ .gitignore           Patterns ignored by git.
 ┣ LICENSE              Project license.
 ┣ Pipfile              Contains information about dependencies.
 ┣ Pipfile.lock         Contains information about dependencies.
 ┣ Procfile             Used for Heroku deployment.
 ┣ README.md            Project's README.
 ┗ manage.py            Django's CLI utility tool.
```

# Usage

If using my instance, i.e.: you are one of my group members, simply go to the [Heroku deploy][2] and fill the form. That's it.

If not, you will have to deploy your own instance and manually create references for the requirements, using Django's admin page. Then _your_ group members can go to your deployment page and fill the form.

# Contributing

If by some incredibly slim chance you found yourself in the exact same situation I was when creating this, you're more than welcome to contribute. If not, well, you're also welcome.

But again, this was a simple weekend project used as a helper to a bigger, more important project which is now finished. No more of my development time will be allocated for it.

_If you still want to contribute..._ Pull requests are welcome.

Please open an issue to discuss what you'd like to change before making major changes.

Please make sure to update and/or add appropriate tests when applicable.

This project is licensed under the [GPL-3.0 License][3].

[1]: https://github.com/ckc-dev/LevantaRequisitos/
[2]: https://levanta-requisitos.herokuapp.com/
[3]: https://github.com/ckc-dev/LevantaRequisitos/blob/main/LICENSE
