# infovis_grading_tool

This is a tool for showing all the student submission in one page. 

For those submissions you want to further check, you can click the link on top of the mini view and then you will be led to a new page of this submission.

## Demo
First, you need to run `preporsssing.py` which will create a new folder call `to_view` with all the student submissions in the `raw_submission` folder and the data files (`routes.csv` and `contries.geo.json`) as well as d3 library. In the `to_view` folder, all the student submissions will be renamed in the form of `[netid]_index.html`. To run the python code, you can run the following command line:

```console
$ python3 preprocessing.py
```

Then you need to run a local server at the position of this project. For example, you can run the following command line:

```console
$ python3 -m http.server
```

And then open the link of [localhost: 8000](http://0.0.0.0:8000/) to view all the submissions. With the data of demo submissions in the `raw_submission` folder, you can see the page as shown below:
![](https://user-images.githubusercontent.com/9759891/67642710-f2b9b700-f8e4-11e9-9c33-4a86d807e99a.png)

## Load lab submissions
To use this tool for grading lab submissions, you should first download all the submissions of the the lab to be graded. There is an option of `Download All ` on the course page when viewing assignment submissions. 

In practice, you should unzip the downloaded package. And then rename the unzipped folder as `raw_submission` and put it in this project. There is already a folder with the name of "raw_submission" just for demo. You can replace the existing "raw_submission" with the upzipped folder of submissions you want to check.

## Grading Principle

1. If the submission looks similar to the target view (as described in the assignment description), then grade it as `Pass`.
2. If there is anything different, click the netid link and debug it (usually just a minor mistake). Find out the bug, and leave a comment of how to fix it to the student in the grading page.
