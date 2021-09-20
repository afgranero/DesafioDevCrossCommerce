# constants used on the project

EXTRACT_ADDRESS = 'http://challenge.dienekes.com.br/api/numbers'
EXTRACT_PARAM = 'page'

RETRY_MAX_COUNT = 5
RETRY_INTERVAL = 5

LOG_FILE_TEMPLATE = './logs/totem-{}.log'
LOG_ID = 'DesafioDevCrossCommerce'


MESSAGE_REQUEST_INIT ="Class initialized."
MESSAGE_REQUEST_SUCCESS = "Request suceess for page '{}'."
MESSAGE_REQUEST_ERROR = "Request error on retry '{}' of page '{}': '{}' - '{}'."
MESSAGE_REQUEST_MAX_RETRIES = "Request max retries of '{}' reached."
MESSAGE_REQUEST_LAST_PAGE = "Last page '{}' reached."

