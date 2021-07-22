# 📚 Autograder

### Goals 

Gain hands-on experience with Docker, running containers in the cloud, and Flask with Ajax.

### Introduction

This project is an inquiry of what can be done (and what you give up) with computation in the cloud that is not based on IaaS or PaaS. This project contains an implementation for a cloud-based, scalable auto-grader system for introductory programming courses (think of how MOOCs might grade their Intro programming assignments). In addition there is a side project to test Ajax related capabilities in a flask app.

### Setup

Due diligence for any cloud project starts with setting a budget to limit resource usage overflow. Always be sure to consistently change the AWS region to what is physically closest (as seen in the top right of the dashboard). Create a cost budget, giving adequate notification metrics. It is recommended that an email notification would be sent after 75% of the indicated budget. Below is a screenshot of the budget I created.

![pa2-budget](https://raw.githubusercontent.com/lpg0/autograder/main/img/pa2-budget.png)

### Strategy

Using an EC2 VM instance, create a bash script that runs a python auto grading file. See the following two files for how the shell file operated along side the auto grade file.

![pa2-program](https://raw.githubusercontent.com/lpg0/autograder/main/img/pa2-program.png)

![pa2-autograde](https://raw.githubusercontent.com/lpg0/autograder/main/img/pa2-autograde.jpg)

### Ajax

Flask was used to create a simple web application to subtract two numbers an immediately return the result. Wholistic implementations of this project would involve running the auto grade python file from the flask application, rather than a simple subtract function. 

![pa2-ajax-1](https://raw.githubusercontent.com/lpg0/autograder/main/img/pa2-ajax-1.jpg)

![pa2-ajax-2](https://raw.githubusercontent.com/lpg0/autograder/main/img/pa2-ajax-2.jpg)

### Docker

Docker was also used to containerize the python server with AWS ECS, however this is no longer being maintained, but is recommended as an additional learning segment to this project.

### Notes

This project is no longer being served on AWS due to budget constraints.

### Acknowledgements

Thanks goes to Marty Humphrey (University of Virginia, 2021) for providing project guidelines during CS 4740 S21.
