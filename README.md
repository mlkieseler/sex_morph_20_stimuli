# sex_morph_20_stimuli Analysis code

Currently, this code has three contributing parts: NewGenderFunctions, NewGenderMorph, and a jupyter notebook to fit a sigmoid curve to the subject's data. 

NewGenderFunctions houses all the functions we need to analyze the data. To analyze the data, run NewGenderMorph. This will, among several different graphs, output a csv-file for each subject with that subject's data. These csv-files are what will be fed into the jupyter notebook. The notebook will produce more graphs and one csv-file per continuum with each subject's point of subjective equality and the slope at the point of subjective equality.
