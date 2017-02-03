All data-8 and connector materials should be in python 3. Because the class material is stored and operated on the jupyter hub it is
recommended to test the lectures on the hub before pushing it to the hub (see below  "General workflow on the data-8 jupyter hub" Section).


### Weekly checklist
#### Before the class
- [] Push final materials (lecture/homework/quiz) to data-8/cogneuro-connector (see below  "General workflow on the data-8 jupyter hub" Section)
- [] Create interactive links and update the web-page
- [] Prepare homework assignment on bcourses (schedule to be posted at Tuesdays, 3pm)
- [] Prepare in-class quiz using google forms
- [] Prepare google doc for notes. Naming convention and example: [Cogneuro_Pad_Lecture01](https://docs.google.com/document/d/1-SSZJY55R_ktdg8kXUAR8UevYdHiJFmrfkqr1QM1LiQ/edit)

#### During the class
- [] Attendance on bcourses: Main instructor
- [] Answer questions on google doc: Co-instructors
- [] Fill the instructor feedback document: /Spring2017/Notes_and_Feedback_to_Lectures
- []

#### After the class
- [] Homework assignment released on bcourses?
- [] Grade homeworks form last week.
- [] Cleanup and rename Cogneuro_Pad from the class. Naming convention and example: [Cogneuro_Pad_Lecture01_postclass](https://docs.google.com/document/d/1-SSZJY55R_ktdg8kXUAR8UevYdHiJFmrfkqr1QM1LiQ/edit)
- [] Create a PDF of the Cogneuro_Pad and post on bcourses
- [] Make sure that class surveys are in the corresponding material folder. You can "stop accepting responses" to freeze the form. It's good to do it in class right after, but if you forget please do it now.
- [] Use Verify Drive button on datahub to transfer jupyter notebook from class that includes the breakout session results into the notebook.

### Updating the web-page

### General workflow on the data-8 jupyter hub
1. On your local machine, git-clone the data-8/cogneuro-connector repository.
2. Add weekly material from the shared Google-Drive folder to this local repo in your computer.
3. Push the material to the data-8/cogneuro-connector repository.
4. Connect to the [jupyter hub](https://datahub.berkeley.edu), after authenticating with your berkeley.edu adress, use the right top 
navigation bar to open a terminal (New --> Terminal) .
5. Git-clone the data-8/cogneuro-connector as cogneuro-dev on the jupyter hub

  `git clone https://github.com/data-8/cogneuro-connector.git cogneuro-dev` 

6. Make edits, test lecture and package dependencies etc. on the hub.
7. Commit changes and push to data-8/cogneuro-connector
8. Make interact links of the form: http://datahub.berkeley.edu/user-redirect/interact?repo=data8assets&path=labs/lab01
9. Edit the course webpage and add the new interact links




