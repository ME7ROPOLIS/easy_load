# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 20:28:17 2016

@author: Jake
"""
import sys

class Easy_load(object):
    
    def __init__(self, total_load, length=25, icon='█', counter=True, bar=True, percent=True):
        """
        Easy_load creates a loading bar object that can be updated and printed 
        to the CLI window. total_load is the amount of things being loaded, and
        current_load is the amount of things already loaded. The percentage is 
        calculated in paint_bar and printed along with the loading bar itself. 
        The loading bar is animated with the string passed to icon (default '='),
        and is the length of characters specified by the length keyword (not 
        including the edges of the bar, '[' and ']'). By default, the loading 
        bar should look like this:
        
        At 70% Done, length=20:
        [==============------] 70% Loaded . . .
        
        At 100% Done, length=20: 
        [====================] 100% Loaded . . .
        
        
        """
        
        # Assert that we are passed an int or float
        assert type(total_load) in (int, float), 'ERROR: Easy_load must take int or float.'
        
        self.total_load = total_load
        self.current_load = 0
        self.length = length
        self.icon = icon
        self.counter = counter
        self.bar = bar
        self.percent = percent
        
    def update(self, update=1):
        """
        Update allows the current_load attribute to be updated.
        """
        self.current_load = self.current_load + update
    
    def paint_bar(self):
        """
        Draws the loading bar.
        """
        start = ''
        bar = ''
        title = ''
        blocks = int(self.length*(float(self.current_load)/float(self.total_load)))
        
        if self.counter:
            start = '{0}/{1}|'.format(self.current_load, self.total_load)
        
        if self.bar:
            bar = '[%s]' % (self.icon * blocks + '-' * (self.length - blocks))
            
        if self.percent:    
            title = '|{}% Loaded . . .'.format(int(100*(float(self.current_load)/float(self.total_load))))        
        
        print(start + bar + title, end='\r')
        
