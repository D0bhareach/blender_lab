import pytest
import os

from datetime import datetime
def format_datetime(ts):
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def map_test(test):
    start = test['metadata']['start']
    stop = test['metadata']['stop']

    return dict({
        "name": test['nodeid'],
        "outcome": test['outcome'],
        "start": start,
        "stop": stop,
        "duration": stop - start,
        "cpu": test['metadata']['cpu'],
        "ram": test['metadata']["ram"],
    })

@pytest.hookimpl(optionalhook=True)
def pytest_json_modifyreport(json_report):
    json_report['created'] = format_datetime(json_report['created'])
    del json_report['root']
    del json_report['collectors']
    del json_report['environment']['Plugins']
    del json_report['environment']['Packages']
    json_report['tests'] = list(map(map_test, json_report['tests']))
    # Add a key to the report
    # Delete the summary from the report
    del json_report['summary']

def pytest_json_runtest_metadata(item, call):
    total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
    ram = round((used_memory/total_memory) * 100, 2)
    if call.when != 'call':
        return {}
    return {
        'start': call.start,
        'stop': call.stop,
        'cpu': os.times()[0],
        'ram': ram
        }

