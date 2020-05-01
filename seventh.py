#table program
#a*b=c


table=int(input('enter the value of table: '))
for i in range(1, 11):
    answer=table*i
    print(table, '*', i, '=', answer)
