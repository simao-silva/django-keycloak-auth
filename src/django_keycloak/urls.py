# KEYCLOAK SERVER
BASE_PATH = "/auth"

# REST API
KEYCLOAK_INTROSPECT_TOKEN = "{}/realms/{}/protocol/openid-connect/token/introspect"
KEYCLOAK_USER_INFO = "{}/realms/{}/protocol/openid-connect/userinfo"
KEYCLOAK_GET_USERS = "{}/admin/realms/{}/users"
KEYCLOAK_GET_TOKEN = "{}/realms/{}/protocol/openid-connect/token"
KEYCLOAK_GET_USER_BY_ID = "{}/admin/realms/{}/users/{}"
KEYCLOAK_GET_USER_CLIENT_ROLES_BY_ID = (
    "{}/admin/realms/{}/users/{}/role-mappings/clients/{}"
)
KEYCLOAK_UPDATE_USER = "{}/admin/realms/{}/users/{}"
KEYCLOAK_CREATE_USER = "{}/admin/realms/{}/users"
KEYCLOAK_SEND_ACTIONS_EMAIL = "{}/admin/realms/{}/users/{}/execute-actions-email"
KEYCLOAK_DELETE_USER = "{}/admin/realms/{}/users/{}"
KEYCLOAK_OPENID_CONFIG = "{}/realms/{}/.well-known/openid-configuration"


# ADMIN CONSOLE
KEYCLOAK_ADMIN_USER_PAGE = (
    "{host}/auth/admin/master/console/#/realms/{realm}/users/{id}"
)