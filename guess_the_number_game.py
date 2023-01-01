import sys
import random

sys.stdout.buffer.write(b"Guess the number!!")
sys.stdout.flush()

def guess(ans):
	while(True):
		guess_num = int(input("Guess the number"))
		if guess_num == ans:
			print("Great!")
			break;
		else:print(f'{guess_num} is not the answer... Try again!!')
	print(f'The answer is {ans}')



while(True):
	min = int(input("Set the minimun number."))
	max = int(input("Set the maximum number."))
	if min < max and min > 0:
		ans = random.randint(min, max)
		guess(ans)
		break;
	elif min > 0:
		print("maximun number must be bigger than minimum number.")
	else:
		print("mininum number have to be bigger than zero.")


