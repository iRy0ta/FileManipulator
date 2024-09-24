import sys
import os

def main():
    if(len(sys.argv) < 2):
        print("コマンドを入力してください。")
        return
    
    command = sys.argv[1]
    
    if(command == "reverse"): reverseContents()
    elif(command == "copy"): copyContents()
    elif(command == "duplicate-contents"): duplicateContents()
    elif(command == "replace-string"): replaceContents()
    else: print("指定されたコマンドは存在しません。")

def reverseContents():
    if(not(isValidArgument(4))): return

    inputPath, outputPath = sys.argv[2:]

    if(not(isExistInputPath(inputPath))): return

    contents = readContents(inputPath)

    contents = reverseSentence(contents)

    with open(outputPath, "w") as f:
        f.write(contents)

    print(f"{inputPath}の内容を反転し{outputPath}へ書き込みました。")

def reverseSentence(sentence):
    reverse = ""
    for char in sentence: reverse = char + reverse 

    return reverse

def copyContents():
    if(not(isValidArgument(4))): return

    inputPath, outputPath = sys.argv[2:]

    if(not(isExistInputPath(inputPath))): return

    contents = readContents(inputPath)

    with open(outputPath, "w") as f:
        f.write(contents)

    print(f"{inputPath}の内容を{outputPath}へ書き込みました。")

def duplicateContents():
    if(not(isValidArgument(4))): return
       
    inputPath = sys.argv[2]

    if(not(sys.argv[3].isdigit())):
        print("繰り返し回数は正の整数値で入力して下さい。")
        return
    
    repeatTimes = int(sys.argv[3])

    if(not(isExistInputPath(inputPath))): return

    contents = readContents(inputPath)

    with open(inputPath, "a") as f:
        for i in range(repeatTimes):
            f.write(contents)

    print(f"{inputPath}の内容を{str(repeatTimes)}回追加で書き込みました。")

def replaceContents():
    if(not(isValidArgument(5))): return

    inputPath, needle, newString = sys.argv[2:]

    if(not(isExistInputPath(inputPath))): return

    contents = readContents(inputPath)

    if(contents.find(needle) == -1):
        print(f"{inputPath}の内容には{needle}は含まれていません。")
        return
    
    contents = contents.replace(needle, newString)

    with open(inputPath, "w") as f:
        f.write(contents)

    print(f"{inputPath}の内容に含まれる{needle}を{newString}に置換しました。")

def readContents(path):
    with open(path) as f:
        contents = f.read()

    return contents

def isExistInputPath(path):
    if(os.path.isfile(path)):
        return True
    else:
        print("指定されたファイルは存在しません。")
        return False

def isValidArgument(num):
    if(len(sys.argv) < num):
        print("引数の数が不足しています。")
        return False
    elif(len(sys.argv) > num):
        print("引数の数が超過しています。")
        return False

    return True

main()