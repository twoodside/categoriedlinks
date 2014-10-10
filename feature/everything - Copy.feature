Feature: Create, Update, and Read categories and links

	Scenario: Create a category
		Given the user is on the main page
		When the user clicks Edit categories
		Then the user should be taken to /update/
		When the user clicks add category
		Then a new texbox should appear
		When the user enters a category name
		And clicks update
		Then the user should be redirected to the main page
		And the system should add the category
	
	Scenario: Add link to existing category
		Given the user is on the main page
		And a category exists
		When the user clicks the category header
		Then the user should be taken to /update/id of the category
		When the user clicks add link
		Then 2 new textboxes should appear
		When the user enters a link label into the first new textbox
		And the user enters a URL into the second new textbox
		And the user clicks update
		Then the user should be redirected to the main page
		And the system should add the link
	
	Scenario: Update existing category name
		Given the user is on the main page
		And a category exists
		When the user clicks Edit categories
		Then the user should be taken to /update/
		When the user changes a category name
		And clicks update
		Then the user should be redirected to the main page
		And the system should update the changed category
	
	Scenario: Update existing link
		Given the user is on the main page
		And a category exists
		And the category has a link
		When the user clicks the category header
		Then the user should be taken to /update/id of the category
		When the user changes a link label and/or a link URL
		And the user clicks update
		Then the user should be redirected to the main page
		And the system should update the changed link
	
	Scenario: Add new category and update existing category
		Given the user is on the main page
		And a category exists
		When the user clicks Edit categories
		Then the user should be taken to /update/
		When the user clicks add category
		Then a new texbox should appear
		When the user enters a category name
		When the user changes a category name
		And clicks update
		Then the user should be redirected to the main page
		And the system should update the changed category
		And the system should add the category
	
	Scenario: Add new link and update existing link
		Given the user is on the main page
		And a category exists
		And the category has a link
		When the user clicks the category header
		Then the user should be taken to /update/id of the category
		When the user clicks add link
		Then 2 new textboxes should appear
		When the user enters a link label into the first new textbox
		And the user enters a URL into the second new textbox
		And the user changes a link label and/or a link URL
		And the user clicks update
		Then the user should be redirected to the main page
		And the system should update the changed link
		And the system should add the link