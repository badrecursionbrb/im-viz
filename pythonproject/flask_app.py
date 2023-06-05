import logging
from flask import Flask, request, json, Response, flash, redirect, url_for
from exceptions.exceptions import *
from werkzeug.utils import secure_filename

from main import main
from util import read_xes_to_log
from util import check_validity_of_logstr, LOGSTRING_VALID_REGEX
from log_from_string.string_to_log import string_to_log

from flask_cors import CORS  


FORMAT = '%(asctime)s pid: %(process)d-%(levelname)s- %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT) # TODO change for production

flask_app = Flask(__name__)
UPLOAD_FOLDER = './tmp_files'
ALLOWED_EXTENSIONS = {'xes', 'xlsx', 'xls'}

flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
flask_app.secret_key = 'YOURSECRETKEYTODOCHANGE'
flask_app.config['SESSION_TYPE'] = 'filesystem'

cors = CORS(flask_app)

LOGFILE_PARAM = "logfile"
LOGSTRING_PARAM = "logstring"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_get_code(error) -> int:
    if not hasattr(error, 'code'):
        code = 500
    else:
        code = error.code
    return code 


@flask_app.post('/get_visualization_data_file')
def post_visualization_data_file():
    """ This request accepts a post request to the above url and is designed for a logfile.
        The API endpoint expects a JSON with the logfile in it and also parameters.
        Also checks the request for validity.
        The logfile is then also converted to a event log using PM4PY
        
    Raises:
        NoFilePartError: Error that is raised if there is no file present in the request
        NoFileSelectedError: Error that is raised if no file is selected, i.e. empty file 
        UnimplementedFileExtensionError: Error raised if a file is supplied that has a file
                                        extension that is not implemented
        NotAllowedFileExtensionError: Error that is raised if a file is supplied that has a file 
                                    extension not allowed

    Returns:
        http-response : a http-response either with success status code or some error code
    """
    try:
        request_args = request.args
        # check if the post request has the file part
        logging.debug(request.files)
        if LOGFILE_PARAM not in request.files and LOGFILE_PARAM not in request.form:
            flash('No file part')
            raise NoFilePartError()
        try: 
            logfile = request.files[LOGFILE_PARAM]
        except Exception as e:
            logging.debug("file not found in request.files, searching in request.form ...")
            logfile = request.form[LOGFILE_PARAM]
        logging.debug("#################### the logfile is: {}".format(logfile))
        if logfile.filename == '':
            flash('No selected file')
            raise NoFileSelectedError()
        if logfile and allowed_file(logfile.filename):
            filename = secure_filename(logfile.filename)
            if filename.endswith('.xes'):
                compatible_logfile = read_xes_to_log(logfile)
            else:
                raise UnimplementedFileExtensionError()
            return handle_visualization_data_request(log=compatible_logfile, request_args=request_args)
        else:
            raise NotAllowedFileExtensionError()
    except (NoFilePartError, NotAllowedFileExtensionError, NoFileSelectedError, UnimplementedFileExtensionError) as e:
        return Response("Error during execution: " + str(e), status=e.code)
    except Exception as e:
        return Response("Error during execution: " + str(e), status=400)
        

@flask_app.post('/get_visualization_data_logstring')
def post_visualization_data_logstring():
    """ This request accepts a post request to the above url and is designed for a handwritten 
        logstring. The API endpoint expects a JSON with the logstring in it and also parameters.
        Also checks the request for validity.
        The logstring is converted to an EventLog using a method supplied by the chair 
        
    Raises:
        LogstringError: Custom Error if the logstring in the JSON is not valid, then the request 
                        is returned with ann error status code.

    Returns:
        http-response : a http-response either with success status code or some error code
    """
    # TODO change next line to = True
    try:
        json_body = request.get_json(silent=False)
        request_args = request.args
        logging.debug("#################### the logstr is: {}".format(json_body))
        logstr = json_body.get(LOGSTRING_PARAM)
        logging.debug(logstr)
        if check_validity_of_logstr(logstr):
            log = string_to_log(logstr)
            return handle_visualization_data_request(log=log, request_args=request_args)
        else:
            logging.debug("Logstring is erroneous")
            raise LogstringError(expression=logstr, message="Logstring is erroneous for regex: " + 
                                LOGSTRING_VALID_REGEX)
    except (InputError, LogstringError) as e:
        logging.error("Exception occurred because of input", exc_info=True)
        return Response("Exception occurred because of user input " + str(e), 
                        status=check_get_code(e))
    except Exception as e:
        logging.error("Exception occurred ", exc_info=True)
        return Response("Error during execution: " + str(e), status=400)
    
        
def handle_visualization_data_request(log, request_args):
    """ Method for unifying the request endpoints for logstring and logfile 

    Args:
        log : EventLog or similar type that is accepted by the inductive miner algorithm
        request_args: data structure that has the arguments of a request 

    Returns:
        http-request:  a http-response either with success status code (200) or some error code
    """
    try:
        ret_val = main(log, request_args)
        logging.debug(msg=ret_val)
        response = flask_app.response_class(
            response=json.dumps(ret_val),
            status=200,
            mimetype='application/json')
        logging.info(response)
        ret_val = None
        return response
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return Response("Error during execution! Reason: " + str(e), status=check_get_code(e))
        

if __name__ == "__main__":
    host = '0.0.0.0'
    logging.info("starting flask app with host: {} ... ".format(host))
    cors = CORS(flask_app, resources={r"/*": {"origins": "*"}})
    logging.info("created CORS object ... ")
    flask_app.run()
    
