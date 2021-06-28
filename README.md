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
* to install run `pip install -r  requirements.txt` inside virtual environment

## Run like 
* to install run `pip install -r  requirements.txt` inside virtual environment
* run `./manage migrate` inside virtual environment


## About the app
the project runs with basic authentication, you can test it within the DRF interface.  
It allows you to retreave a list without being logged in but you need to be logged for anything other than GET

##available endpoints 
root **/**: it has a Swagger UI to navigate the API  
`api-token-auth` to login and get a token  
`movie` and `person`
* GET: list all with a list to references
* POST/PUT/DELETE: needs to be authenticated
`alias`: needs to be authenticated for anything (for easy auth test) 

## justifications 
* django and django rest framework: both are great frameworks and are the ones I know the most. 

there other are fastapi or flask but you need to add other things like sqlAlchemy.