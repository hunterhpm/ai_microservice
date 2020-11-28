ROUTES = {
    'v1': [
        # AUTH
        {
            'rule': '/auth/login',
            'method': 'POST',
            'endpoint': 'auth',
            'function': 'login',
        },
        {
            'rule': '/auth/logout',
            'method': 'POST',
            'endpoint': 'auth',
            'function': 'logout',
        },
        {
            'rule': '/auth/resend-confirmation',
            'method': 'POST',
            'endpoint': 'auth',
            'function': 'resend_confirmation',
        },
        {
            'rule': '/auth/confirm-email',
            'method': 'POST',
            'endpoint': 'auth',
            'function': 'confirm_email',
        },
        # USERS
        {
            'rule': '/users/me',
            'method': 'GET',
            'endpoint': 'users',
            'function': 'get_current',
        },
        {
            'rule': '/users/get-list',
            'method': 'GET',
            'endpoint': 'users',
            'function': 'get_list',
        },
        {
            'rule': '/users/register',
            'method': 'POST',
            'endpoint': 'users',
            'function': 'register',
        },
        # MONITORING
        {
            'rule': '/monitoring/inference',
            'method': 'GET',
            'endpoint': 'monitoring',
            'function': 'inference',
        },
        {
            'rule': '/monitoring/all-inference',
            'method': 'GET',
            'endpoint': 'monitoring',
            'function': 'get_all_inference',
        },
        {
            'rule': '/monitoring/calendar',
            'method': 'GET',
            'endpoint': 'monitoring',
            'function': 'get_calendar',
        },
        # AGENTS
        {
            'rule': '/agents/get-all',
            'method': 'GET',
            'endpoint': 'agents',
            'function': 'get_all_agents',
        },
        # CAMERA
        {
            'rule': '/camera/save-preset',
            'method': 'POST',
            'endpoint': 'camera',
            'function': 'save_preset',
        },
        # MODEL
        {
            'rule': '/models/all-models',
            'method': 'GET',
            'endpoint': 'models',
            'function': 'get_models',
        }
    ]
}