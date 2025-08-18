## Необходимо посчитать количество повторений каждого слова


text = ("Mr. and Mrs. Smith have one son and one daughter. The son's name is John. "
        "The daughter's name is Sarah. The Smiths live in a house. They have a living room. "
        "They watch TV in the living room. The father cooks food in the kitchen. They eat in the dining room. "
        "The house has two bedrooms. They sleep in the bedrooms. They keep their clothes in the closet. "
        "There is one bathroom. They brush their teeth in the bathroom.The house has a garden. "
        "John and Sarah play in the garden. They have a dog. John and Sarah like to play with the dog.")

lowerCase_text = text.lower()
list_text = lowerCase_text.split()


for i in range(len(list_text)):
  word = (list_text[i]).strip('.')    # метод .strip('.')  использовала для удалении точки в конце слов
  count_word = 0

  for j in range(len(list_text)):
      if (list_text[j]).strip('.') == word:
         count_word += 1

  print(f'{word} = {count_word}')











