
common_list = []

with open('./sample1.txt', 'r') as f1:
  for num1 in f1:
    with open('./sample2.txt', 'r') as f2:
      for num2 in f2:
        if num1 == num2:
          common_list.append(num1)

with open('./output.txt', 'w') as f:
  f.writelines(common_list)