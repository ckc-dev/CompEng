# unWaste - Industrial Waste Recycling Platform

"unWaste" is an interdisciplinary school project between the computer and manufacturing engineering courses, carried out in the fifth semester. This project centers around the creation of an online platform, designed for the streamlined recycling of specific industrial waste materials. Our main objective is to expedite the recycling processes, ultimately reducing the time it takes for these waste materials to become suitable for resale.

unWaste is dedicated to assisting industries in responsible waste disposal by offering comprehensive information about discarded materials. We provide tailored guidance for the removal process, which varies based on waste type and quantity. Our specialization lies in treating materials such as ABS (Acrylonitrile Butadiene Styrene) and PP (Polypropylene). For materials beyond our scope, we collaborate with specialized recycling companies to ensure proper treatment.

By bridging the gap between waste disposal and recycling, unWaste contributes to sustainable practices and environmental preservation.

This is the repository for the concept website.

## Technologies used

- Python
  - Django
- HTML
- CSS
- JavaScript

## Table of contents

- [unWaste - Industrial Waste Recycling Platform](#unwaste---industrial-waste-recycling-platform)
  - [Technologies used](#technologies-used)
  - [Table of contents](#table-of-contents)
  - [File tree](#file-tree)
- [Contributing](#contributing)

## File tree

```
unWaste
 ┣ base/
 ┃ ┣ migrations/
 ┃ ┃ ┣ 0001_initial.py                                              Initial migration for the `base` app.
 ┃ ┃ ┣ 0002_user_cnpj_user_cnpj_clean_user_is_business_and_more.py  Migration for user and business-related data in the `base` app.
 ┃ ┃ ┣ 0003_passwordresetrequest.py                                 Migration for password reset requests in the `base` app.
 ┃ ┃ ┣ 0004_wastecollectionrequest.py                               Migration for waste collection requests in the `base` app.
 ┃ ┃ ┣ 0005_alter_wastecollectionrequest_waste_type.py              Migration for altering waste types in the `base` app.
 ┃ ┃ ┗ __init__.py                                                  Initialization file for treating the `migrations` directory as a package.
 ┃ ┣ static/
 ┃ ┃ ┗ base/
 ┃ ┃ ┃ ┗ scripts/
 ┃ ┃ ┃ ┃ ┗ register.js  JavaScript file for user registration in the `base` app.
 ┃ ┣ templates/
 ┃ ┃ ┗ base/
 ┃ ┃ ┃ ┣ about-us.html            HTML template for the 'About Us' page in the `base` app.
 ┃ ┃ ┃ ┣ authentication.html      HTML template for authentication-related pages in the `base` app.
 ┃ ┃ ┃ ┣ index-juridical.html     HTML template for legal entity index page in the `base` app.
 ┃ ┃ ┃ ┣ index-landing-page.html  HTML template for landing page in the `base` app.
 ┃ ┃ ┃ ┣ index-physical.html      HTML template for physical entity index page in the `base` app.
 ┃ ┃ ┃ ┣ index.html               HTML template for the index page in the `base` app.
 ┃ ┃ ┃ ┣ password-reset.html      HTML template for password reset page in the `base` app.
 ┃ ┃ ┃ ┣ privacy-policy.html      HTML template for privacy policy page in the `base` app.
 ┃ ┃ ┃ ┣ settings.html            HTML template for user settings page in the `base` app.
 ┃ ┃ ┃ ┗ terms-of-service.html    HTML template for terms of service page in the `base` app.
 ┃ ┣ __init__.py                  Initialization file for treating the `base` directory as a package.
 ┃ ┣ admin.py                     Django admin configuration for the `base` app.
 ┃ ┣ apps.py                      App configuration for the `base` app.
 ┃ ┣ forms.py                     Forms related to the `base` app.
 ┃ ┣ models.py                    Models for the `base` app.
 ┃ ┣ tests.py                     Tests for the `base` app.
 ┃ ┣ urls.py                      URL patterns for the `base` app.
 ┃ ┣ utils.py                     Utility functions for the `base` app.
 ┃ ┗ views.py                     Views for the `base` app.
 ┣ static/
 ┃ ┣ images/
 ┃ ┃ ┗ svg/
 ┃ ┃ ┃ ┣ background.svg   SVG image for the background.
 ┃ ┃ ┃ ┣ logomark.svg     SVG image for the logomark.
 ┃ ┃ ┃ ┗ logotype.svg     SVG image for the logotype.
 ┃ ┣ scripts/
 ┃ ┃ ┗ script.js  Main project JavaScript file.
 ┃ ┗ styles/
 ┃ ┃ ┣ reset.css  CSS reset file.
 ┃ ┃ ┗ style.css  Main project CSS file.
 ┣ templates/
 ┃ ┣ footer-items.html  HTML template for footer items.
 ┃ ┣ main.html          Main HTML template for the project.
 ┃ ┗ navbar-items.html  HTML template for navbar items.
 ┣ unwaste/
 ┃ ┣ __init__.py  Initialization file for treating the `unwaste` directory as a package.
 ┃ ┣ asgi.py      ASGI configuration for the project.
 ┃ ┣ settings.py  Project settings.
 ┃ ┣ urls.py      Project-level URL patterns.
 ┃ ┗ wsgi.py      WSGI configuration for the project.
 ┣ .gitignore     Git ignore file.
 ┣ LICENSE        Project license.
 ┣ Pipfile        Dependency information file.
 ┣ Pipfile.lock   Locked dependency information file.
 ┣ README.md      Project's README.
 ┗ manage.py      Django's CLI utility tool.
```

# Contributing

Pull requests are welcome.

Please open an issue to discuss what you'd like to change before making major changes.

Please make sure to update and/or add appropriate tests when applicable.

This project is licensed under the [GPL-3.0 License](./LICENSE).
