""" Testing log files """
import os


def test_request_log_exists():
    """Checking request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../app/logs/request.log')
    assert os.path.exists(requestlog) == True


def test_errors_log_exists():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(errorlog) == True