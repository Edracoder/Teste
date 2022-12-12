# Final training of list code using. ([],insert,append,pop,remove)

guest_list=['carol','joao','fernando']
print(guest_list)

print('\n\t' + guest_list[0].title()+', you are invited for my dinner.')
print('\n\t' + guest_list[1].title()+', you are invited for my dinner.')
print('\n\t' + guest_list[2].title()+', you are invited for my dinner.')


print('\n\n' + guest_list[0].title() + ', will not come to the dinner'.upper())

guest_list[0]=('tays')

print('\n')

print('\n\t' + guest_list[0].title()+', you are invited for my dinner.')
print('\n\t' + guest_list[1].title()+', you are invited for my dinner.')
print('\n\t' + guest_list[2].title()+', you are invited for my dinner.')

guest_list.insert(3,'arcanja')
guest_list.insert(4,'pedro')
guest_list.append('carlos')



print('\n\n' + guest_list[3].title() + ', ' + guest_list[4].title() + ' and ' + guest_list[5].title() + 
', we found a new table and you are invited for my dinner.'.upper())

print('\n\n\nThe new table will not come at time. I will have only two vacancy.'.upper())

print('\n\n\n\tDear ' + guest_list[1].title()+", sorry the inconvenient, you vacancy does'nt will come at time.")
print('\n\tDear ' + guest_list[2].title()+", sorry the inconvenient, you vacancy does'nt will come at time.")
print('\n\tDear ' + guest_list[4].title()+", sorry the inconvenient, you vacancy does'nt will come at time.")
print('\n\tDear ' + guest_list[5].title()+", sorry the inconvenient, you vacancy does'nt will come at time.")

guest_1=guest_list.pop(1)
guest_2=guest_list.pop(1)
guest_3=guest_list.pop(2)
guest_4=guest_list.pop(2)

print('\n\n\n\n\t' + guest_list[0].title() + ', you still invited for the dinner.')

print('\n\t' + guest_list[1].title() + ', you still invited for the dinner.')

guest_list.remove(guest_list[0])
guest_list.remove(guest_list[0])

print(guest_list)




