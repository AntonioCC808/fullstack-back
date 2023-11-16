"""
Test cases for the calculadora module.

This module contains unit tests for the functions in the calculadora module.
"""

import time

from microactividad_pylint.calculadora import sumar, restar


def test_sumar():
    """Test suma"""
    time.sleep(1)
    a = 2
    b = 2
    c = sumar(a, b)
    assert c == 4


def test_restar():
    """Test resta"""
    time.sleep(1)
    a = 2
    b = 2
    c = restar(a, b)
    assert c == 0
