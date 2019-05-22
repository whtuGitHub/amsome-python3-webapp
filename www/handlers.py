#/!urs/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'whtuDT'

' url handlers '

from models import User
from coroweb import get
import asyncio

@get('/')
async def index(request):
    users = await User.findAll()
    return {
            '__template__': 'test.html',
            'users': users
    }
