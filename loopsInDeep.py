# for i in range(1,11):
#     print(i)
# for i in range(10,0,-1):
#     print(i)


# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

#i=10; i>=1 T; print(i) = 10; i=10-1; i=9
#i=9; i>=1 T; print(i) = 9; i=8;
#i=7; i>=1 T; print(i) = 8; i=7;
#.......
#i=1; i>=1 T; print(i) = 1; i=0;
#i=0; i>=1 F

# i=1
# while (i<=50):
#       if(i%2!=0):
#            print(i)
#       i += 1 

#i=1 (i<=50) T, i%2=1; i=2
#i=2 (2<=50) T, i%2=0;print(2); i=3
#.....
#i=50 (50<=50)T; i%2=
# print(50%3==0)
# print(2**3)

# n=7
# i=1
# while(i<=100):
#     if(i%n==0):
#         print(i)
#     i += 1

#sum of first 10 number
# sum=0
# i=1
# while(i<=10):
#     sum += i
#     i += 1
# print(sum)
#sum=0; i=1; i<=10 T; sum=1 i=2;
#sum=1; i=2; i<=10; sum=3 i=3;
#sume=3; i=3; i<=10; sum=6 i=4;
#sum=6; i=4; i<=10; sum 10
#..
#sum=55

# n=5
#5*4*3*2*1=120 
# num = 5
# fact = 1

# while num > 0:
#     fact *= num
#     num -= 1

# print(fact)

#num=5 fact=1 while(num > 0); fact=5; num=4
#num=4 fact=5 num>0 T; fact=20; num=3
#num=3 fact=20 num>0 T; fact=60; num=2
#num=2 fact=60 num>0 T; fact=120; num=1
#num=1 fact=120 num>0 T; fact=120; num=0
#num=0 fact=120 num>0 F;

#????*
#???***
#??*****
#?*******
#*********

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print("?", end="")
#     for k in range(0,n-i+1):
#         print("*", end="")
#     for p in range(0,n-i):         
#         print("*", end="")
#     print("")


# i=5; 5>0 T;
# j=1; j<5 T; j=2; j<5 T; j=3, 3<5 T;j=4 4<5 ; j=5 5<5 F
# k=0 0<5-5+1=1 T;k=1 1<1 F
# p=0 0<0 F

# i=4; 4>0 T;
# j=1 1<4 T; j=2 2<4 T; j=3 3<4 T; j=4 4<4 F
# k=0 0<2 T; k=1 1<2 T; k=2 2<2
# p=0 0<1 T; p=1 1<1 F









#pattern
#????*
#???***



# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if (i==0 or i==n-1 or j==0 or j==n-1):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print("")



# print(int(float("2.5")))
#zero and empty value are falsy value
# print(bool(0))
# print(bool(-1))
# print(bool(1))
# print(bool([ ]))
# print(bool(""))
# print(bool(" "))