from flask import Flask, session, jsonify

from extract import Extract
from transform import Transform
from config import *
from log import Log

app = Flask(__name__)


@app.route('/numbers/<page>', methods=['GET'])
def numbers(page):
    try:
        int_page =  int(page)

        page_index = int_page - 1
        start_index = page_index * LOAD_PAGE_SIZE
        end_index = start_index + LOAD_PAGE_SIZE

        if 0 <= start_index <= len(sorted_list) and  0 <= end_index <= len(sorted_list):
            logger.info(MESSAGE_LOAD_REQUEST.format(page, start_index, end_index))
            logger.info(sorted_list[start_index: end_index])

            return jsonify(
                numbers=sorted_list[start_index: end_index]
            )
        else:
            return jsonify(
                numbers=[]
            )

    except (ValueError, TypeError):
        error_message = MESSAGE_LOAD_REQUEST_ERROR.format(page)

        logger.error(error_message)

        return jsonify(
            error=error_message
        )


if __name__ == '__main__':
    logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)

    extract = Extract(logger, EXTRACT_ADDRESS)
    extracted_list = extract.run()

    transform = Transform(logger)
    sorted_list = transform.run_sort(extracted_list)

    logger.info(sorted_list)

    app.run(host='0.0.0.0', port='8003', debug=False)