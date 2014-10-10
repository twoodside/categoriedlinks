from behave import *
from selenium import *

@given('the user is on the main page')
def step_impl(context):
	context.browser.get('http://obscure-everglades-8713.herokuapp.com/mylinks/')

@given('the user is on update/')
def step_impl(context):
	context.browser.get('http://obscure-everglades-8713.herokuapp.com/mylinks/update/')

@given('the user is on update/1')
def step_impl(context):
	context.browser.get('http://obscure-everglades-8713.herokuapp.com/mylinks/update/1/')
		
	
@when('the user clicks add category and enters a category name')
def step_impl(context):
	button=get_element(context.browser,tag='button',value="Add category")
	button.click();
	textbox=get_element(context.browser,tag='input',value="")
	textbox.value="BehaveTest"

@when('the user clicks update')
def step_impl(context):
	form=get_element(context.browser,tag='form')
	form.submit()
	
@then('the system should add the category')
def step_impl(context):
	category=get_element(context.browser,value="BehaveTest")
	if !category:
		fail("Category wasn't added")
		
@when('the user clicks add link and enters a link label and url')
def step_impl(context):
	button=get_element(context.browser,tag='button',value="Add link")
	button.click();
	textbox_label=get_element(context.browser,tag='input',value="",placeholder="Link")
	textbox_label.value="BehaveTestLink"
	textbox_url=get_element(context.browser,tag='input',value="",placeholder="URL")
	textbox_url.value="http://www.behavetest.com/"
	
@then('the system should add the link')
def step_impl(context):
	link=get_element(context.browser,value="BehaveTestLink")
	if !link:
		fail("Link wasn't added")
		
		
@when('the user changes a category name')
def step_imp(context):
	category=get_element(context.browser,tag="input")
	category.value="BehaveTestUpdate"
	
@then('the system should update the changed category')
def step_imp(context):
	category=get_element(context.browser,value="BehaveTestUpdate")
	if !category:
		fail("Category wasn't updated")

@when('the user changes a link label and url')
def step_imp(context):
	textbox_label=get_element(context.browser,tag='input',placeholder="Link")
	textbox_label.value="BehaveTestUpdateLink"
	textbox_url=get_element(context.browser,tag='input',placeholder="URL")
	textbox_url.value="http://www.behavetestupdate.com/"
	
@then('the system should update the link')
def step_imp(context):
	category=get_element(context.browser,value="BehaveTestUpdateLink")
	if !category:
		fail("Category wasn't updated")
