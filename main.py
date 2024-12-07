# \n -> перенос на новую строчку
# \t -> табуляция
# \  -> Зеркалирование

print ("hello world1")
print ("hello\nworld2!")
print ("hello\n\tworld3")
print ("hello\"world4\"")
print ("hello\\n\\t\"world5\"")

####

print ("hello")
print ("world")

# end= -> добавялет написанное в " " между 2 принтами
print ("hello", end=" - ")
print ("world")

# sep= -> установить\убрать пробелы в принте

print ("hello", "one", "two", "three", sep=",")

