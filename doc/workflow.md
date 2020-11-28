#Adding route

Adding a route is done in 3 steps.

## Handlers

Create or update an existing handler with a function with the query logic.

These should include responses: success and error handling.

Error responses can be found in __controllers/v1/errors__.

Example:

    def get_current_user():
        username = get_jwt_identity()
        if isinstance(username, str):
            user = User.query.filter_by(username=username).first()
            return jsonify({
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'registered_on': user.registered_on
                }
            }), 200
    
        return errors.unauthorized(message='login_required')


## Controllers

In the appropriate controller, add a function with associated logic and/or handler.

Add the appropriate route decorators.

These decorators can be found in the [decorators documentation](./decorators.md).

Example:
    
    @jwt_required
    def get_current():
        return get_current_user()
        

## Route config

Define the route parameters.

- Rule: Route url
- Method: Route method
- Endpoint: File in the controllers
- Function: Function in the controller

Example:

    {
        'rule': '/users/me',
        'method': 'GET',
        'endpoint': 'users',
        'function': 'get_current',
    },
