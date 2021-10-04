def rotationalCipher(input, rotation_factor):
  output = ""
  rf_num = rotation_factor % 10
  rf_char = rotation_factor % 26
  
  for char in input:
    if char.isnumeric():
      output = output + str( ( int(char) + rf_num ) % 10 )
    
    elif char.isalpha() and char.islower():
      num = ord(char)
      num += rf_char
      if num > 122:
        num -= 26
      output += chr(num)
      
    elif char.isalpha() and char.isupper():
      num = ord(char)
      num += rf_char
      if num > 90:
        num -= 26
      output += chr(num)
      
    else:
      output = output + char
  
  return output
