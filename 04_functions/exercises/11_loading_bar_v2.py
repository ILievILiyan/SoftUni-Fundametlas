def loading_bar(progress):
    divided = progress // 10
    dots = 10 - divided
    if divided == 10:
        print(f"{progress}% Complete!\n[{'%' * divided}]")
    else:
        print(f"{progress}% [{'%' * divided}{'.' * dots}]\nStill loading...")


number = int(input())
loading_bar(number)