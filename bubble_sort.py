def bubble_sort(unsorted_list):
    # um for para percorer a mesma quantidade do array
    for i in range(len(unsorted_list)):
        # -1 para equilibrar com o +1 usado logo abaixo, por estar usando +1 poderia acabar referenciando im index quye não existe
        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j+1]:

                # muda os dois de posições, tem que ser ao mesmo tempo
                unsorted_list[j], unsorted_list[j +
                                                1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list
