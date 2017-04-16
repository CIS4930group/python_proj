# Python project info

Project writeup: Website will feature a name at the top saying the website name, then it will have 3 drop down menus “Select your categories or select random for all categories or an individual category” each menu has a header at the top drop downs will include all the items or a random option Button at bottom for submit submit button checks if the user selected an item for each category (or if they selected random for that category) Random button that once pressed acts like the submit button except adds a random value for all categories If they didn’t select anything in a category, will need to alert user with a dialog box or something Once user has selected an item from each category: If user has random selected for any categories, will just perform rand function on a list of all the items and select one for each category. Two options (based on time constraints):

Will have a database mapping all 3 categories to different URLs of recipes a.	Could be a dict where the key is a tuple of the 3 items and the value is the website, or the value is a tuple of multiple websites that will then produce a random one from that list
(Not sure if this one is even viable) Will take the three items from each category, then search recipes website for the first listing that contains those 3 items and is rated highly. Both options just return the website URL as a hyperlink that says the name of the recipe.
Timeline:

Make Front-end of website featuring just the drop downs, and other content without any functionality
Add in the backend of storing all of the items
Implement one of the two options for searching for the recipe
Add in the hyperlink and a new recipe button (just refreshes the page but with a new recipe instead of the one already displayed, this will not display until the submit button has been clicked)
