def square_filter(start, end):
    squares = []

    
    for num in range(start, end + 1):
        squares.append(num ** 2)

    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("All Squares:", squares)
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)

square_filter(1, 10)
