Feature: Create, Update, and Read categories and links

	Scenario: Create a category
		Given the user is on update/
		When the user clicks add category and enters a category name
		And the user clicks update
		Then the system should add the category
	
	Scenario: Add link to existing category
		Given the user is on update/1
		When the user clicks add link and enters a link label and url
		And the user clicks update
		Then the system should add the link
	
	Scenario: Update existing category name
		Given the user is on update/
		When the user changes a category name
		And the user clicks update
		Then the system should update the changed category
	
	Scenario: Update existing link
		Given the user is on update/1
		When the user changes a link label and url
		And the user clicks update
		Then the system should update the link
	
	Scenario: Add new category and update existing category
		Given the user is on update/
		When the user clicks add category and enters a category name
		And the user changes a category name
		And the user clicks update
		Then the system should add the category
		And the system should update the changed category
	
	Scenario: Add new link and update existing link
		Given the user is on update/1
		When the user clicks add link and enters a link label and url
		And the user changes a link label and url
		And the user clicks update
		Then the system should add the link
		And the system should update the link