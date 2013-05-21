# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Vincent Garonne, <vincent.garonne@cern.ch>, 2013

from nose.tools import assert_equal

from rucio.core import account_counter, rse_counter
from rucio.core.rse import get_rse


class TestCoreRSECounter():

    def test_inc_dec_get_counter(self):
        """ RSE COUNTER (CORE): Increase, decrease and get counter """
        rse_id = get_rse('MOCK').id
        rse_counter.del_counter(rse_id=rse_id)
        rse_counter.add_counter(rse_id=rse_id)
        cnt = rse_counter.get_counter(rse_id=rse_id)
        del cnt['updated_at']
        assert_equal(cnt, {'files': 0, 'bytes': 0})

        count, sum = 0, 0
        for i in xrange(10):
            rse_counter.increase(rse_id=rse_id, delta=1, bytes=2.147e+9)
            count += 1
            sum += 2.147e+9

        for i in xrange(4):
            rse_counter.decrease(rse_id=rse_id, delta=1, bytes=2.147e+9)
            count -= 1
            sum -= 2.147e+9

        cnt = rse_counter.get_counter(rse_id=rse_id)
        del cnt['updated_at']
        assert_equal(cnt, {'files': count, 'bytes': sum})


class TestCoreAccountCounter():

    def test_inc_dec_get_counter(self):
        """ACCOUNT COUNTER (CORE): Increase, decrease and get counter """
        rse_id = get_rse('MOCK').id
        account = 'jdoe'
        account_counter.del_counter(rse_id=rse_id, account=account)
        account_counter.add_counter(rse_id=rse_id, account=account)
        cnt = account_counter.get_counter(rse_id=rse_id, account=account)
        del cnt['updated_at']
        assert_equal(cnt, {'files': 0, 'bytes': 0})

        count, sum = 0, 0
        for i in xrange(10):
            account_counter.increase(rse_id=rse_id, account=account, delta=1, bytes=2.147e+9)
            count += 1
            sum += 2.147e+9

        for i in xrange(4):
            account_counter.decrease(rse_id=rse_id, account=account, delta=1, bytes=2.147e+9)
            count -= 1
            sum -= 2.147e+9

        cnt = account_counter.get_counter(rse_id=rse_id, account=account)
        del cnt['updated_at']
        assert_equal(cnt, {'files': count, 'bytes': sum})
