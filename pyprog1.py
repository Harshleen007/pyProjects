#count how often each char appear in text
message = 'life is like riding a bicycle. To keep your balance, you must keep moving'
count = {}
for character in message:
  count.setdefault(character, 0)
  count[character] = count[character] + 1
print(count)
