# Normalization script to replace from list in a input file
## How to run?

```bash
python3 word_ambguity-normalizer.py input.txt list.txt 
```

# Normalization script to replace from transcription text in a input file for making it mt ready
## How to run?

```bash
python3 mt-ready-normalizer.py ET-l-01-transcription-rich-text-MTReady.txt mtready-variation.txt
```
Here mtready-variation.txt has fixed lines like

# Anywhere in the text
nineteen twenty four	1924
nineteen forty five	1945
nineteen sixty two	1962
nineteen eighty six	1986
nineteen sixty eight	1968
nineteen seventy three	1973
nineteen fifty nine	1959

# Every begining line only
Number one,	1)
Number two,	2)
Number three,	3)
Number four,	4)
Number five,	5)
Number six,	6)
Number seven,	7)
Number eight,	8)
Number nine,	9)
Number ten,	10)
Number eleven,	11)

# Anywhere in the text
et-one	ET-I
et-two	ET-II
et-three	ET-III

Based on the comment lines regex will be formed. So dont change comment line format.
