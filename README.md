# infovis_grading_tool

This is a tool for showing all the student submission in one page. 

For those submissions you want to further check, you can click the link on top of the mini view and then you will be led to a new page of this submission.

##Usage

To use this tool, you should first download all the submissions to this project. There is an option of `Download All ` on the course page when viewing submissions. 

In practice, you should unzip the submission package. And then rename the unzipped folder as `raw_submission` and put it in this project. There is already a folder with the name of "raw_submission" just for demo. When you need to grade the new  assignment, just replace the existing "raw_submission" folder with the folder of submissions you want to check.

Now you need to run `preporsssing.py` which will create a new folder call `to_view` with all the student submissions and the data files as well as d3 library. In this folder, all the student submissions will be renamed in the form of `[netid]_index.html`. To run the python code, you can run the following command line:

```console
$ python3 preprocessing.py
```

In the end, run a loacal server at the position of this project. For example, you can run the following command line:

```console
$ python3 -m http.server
```

And then open the link of [localhost: 8000](http://0.0.0.0:8000/) to view all the submissions.

## Grading Principle

1. If the submission looks similar to the target view (as described in the assignment description), then grade it as `Pass`.
2. If there is anything different, click the netid link and debug it (usually just a minor mistake). Find out the bug, and leave a comment of how to fix it to the student in the grading page.