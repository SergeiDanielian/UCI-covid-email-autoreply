# Why

University of California, Irvine requires all students to reply to a daily email questionnaire asking whether the student is on campus or not on campus, in an effort to contact-trace any on-campus students experiencing covid19-like symptoms.

# What it does

For those who are pemanently off-campus for Fall 2020, this script responds to ALL unread "UCI Student Daily Symptom Monitoring" emails as "Not on Campus Today"

# How to use it

pip install imap_tools lxml
pip install python-decouple

Enable imap access in gmail.
Enable Less Secure App Access to allow imap to login to gmail.

# How to automate

This script can be set up to run daily on task scheduler or as a cronjob.
