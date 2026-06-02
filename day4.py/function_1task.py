def average(*marks):
    if len(marks)==0:
        return "no marks provided"
    total=sum(marks)
    avg=total/len(marks)
    return avg
print(average(80,90,70))
print(average(50,60))
print(average())



    