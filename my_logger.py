#!/usr/local/python


import logging
import inspect
from inspect import stack, getframeinfo


def my_logger():
    call_from = getframeinfo( stack()[1][0] )
    extra = {'lineno': call_from.lineno, 'fn_name': call_from.function}
    logger = logging.getLogger( call_from.filename.split( '/' )[-1].replace( '.py', '' ) )
    logging.basicConfig( format='%(asctime)-15s  %(name)s %(lineno)s %(levelname)s  %(message)s' )
    logger.setLevel(logging.DEBUG)
    return logger
