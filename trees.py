trees = ['dogwood', 'apple', 'cedar']
trees.extend(['cyprus', 'oak'])

def isPalindrome(self, x: int) -> bool:
  num_string = str(x)
  rev_num_string = num_string[::-1]
  if num_string == rev_num_string:
      return True
  else: 
      return False

  # Making changes for new branch 'trees-again'.