import os
import sys

from org.transcrypt import utils

sys.path.append ('{}/pyflakes'.format (os.path.dirname (os.path.abspath (__file__)) .replace ('\\', '/')))
import pyflakes.checker

def run(sourceFile, parseTree):
    messageHolders = sorted (
        pyflakes.checker.Checker (parseTree, sourceFile) .messages,
        key = lambda messageHolder: 10000 * messageHolder.lineno + messageHolder.col
    )

    utils.log(
        messageHolders or utils.commandArgs.verbose,
        f'Performing lightweight consistency check on module: {sourceFile}',
    )
    if messageHolders:
        for messageHolder in messageHolders:
            utils.log(
                True,
                f'\n\tLine {messageHolder.lineno - utils.nrOfExtraLines}: {messageHolder.message % messageHolder.message_args}',
            )
        utils.log (True, '\n\n')
    else:
        utils.log (utils.commandArgs.verbose, ' OK\n')
