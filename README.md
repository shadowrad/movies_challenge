## requirements

1. Provide a REST API to access movies and persons models.
2. Safe methods are publicly available, no authentication is required.
3. Unsafe methods are only available to authenticated users.
4. Movie documents must include references or full documents to persons in their different roles.
5. Person documents must include references or full documents to movies in the different roles the Person has.
6. Movie documents must include the Release Year in roman numerals. This field should not be stored in the DB, just calculated on the fly.

## Packages
*django
*django rest framework
* to install run `pip install -r  requirements.txt` inside virtual enviroment

## Run like 
* to install run `pip install -r  requirements.txt` inside virtual enviroment

## About the app
the project runs with basic authentication, you can test it within the DRF interface.  
It allows you to retreave a list without being logged in but you need to be logged for anything other than GET

