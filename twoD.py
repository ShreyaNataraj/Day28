import numpy as np
twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(twoDarray)
#inserting into 2D
# ARRAY
newarray = np.insert(twoDarray,0,[[17,18,19,20]],axis =0)
print(newarray)
#while inserting make sure that it starts with old array which row/column index you want to insert followed by elements wih axis =0 when it is row and 1 when it is column
#Accesing an element in an array
def accesselement(array,rowindex,colindex):
  if rowindex>=len(array) or colindex>=len(array):
    print("incorect index")
  else:
    print(array[rowindex][colindex])
accesselement(twoDarray,3,3)      
#traversing two dimensional arrays
def traversearray(array):
  for i in range(len(array)):
    for j in range(len(array[0])):
      print(array[i][j])
traversearray(twoDarray)
#Searching 2D array
def search(array,value):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if(array[i][j]==value):
        print( "the value is found at the index" + str(i) +" " +str(j))
search(twoDarray,12)        

#Deleting an entire row or column
newarray = np.delete(twoDarray,0,axis=0)
#old array index axis =0 it's arow else its a column
print(newarray)