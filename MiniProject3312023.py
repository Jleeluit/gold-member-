# We will create an AWS services list using python

# Start by creating an empty list
services_list = []

# Add items/services to the list using "+=". 
services_list += ["EC2", "Lambda", "CloudWatch"]
#print to see formed list
print(services_list)

# add another service to the list by "inserting" it to first position.
services_list.insert(0,"ECS")
#check to see if it was added
print(services_list)

# print length of the list
print(len(services_list))

# remove a service
services_list.remove("Lambda")

# remove another service from the list
services_list.remove("EC2")

# print the new list and the new length of the list
print(services_list)
print(len(services_list))
