# constants used on the project

EXTRACT_ADDRESS = 'http://challenge.dienekes.com.br/api/numbers'
EXTRACT_PARAM = 'page'

RETRY_MAX_COUNT = 5
RETRY_INTERVAL = 5
RETRY_LONG_INTERVAL = 50

TASK_COUNT = 101

LOG_FILE_TEMPLATE = "./logs/totem-{}.log"
LOG_ID = "DesafioDevCrossCommerce"

MESSAGE_REQUEST_INIT = "Class initialized."
MESSAGE_REQUEST_SUCCESS = "Request success for page '{}'."
MESSAGE_REQUEST_ERROR = "Request error on retry '{}' of page '{}': '{}' - '{}'."
MESSAGE_REQUEST_MAX_RETRIES = "Request max retries of '{}' reached."
MESSAGE_REQUEST_LAST_PAGE = "Last page '{}' reached."
MESSAGE_REQUESTS_PARALLEL_ROUND = "Beginning a new round of '{}' parallel requests for pages from '{}' to '{}'."
MESSAGE_REQUESTS_PARALLEL_ERROR = "Error '{}' on round of parallel requests for pages from '{}' to '{}', retry '{}'."
MESSAGAGE_SLEEPING ="Sleeeping for '{}' seconds."
MESSAGE_SUCCESS = "Success, all pages scanned: '{}' elements fetched."

MESSAGE_TRANSFORM_INIT = "Class initialized."

MESSAGE_MAIN_START = "Start."
MESSAGE_MAIN_EXTRACT_START = "Start extract."
MESSAGE_MAIN_EXTRACT_END = "End extract."
MESSAGE_MAIN_TRANSFORM_START = "Start transform."
MESSAGE_MAIN_TRANSFORM_END = "End transform."
MESSAGE_MAIN_END = "End."
