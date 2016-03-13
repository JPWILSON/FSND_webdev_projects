#Full Stack Web Developer Nanodegree - Project 2 README

This is my **second README!** 
It details the format of my submission for Project 2 - a game tournament database. 

GitHub: https://github.com/JPWILSON/FSND_webdev_projects

##About

Two main folders are attached in this submission. 

- The first folder contains my main project submission, intended to exceed expectations.
	The folder is named: Xtra_cred_submission 
  It contains the basic functionality and, in addition:
  	- Allows for draws instead of only wins and losses
      (A win gets 2 points, a draw gets 1 point, a loss gets 0 points)
  	- Allows for multiple tournaments to be played and stored

  It contains the following files:
  	- Schema Diagram.jpg * this is a visualisation of the four tables and how they
                              are related
  	- tournament.py 		 * this contains my python functions to query the database
  	- tournament.sql 		 * this contains my database schema, with four tables. 
  	- populate.py 			 * this may not be necessary, but was used to populate the 
      							        the database during testing and development
  	- tournament_test.py * this contains the UNEDITED test suite, provided by Udacity.
                           Please Note: I was uncertain about whether I could change it and therefore it does not 
                           test the 7th function - ReportMatch. It correctly tests all other functions in tournament.py, 
                           unless ReportMatch is included in the test. I would have modified this test, but instead made 
                           explanations (comments) in the tournament.py file, as I wasn't sure if modification of this file 
                           was permitted. (I did however modify the ReportMatch function in tournament.py in order to 
                           include the added fields in the matches table, as alluded to in the extra credit notes).  


- The second folder contains my basic project that meets expectations.
	It is named: Basic_submission 
  The main reason for it's inclusion is so that, if I misunderstood the 
  requirements for extra credit, at the least my basic submission can be graded. 
  Although this is already stated, PLEASE IGNORE THIS FILE IF EXTRA CREDIT ACCEPTABLE.

  It contains the following files:
  	- tournament.py 		  * this contains my python functions to query the database
  	- tournament.sql 		  * this contains my database schema
  	- populate.py 			  * this may not be necessary, but explains how I populated
  							             my database during testing and development
  	- tournament_test.py 	* this contains the UNEDITED test suite, provided by Udacity


##How To Use

- Get started by installing the dev env (vagrant up, ssh, etc). Open psql in git, import the database 
  SQL file: i\ tournament.sql, then run the populate.py or the tournament.test.py files 
  to check that it works as required.  
- Most important: All methods in tournament.py have been included, and all views 
  in tournament.sql have been included. HOWEVER, some of each have been commented out 
  (with relevant, detailed explanations included) to ease the testing of this project. That is, with 
  the intention of making tournament_test.py be as functional as possible. 
  This means that there is no redundant code in the comments, and everything can be used, 
  as per the explanations in the comments. 
- Please read the comments in the code, they are exhaustive, to the point of tedium,
  but at the very least, should eliminate confusion on what my code does (or is supposed to do), 
  and how it does this, and lastly how to test that it does this. 
  Obviously,
- Ensure that Python is installed on the machine running these modules. (2.7 or later) 
- Make sure that the relevant python modules are located in the same folder
- Run the various functions in tournament.py to test the funcionality of the database.
  Note that populate.py and tournament_test.py may assist in checking the functionality. 


##Project Explanation

The extra credit components that have been incorporated (i. to allow for draws ii. to accomodate multiple 
tournaments) require four tables instead of two, and require additional fields in 
the 'matches' table. Please note that 'wins' in player standings is actually the points - NOT the number 
of wins, but still orders the standings correctly. The wins could be shown by just dividing the points by 2, 
but this would require minor changes to tournament_test.py which I am not sure is permitted. 
However, standings doesn't change. 

Additional functions in tournament.py are required for the added functionality. Those added are: 
   - countPlayersTournament()
   - registerPlayerTourney()
   - registerTourney()
   - winnerTourney()
   - playerStandings_tourney() - commented out for ease of testing. 



##Contributing

I will load this on GitHub and then happilly welcome anyone to provide any constructive 
criticism of this project in particular, or my coding in general. I just want to get better. 


##License

tl;dr - The MIT License (MIT)

So, I don't really care about trying to own information, this isn't the 90s.
Do what you like with this or anything else as I don't think anyone can actually own information, just because current laws say that they can. I mean, who am I to say who can
know what, or who on earth thinks they can dictate what my mind is allowed to know...
So, take this and use it, and any other code I write. 


##Add Later

This is still a tiny little repository, but as it grows I intend to add:
-FAQ
-Table of Contents
