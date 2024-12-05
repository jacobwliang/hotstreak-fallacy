# hotstreak-fallacy
Python project that uses statistics to analyze whether basketball's hot-streak fallacy is true. 

What is the Hot Hand Fallacy?
  The belief that players are more likely to make a successful shot after making consecutive successful shots, even when the events are independent.
  
Goal of the Project:
  To investigate whether the "hot hand" phenomenon exists by simulating basketball shot sequences and analyzing probabilities after streaks.
  
Setup:
  1. Simulated 10,000 basketball shot sequences using Python, each consisting of 50 shots.
  2. Assigned each shot a 58% probability of success, matching a player’s true shooting percentage.
  3. Used random number generation to determine whether each shot was successful (1 for success, 0 for miss).
  4. Focused specifically on shot sequences where players made 2 consecutive successful shots (a "hot streak").
  5. Calculated the probability of making the next shot after such streaks to see if it deviates from the baseline shooting percentage of 58%.
  6. Plotted the probabilities of the 10,000 trials using a histogram to visualize the likelihood of a hitting a shot on a streak.

My findings:
  The probability of success after two consecutive makes is approximately the same as the true shooting percentage (58%), with no significant increase in success rate after streaks. Distribution of hotstreaking probabilities was symmetric around the mean, which supports the hot hand fallacy.
  
What I learned/reinforced:
  -two pointer method to traverse arrays 
  -using pandas and statistics modules to modules to clean, analyze, and summarize data
  -creating data visualizations with matplotlib
  -the importance of statistical reasoning in debunking cognitive biases like the hot hand fallacy
