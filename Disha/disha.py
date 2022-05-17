def dprint(text): 
    if "hate" in text:
      a=text.replace("hate","love")
      return print(a)
    else: 
      return print(text)
