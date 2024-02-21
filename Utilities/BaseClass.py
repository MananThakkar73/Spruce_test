import pytest
import logging
import openpyxl

@pytest.mark.usefixtures("startup")
class Baseclass:
    print("this is baseclass")