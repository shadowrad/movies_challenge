# movies_challenge

## requirements

1. Provide a REST API to access movies and persons models.
2. Safe methods are publicly available, no authentication is required.
3. Unsafe methods are only available to authenticated users.
4. Movie documents must include references or full documents to persons in their different roles.
5. Person documents must include references or full documents to movies in the different roles the Person has.
6. Movie documents must include the Release Year in roman numerals. This field should not be stored in the DB, just calculated on the fly.
