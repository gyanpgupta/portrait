### Status
[![Build Status](https://travis-ci.org/gyanpgupta/portrait.png)](https://travis-ci.org/gyanpgupta/portrait)


# Portrait
Django app which accepts a photo upload via a form, and then displays that photo back to the user.

### Description.
Django app which accepts a photo upload via a form, and then displays that photo back to the user without saving the uploaded file, 
Test cases for this app which checks that a POST request to the upload route correctly returns the uploaded photo as the response body.
Continuous Integration testing for this app.

### Installation
```git clone https://github.com/gyanpgupta/portrait.git ```

### GitHub Repo
[git repository](https://github.com/gyanpgupta/portrait.git) 

### Travis
https://travis-ci.org/gyanpgupta/portrait

### Prerequisites
* create virtual environment 
	```virtualenv -p python3.6 <env_name>```
* run  ```pip install -r requirements.txt``` to install dependencies.
	* Django==1.11
	* Pillow==5.0.0

### Usage
* First activate virtual environment .
	* go environment path like cd env_name
	* execute command ```source bin/activate```
* To run app
	* ```cd Portrait```
	* ```python manage.py migrate```
	* ```python manage.py runserver```

### To run TestCases
* ```python manage.py test```
* Test Cases tested
	* Valid form
	* Invalid form with invalid image field
	* Invalid form with empty fields


### Code Coverage
* ```coverage run manage.py test```