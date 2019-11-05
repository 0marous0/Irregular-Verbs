import random
import dllWord

def sample(wordR,wordE1,wordE2,wordE3):#проверка ответа пользователя
	if wordR == wordE1 or wordR == wordE3 or wordR == wordE3:
		return True
	else:
		return False

def dellWord(Dword):#функция удаления слов
	dllWord.words.pop(Dword)
	dllWord.words.pop(Dword)
	dllWord.words.pop(Dword)
	dllWord.words.pop(Dword)

		
def question(x,y):
	for i in range(0,x):
		attemp = y
		lenWords = len(dllWord.words)#количество слов в списке
		rnd = random.randrange(0,lenWords-1,4)#генератор русского слова
		print('переведите с русского на английский слово(а) "{}"\nиспользуя одну из трех форм неправильных глаголов\nу вас {} попыток'.format(dllWord.words[rnd],attemp))
		YWord = input("введите ваш вариант: ")#ввод вариантов пользователя
		attemp -=1
		rr = sample(YWord,dllWord.words[rnd+1],dllWord.words[rnd+2],dllWord.words[rnd+3])#проверка истинности ответа
		while True:
			if rr:
				print("поздравляю вы справились")
				print('слово "{}" в разных формах:\n1: {}\n2: {}\n3: {}'.format(dllWord.words[rnd],dllWord.words[rnd+1],dllWord.words[rnd+2],dllWord.words[rnd+3]))
				break
			else:
				if attemp > 0:
					print("у вас осталось {} попытки(ок)\nпопробуйте еще".format(attemp))
					YWord = input("введите ваш вариант: ")
					rr = sample(YWord,dllWord.words[rnd+1],dllWord.words[rnd+2],dllWord.words[rnd+3])
					attemp-=1
				else:
					print("к сожалению попытки закончились\nпожалуйста выучите эти слова:\nRU: {}\n1: {}\n2: {}\n3: {}".format(dllWord.words[rnd],dllWord.words[rnd+1],dllWord.words[rnd+2],dllWord.words[rnd+3]))
					break
		dellWord(rnd)
lenWords = len(dllWord.words)
while True:
	x = int(input("введите количество вопросов(не больше: {}): ".format(int(lenWords/4))))
	if x<115 and x>1:
		break
	else:
		print("введите число не больше: {}".format(int(lenWords/4)))

while True:
	y = int(input("введите количество попыток: "))
	if y>0:
		break
	
question(x,y)
input()