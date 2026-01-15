# 2. Choosing a layout

Before defining the HTML and CSS, consider the overall structure and navigation of your web app
interface.

## Getting started

### Tutorial app

The tutorials are based on creating a paralympics app for use in schools (ages 11 to 16) for
students to analyse paralympics data and answer homework questions. The app will have a dashboard
and a quiz/questions feature.

The overall design is a multipage app with a page for the charts and a page for the quiz feature.

### Coursework app

A suggested approach for the coursework:

1. Consider your wireframes from COMP0035 coursework 2

    - Do you expect the users to use a mobile or laptop/desktop device?
    - What charts, content and features does your app have?
2. Decide on single versus mutipage and the navigation approach

    - Is a single page or multipage layout better suited given the answers to question 1?
    - How will a user navigate the app (especially if multipage)?
3. Is a grid and/or flex layout appropriate?
4. Choose an open source third-party CSS to use to create the layout and style of the app.

    - Consider the availability of documentation and support available. Some popular CSS frameworks:

        - [Bootstrap](https://getbootstrap.com)
        - [Tailwind CSS](https://tailwindcss.com)
        - [Materialize](https://materializecss.com)
        - [Pure.css](https://purecss.io)
        - [Bulma](https://bulma.io)
        - [Foundation](https://get.foundation)

    - Use Bootstrap if you don't have a preference.

## Paralympics layout

The paralympics app will use a 12-column grid layout defined using Bootstrap styles.

<img alt="Paralympics app grid" src="../img/grid.png" style="width: 30%;"/>

This may need to be adapted for each of the frameworks as the tutorials progress.

## Next activity

[Dash version](3-dash-layout.md)

[Flask version](3-flask-layout.md)

[Streamlit version](3-streamlit-layout.md)
