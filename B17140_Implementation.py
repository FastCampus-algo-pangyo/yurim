from collections import Counter

def r_operation(input_list):
    output_list = []
  
    for row in input_list:
        element_count = Counter(row)
        sorted_items = sorted(element_count.items(), key=lambda x: (x[1], x[0]))
        row_result = []  
        for number, count in sorted_items:
            if number != 0:
                row_result.append(number)
                row_result.append(count)
        
        output_list.append(row_result) 

    max_length = max(len(row) for row in output_list) 
    
    for row in output_list:
        while len(row) < max_length:
            row.append(0)
          
    return output_list

def c_operation(input_list):
    transposed_list = []
  
    for j in range(len(input_list[0])):
        column_data = [row[j] for row in input_list]
        transposed_list.append(column_data)

    transposed_list = r_operation(transposed_list)

    output_list = []
  
    for i in range(len(transposed_list[0])):
        row_result = [transposed_list[j][i] for j in range(len(transposed_list))]
        output_list.append(row_result)
    
    return output_list


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

time = 0

while True:
  if r-1 < len(A) and c-1 < len(A[0]) and A[r-1][c-1] == k: 
      break
      
  if time > 100: 
    time = -1
    break
    
  if len(A) >= len(A[0]):
      A = r_operation(A)
  else:
      A = c_operation(A)
    
  time += 1
  
print(time)