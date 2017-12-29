
import pytest
import bot
import os
import telegram

b = telegram.Bot(str(os.environ["TGKEY"]))
u = telegram.Update(1243)

def test_test():  # tests tests
    assert(2+2 == 4)  # hmm

