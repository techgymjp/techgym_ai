text = "I have a pen, you have a pen, she has a pen."

# comma(,)とperiod(.)の前にスペースを入れる
def process_text(text):
  comma_split = text.split(",")
  comma_text  = "" 
  for i in range(0, len(comma_split) - 1):
    comma_text += comma_split[i] + " ,"
  if (len(comma_split) - 1) > 1:
    comma_text = comma_text + comma_split[len(comma_split) - 1]
  tmp_text   = comma_text
  period_split = tmp_text.split(".")
  period_text  = ""
  for i in range(0, len(period_split) - 1):
    period_text += period_split[i] + " ."
  if (len(period_split) - 1) > 1:
    period_text = period_text + period_split[len(period_split) - 1]

  return period_text

print(text)
print(process_text(text))
