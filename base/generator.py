#!/usr/bin/python

from moduleframework import CommonFunctions

class TestGenerator(CommonFunctions):
    def __init__(self):
        self.loadconfig()
        self.output=""
        self.templateClassBefore()
        for testname  in self.config['test']:
            self.templateTest(testname, self.config['test'][testname])

    def templateClassBefore(self):
        self.output = """#!/usr/bin/python

import socket
from avocado import main
import moduleframework

if __name__ == '__main__':
    main()

class GeneratedTestsConfig(moduleframework.AvocadoTest):
    \"\"\"
    :avocado: enable
    \"\"\"
"""

    def templateTest(self, testname, testlines):
        self.output=self.output+"""
    def test_%s(self):
        self.start()
""" % testname
        for line in testlines:
            self.output = self.output + """        self.run("%s")\n""" % line

config = TestGenerator()
configout = open('generated.py', 'w')
configout.write(config.output)
configout.close()