# Initialize variables to hold maximum and minimum values
current_maximum = typemin(Int32)  # Start with the smallest possible value
current_minimum = typemax(Int32)  # Start with the largest possible value

my_list = [5, 15, 50, 3, 67, 100]

# Loop through each element in my_list
for i in my_list
    if current_minimum > i
        current_minimum = i
    end
    
    if current_maximum < i
        current_maximum = i
    end
end

println("Maximum: $current_maximum, Minimum: $current_minimum")
