==============================================================
                       easy_load.py
==============================================================

easy_load is a module for python 3.X that allows for easy load
bars to be printed to the terminal/cmd when using a loop.

ex:
(counter)        (bar)              (percent)  
33/100 | [======--------------] | 33% Loaded . . . 

How To Use:

Use the method: 
	load = easy_load.progress_bar(total_num_of_increments, length=25,
				 icon='=', counter=True, bar=True,
				 percent=True)
-total_num...: Your total number of documents/files needed to be 
	iterated through. 
-length: Length of the progress bar in string elements (for aesthetic 
	purposes).
-icon: Change the 'full' icon. Default is '¦'.
-counter: Displays the total counter, if True.
-bar: Displays the progress bar, if True.
-percent: Displays the percent Loaded, if True.

Update the Bar with:
	load.update(update=1)

-self.upadte() defualts with an increment of 1 per call, but can be
	changed.

Paint the bar with:
	load.paint_bar()
