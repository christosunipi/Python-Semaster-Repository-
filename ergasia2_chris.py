
import random
from turtle import clear, position

total = 0 
end_of_game = False 

list_array1 = [ ' ' , ' ' , ' ' ]
list_array2 = [ ' ' , ' ' , ' ' ]
list_array3 = [ ' ' , ' ' , ' ' ]

size = [ 'small' , 'medium' , 'large' ]
position_choice = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

small = 9
medium = 9 
large = 9 

avaliable_size = True 
choice_confirmed = False
while end_of_game==False and avaliable_size== True :
   #selection of cup size 
   while choice_confirmed == False and avaliable_size == True :
  
     size_choice = random.choice ( size )

    #checking wich cup was selected
     if size_choice == 'small' and small > 0 :
      choice_confirmed = True 
      small = small - 1 


     if  size_choice == 'medium' and medium > 0 :
       choice_confirmed = True 
       medium = medium - 1 

     
     if  size_choice == 'large' and large > 0 :
       choice_confirmed = True 
       large = large - 1 

    #checking if there is no cups left - end of game 
     if choice_confirmed == False and small == 0 and medium== 0 and large==0 :
       avaliable_size = False



   position = 0
   #checking if the game will continue - positioning the cup 
   if avaliable_size == True :

    position = random.choice ( position_choice )
   
      #positioning the selected cup in the list   
    if position <= 3 :
         # checking if the box can fit a larger cup or its full 
          if list_array1[position - 1] == ' ':
             list_array1[position - 1] = size_choice 
             total = total + 1

          elif size_choice == 'small' :
             if size_choice == 'medium' or size_choice == 'large' :
               list_array1[position - 1] = size_choice
               total = total + 1
             else :
                 # return of cup because the spot is already filled 
                  small = small + 1 

          elif size_choice == 'medium' :
             if list_array1[position - 1] == 'large' :
               list_array1[position - 1] = 'large'
               total = total + 1

             else : 
                 # return of cup because the spot has been filled with bigger size cup
                 medium = medium + 1
      
          elif size_choice == 'large' :
          # return of cup because the spot has been filled with the biggest cup 
             large = large + 1
          
    elif position <= 6 :
         # checking if the box can fit a larger cup or its full 
         if list_array2[position - 4] == ' ' :
            list_array2[position - 4] = size_choice 
            total = total + 1

         elif size_choice == 'small' :
            if size_choice == 'medium' or size_choice == 'large' :
                list_array2[position - 4] = size_choice
                total = total + 1
            else :
             # return of cup because the spot is already filled 
             small = small + 1 

         elif size_choice == 'medium' :
            if list_array2[position - 4] == 'large' :
                 list_array2[position - 4] = 'large'
                 total = total + 1

            else : 
                # return of cup because the spot has been filled with bigger size cup
                medium = medium + 1

         elif size_choice == 'large' :
           # return of cup because the spot has been filled with the biggest cup 
           large = large + 1
           

    else :
        # checking if the box can fit a larger cup or its full 
         if list_array3[position - 7] == ' ' :
            list_array3[position - 7] = size_choice 
            total = total + 1

         elif size_choice == 'small' :
            if size_choice == 'medium' or size_choice == 'large' :
                list_array3[position - 7] = size_choice
                total = total + 1
            else :
             # return of cup because the spot is already filled 
             small = small + 1 

         elif size_choice == 'medium' :
            if list_array3[position - 7] == 'large' :
                 list_array3[position - 7] = 'large'
                 total = total + 1
   
            else : 
                # return of cup because the spot has been filled with bigger size cup
                medium = medium + 1
      
         elif size_choice == 'large' :
              # return of cup because the spot has been filled with the biggest cup 
              large = large + 1

           
           
    if end_of_game == False :
      if list_array1[0] == list_array1[1] and list_array1[1] == list_array1[2] : # checking if the ganmes due if every cup is the same row 1 (same cups)
        end_of_game = True
      elif list_array2[0] == list_array2[1] and list_array2[1] == list_array2[2] : #  checking if the ganmes due if every cup is the same row 2 (same cups)
       end_of_game = True
      elif list_array3[0] == list_array3[1] and list_array3[1] == list_array3[2] : #  checking if the ganmes due if every cup is the same row 3 (same cups)
       end_of_game = True   
      elif list_array1[0] == 'small' and list_array1[1] == 'medium' and list_array1[2] == 'large' : # checking if the games due row 1 in order S, M, L 
       end_of_game = True
      elif list_array1[2] == 'small' and list_array1[1] == 'medium' and list_array1[0] == 'large' : # checking if the games due row 1 in order L, M, S 
       end_of_game = True
      elif list_array2[0] == 'small' and list_array2[1] == 'medium' and list_array2[2] == 'large' : # checking if the games due row 2 in order S, M, L 
       end_of_game = True
      elif list_array2[2] == 'small' and list_array2[1] == 'medium' and list_array2[0] == 'large' : # checking if the games due row 2 in order L, M, S 
       end_of_game = True
      elif list_array3[0] == 'small' and list_array3[1] == 'medium' and list_array3[2] == 'large' : # checking if the games due row 3 in order S, M, L 
       end_of_game = True
      elif list_array3[2] == 'small' and list_array3[1] == 'medium' and list_array3[0] == 'large' : # checking if the games due row 3 in order L, M, S 
       end_of_game = True


 #ckeking if the game is due - checking collums 
   if end_of_game == False :    
      if list_array1[0] == list_array2[0] and list_array2[0] == list_array3[0] : #checking if the games due if every cup is the same collum 1 (same cups)
         end_of_game = True 
      elif list_array1[1] == list_array2[1] and list_array2[1] == list_array3[1] : #checking if the games due if every cup is the same collum 2 (same cups)
         end_of_game = True 
      elif list_array1[2] == list_array2[2] and list_array2[2] == list_array3[2] : #checking if the games due if every cup is the same collum 3 (same cups)
         end_of_game = True 
      elif list_array1[0] == 'small' and list_array2[0] == 'medium' and list_array3[0] == 'large' : #checking if games due collum 1 in order S, M , L
         end_of_game = True  
      elif list_array1[0] == 'small' and list_array2[0] == 'medium' and list_array3[0] == 'large' : #checking if games due collum 1 in order L, M , S
         end_of_game = True  
      elif list_array1[1] == 'small' and list_array2[1] == 'medium' and list_array3[1] == 'large' : #checking if games due collum 2 in order S, M , L
         end_of_game = True  
      elif list_array1[1] == 'small' and list_array2[1] == 'medium' and list_array3[1] == 'large' : #checking if games due collum 2 in order L, M , S
         end_of_game = True  
      elif list_array1[2] == 'small' and list_array2[2] == 'medium' and list_array3[2] == 'large' : #checking if games due collum 3 in order S, M , L
         end_of_game = True  
      elif list_array1[2] == 'small' and list_array2[2] == 'medium' and list_array3[2] == 'large' : #checking if games due collum 3 in order L, M , S
        end_of_game = True  


   # checking if the game is due - checking x cups 
   if end_of_game == False :
      if list_array1[0] == list_array2[1] and list_array2[1] == list_array3[2] : #checking if the games due if every cup is the same first x (same cups)
         end_of_game = True
      elif list_array1[2] == list_array2[1] and list_array2[1] == list_array3[0] : #checking if the games due if every cup is the same second x (same cups)
         end_of_game = True    
      elif list_array1[0] == 'small' and list_array2[1] == 'medium' and  list_array3[2] == 'large' : #checking if the games due first x in orfer S, M , L 
         end_of_game = True
      elif list_array1[0] == 'large' and list_array2[1] == 'medium' and  list_array3[2] == 'small' : #checking if the games due first x in orfer L, M , S 
         end_of_game = True
      elif list_array1[2] == 'small' and list_array2[1] == 'medium' and  list_array3[0] == 'large' : #ckeking ig the games due second x in order S, M, L 
         end_of_game = True
      elif list_array1[2] == 'large' and list_array2[1] == 'medium' and  list_array3[0] == 'small' : #ckeking ig the games due second x in order L, M, S 
         end_of_game = True    
else:
   end_of_game = True


print( list_array1, list_array2, list_array3,size_choice)
print(small, medium, large, position)
# i consider as fact that if there is no avaliable cup the code of finding a random cup will be run again and it wont be cosidered as move to be added to total
# i consider as fact that if at first try a cup cannot be put on the randomly assigned spot the hole code will be run again and it wont be cosidered as
