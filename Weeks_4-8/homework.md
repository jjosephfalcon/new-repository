Task — Movie Directors

Step 1: Create a dictionary called movies that stores at least 5 movie titles and their directors.
Create a second dictionary called genres that stores those same 5 movie titles and their genre (Action, Comedy, Horror, etc.)

Step 2: Define a function called get_movie_info(title) that takes a movie title and returns a formatted string with both the director AND the genre. If the title isn't in the dictionary, return "Never heard of it!".

💡 Hint: look up the title in both dictionaries separately, then combine the results into one string using an f-string.

Step 3: Write a while loop that asks the user to enter a movie title. If they type "quit", print "Goodbye!" and break. Otherwise, call get_movie_info() and print the result.

Expected output:

Enter a movie (or quit): Inception

Director: Christopher Nolan | Genre: Sci-Fi

Enter a movie (or quit): The Shining

Director: Stanley Kubrick | Genre: Horror

Enter a movie (or quit): Shrek

Never heard of it!

Enter a movie (or quit): quit

Goodbye!