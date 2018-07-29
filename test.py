def testleapyear(year):
    val = year/4
    val_2_str = str(val)
    print(val_2_str)
    print val_2_str.isdigit()
    return val_2_str.isdigit()


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    daysOfMonths_nonleap = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths_leap = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    mark = testleapyear(year1)

    if mark is False:
        return print('common year')
    else:
        return print('leap year')


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    result = testleapyear(2012)
    # result = testleapyear(2011)
    # for (args, answer) in test_cases:
    #     result = daysBetweenDates(*args)
        # if result != answer:
        #     print "Test with data:", args, "failed"
        # else:
        #     print "Test case passed!"
    return result

test()
