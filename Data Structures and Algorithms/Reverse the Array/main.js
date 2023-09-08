let my_list = [1, 2, 3];

for (let i = 0; i < Math.floor(my_list.length / 2); i++) {
    let j = my_list.length - 1 - i;

    [my_list[i], my_list[j]] = [my_list[j], my_list[i]];
}

console.log(my_list);  
