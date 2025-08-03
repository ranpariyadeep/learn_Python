
#Expression Execution

A,B =2,3
Txt ="@"

# String and Number ne '*' multiply kari sakay 
# like 2 * "@" = @@ , 3 * "@" = @@@
print(A * Txt)  # Output: @@
print(B * Txt)  # Output: @@@
print(A * Txt* B)  # Output: @@@@@@


# be k vadhu String ne '+' thi jodi sakay 
# like "Hello" + "World" = "HelloWorld"

F,G = "2",3
Text = "@"
# ((F +Text)*G) = "2@2@2@"
print((F + Text) * G)  # Output: 2@2@2@

# Integer + Float  = Float
# Integer / Integer = Float
# Integer * Float = Float
# Integer - Float = Float
# Float + Float = Float
# Float / Float = Float
# Float * Float = Float
# Float - Float = Float
# Integer + Integer = Integer

# Integer // Float = Float But Integer
#example 1.5/3 = 0.5

print(1.5//3) # Output: 0.0
print(3/1.3)  # Output: 2.3076923076923075
print(3//1.3) # Output: 2.0
print(1.5/3)  # Output: 0.5

print(3.0//1.3)  # Output: 2.0
print(3.0/1.3)   # Output: 2.307692

print(-3.0//1.3) # Output: -3.0


