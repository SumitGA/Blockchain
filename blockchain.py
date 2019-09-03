#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:02:50 2019

@author: sumitgautam
"""
# Module 1 - create a Blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part ! Building a Blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
# Part2 - Mining a Blockchain

