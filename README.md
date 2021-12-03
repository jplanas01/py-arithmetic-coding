Basic implementation of an arithmetic coder.
Done so I could wrap my head around how having a good model results in good compression.


Spoiler: It's because by having a good model that predicts well future inputs, less numbers have to be appended to the code since the fraction doesn't move out of the expected window. Less information has to be stored in the fraction because the model doesn't need to much to know what's coming, leads to compression.
