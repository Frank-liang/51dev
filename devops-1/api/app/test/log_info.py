#!/usr/bin/env python
#coding:utf-8

import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info('start reading database')
records = {'join': 55, 'tom': 66}
logger.debug('records: %s', records)
logger.info('Update record....')
logger.info('Finish udating records')
