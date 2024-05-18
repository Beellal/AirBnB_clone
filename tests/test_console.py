#!/usr/bin/python3

import unittest
import console
from console import HBNBCommand

class test_console(unittest.TestCase):
    """Test console class"""
    def create(self):
        """Create a new instance of HBNBCommand"""
        return HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))