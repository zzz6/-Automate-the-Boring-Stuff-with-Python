def spam():
	eggs = 'spam local'
	print(eggs) # вызываем строку spam local

def bacon():
	eggs = 'bacon local'
	print(eggs) # выводится строка bacon loca
	spam()
	print(eggs) # выводится строка bacon loca

	eggs = 'global'
	bacon()
	print(eggs) # выводится строка 'global'