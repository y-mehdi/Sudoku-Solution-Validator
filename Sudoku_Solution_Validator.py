def valid_solution(board):
#########################################################
    def zero_check(board):  # WICHTIG für den Test 1Grad
        nn = counter_1 = 0  # this fonction checks if 0 exist in 2D list
        while nn < 9:  # horizontal
            while counter_1 < 9:
                if board[nn][counter_1] == 0:
                    return False
                else:
                    return True
            counter_1 += 1
        nn += 1

#########################################################
    # this fonction cheks if summation values ==45
    def check(k):  # WICHTIG für den Test
        if k != 45:
            return False
        elif k == 45:
            return True

#########################################################
    def removing_duplicated(board):
        while n < 9:  # to test if there is any duplicated number
            result = [i for a, i in enumerate(board[n]) if i not in board[:a]]
            n += 1
            if len(board[n]) != 9:
                return False
            elif len(board[n]) == 9:
                return True
                pass

#########################################################
    def sum_vertical_array(count1, count2):  # secondaire
        d = 0  # this function add verticale values of the 2d array
        while count1 < 9:
            d += board[count1][count2]
            count1 += 1
        return d
        pass

#########################################################
    n = 0
    while n < 9:  # horizontal
        ka = sum(board[n])
        return check(ka)  # WICHTIG für den Test 1Grad
        n += 1

    count1 = count2 = 0
    while count1 < 9:  # vertical
        while count2 < 9:
            ko = sum_vertical_array(count1, count2)  # here i used the 3rd fonction

            count2 += 1
            return check(ko)  # WICHTIG für den Test 1Grad
        count1 += 1
#########################################################

    if check(ko) & check(ka) & zero_check(board) & removing_duplicated(board) == True:
        return True
    else:
        return False
    pass