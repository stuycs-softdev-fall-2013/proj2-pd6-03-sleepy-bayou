proj2-pd6-03-sleepy-bayou
=========================

Localized Trip Planner
This program requires:
	selenium, oauth2
	Firefox must be in $PATH
	A good popup blocker.
	
Register for an account:
	Username must be at least 4 characters
	Password must be at least 6 characters

Choose your route:
	Enter start and end destinations. Google maps was used for their suggestions menu.
	Either add your own search term, or choose one from your listed preferences.
	Note that if both options are chosen, the new search term will take priority.
	
Hopstop:
	Since hopstop does not have an API, we decided to screen scrape it in order to get the route.
	It opens a new webdriver browser which will automatically navigate, before scraping the results
	We experimented with headless browsers (which would not open a visible browser), but ran into problems and found it harder to debug.
	
Yelp:
	Using the search term and the list of stations, we iterate through each station and search for nearby matches.
