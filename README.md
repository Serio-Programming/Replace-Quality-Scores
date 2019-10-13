# Replace-Quality-Scores
# A Program by Tyler Serio

# What is it?
Replace Quality Scores

# What does it do?
This program replaces the quality scores of Thymine bases in specific positions on reads in FASTQ files.

# How does it do it?
This program reads through all the lines of a FASTQ file, and when it encounters a Thymine base in the first, second, next to last, or last position of a read, it changes the corresponding quality score to a "#" which is a relatively low quality score.

# Why was it written?
This program was written to address an issue that arose while doing quality control on ancient DNA data. For ancient DNA, Thymine bases in specific positions can have overestimated quality scores, and this program reduces those quality scores to compensate. 
