# <center>CC_Redact_Iter3</center>

This is the third iteration of my CC_Redact website, a fresh attempt at my previous Fake Chuckee Cheese Neptune Membership Card Redactor App. 

The main purpose of this project is to accept the web site visitor's fake membership card number and redact it.

What distinguishes this iteration of this poject from previous iterations is that this time around I intend on using only a single template (the home page / landing page) to handle all the functionality. 

This project includes three core apps:
* <strong>redactors</strong>: This app accepts the user's 12 digit card number as input and then processes (redacts) it
* <strong>posts</strong>: This app is kinda like a blog post, but in my production environment I intend on invoking this app only once to create a single blog post which will contain my 'post-mortem' to (document everything I learned while writing this Django site)
* <strong>counters</strong>: This app will eventually count all the words used in the postmortem and present the data to the user. But for now it just counts the most common words in a text file of the public domain work Alice and Wonderland - - which was a project that I have worked on for a previous Python shell script that I wrote in 2019

After the above features are implemeneted, later I plan on adding these three minor additional features:
* When the usr clicks the 'Redact' button, the results 'gently' animate into existence.  
* A page view hit counter
* Show current time and date at bottom of landing webpage
* Public domain copyright note with dynamic year value
