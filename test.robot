# example.robot
*** Settings ***
Library    Process

*** Test Cases ***
Running of python script
    Start Process   python    server.py
    Start Process   python    client.py
