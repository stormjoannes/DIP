type data\Dutch_text.txt | python algorithm\mapper.py | python algorithm\reducer.py
echo Dutch | python algorithm\right_filename.py

type data\English_text.txt | python algorithm\mapper.py | python algorithm\reducer.py
echo English | python algorithm\right_filename.py

python algorithm\Language_guesser.py