type data\Dutch_text.txt | python mapper.py | python reducer.py
echo Dutch | python right_filename.py

type data\English_text.txt | python mapper.py | python reducer.py
echo English | python right_filename.py

python Language_guesser.py