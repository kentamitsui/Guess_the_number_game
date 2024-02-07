import sys,random

def get_integer_input(prompt):
  # プロンプトがtrueである限り、ターミナルに出力を行う
    while True:
        sys.stdout.write(prompt + "\n")
        sys.stdout.flush()
# 標準ストリーム
        try:
            return int(sys.stdin.readline().strip())
        except ValueError:
            sys.stdout.write("数値を入力して下さい。\n")
            sys.stdout.flush()
# 最小値と最大値のプロンプトを設定
minNum = get_integer_input("最小値を入力して下さい：")
maxNum = get_integer_input("最大値を入力して下さい：")

while minNum > maxNum:
    sys.stdout.write("最小値は最大値以下で入力して下さい。")
    sys.stdout.flush()

    minNum = get_integer_input("最小値を入力して下さい：")
    maxNum = get_integer_input("最大値を入力して下さい：")
# 最小値と最大値の間で、ランダムな数値を出力する
randomNum = random.randint(minNum, maxNum)

sys.stdout.write("数値を入力して下さい。\n")
sys.stdout.flush()

guessNum = None

while guessNum != randomNum:
    guess = get_integer_input("ランダム生成された数値と、同じだと思う数値を入力して下さい：")
    if guess > randomNum:
        sys.stdout.write("入力された数値は「大きい」です。もう一度入力して下さい。\n")
        sys.stdout.flush()
    elif guess < randomNum:
        sys.stdout.write("入力された数値は「小さい」です。もう一度入力して下さい。\n")
        sys.stdout.flush()
    else:
        sys.stdout.write("入力された数値とランダム生成された数値が一致しました。\n")
        sys.stdout.flush()
        break