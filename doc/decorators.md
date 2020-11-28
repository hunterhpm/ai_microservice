#Route decorators

## Authentification

Used in the controller over the functions to validate different user permissions.

#### jwt_required

Validate that the user has a valid jwt token.

#### admin_required

Validate that the user has the admin role.

This could eventually be changed to validate that the user's role is included in a role array for that route.
