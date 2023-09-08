my_list = [1, 2, 3]

for i in 1:div(length(my_list), 2)
    j = length(my_list) - 1 - i

    my_list[i], my_list[j] = my_list[j], my_list[i]
end

println(my_list)