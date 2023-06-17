# Contributing

## Prerequisite knowledge

Before contributing to this project, it would be helpful to have a basic understanding of HTML, CSS, and JavaScript. Additionally, familiarity with Hugo is beneficial but not mandatory. If you are new to Hugo, consider visiting [the official Hugo documentation](https://gohugo.io/documentation/) for some insightful resources and learning materials.

## Tech stack

This project primarily uses HTML, CSS​, and JavaScript. The website is built using Hugo and hosted on GitHub Pages. Hugo is a static site generator that uses a command-line interface. You will need to have Hugo installed on your local machine. You can download it from [the official Hugo website](https://gohugo.io/installation/).

## Setup

Before you start, make sure you have a local copy of the project. First, fork the repository on GitHub, then clone it to your local machine using the `git clone` command along with the URL of your forked repository. Here is an example of the command:

```
git clone https://github.com/<YourUsername>/uwswp.co.uk.git
```

## Making changes

To contribute, follow these steps:

- **Run the site locally:** Navigate to the project's root directory in your terminal and execute the `hugo server` command. This command builds the site and makes it accessible on a local server, typically at `localhost:1313`.
- **Implement your changes:** Now, you can start modifying the website's source code. Remember, Hugo websites follow a specific structure. The `content` directory houses the site's content, the `static` directory stores static files such as images, and the `themes` directory contains the site's theme. You can refer to [Hugo's directory structure documentation](https://gohugo.io/getting-started/directory-structure/) for more details.
- **Test your changes:** As the Hugo server runs, it reflects any changes you make to the site on the local server in real-time. It's vital to test your modifications to ensure they behave as expected.
- **Commit and push your changes:** Satisfied with your changes? Great! Commit them using `git commit`, then push them to your GitHub repository with `git push`.
- **Open a pull request:** To wrap up, visit [the GitHub page for the original repository](https://github.com/UWSWP/uwswp.co.uk) and open a pull request. This action alerts the project maintainers that you have some changes for consideration.
