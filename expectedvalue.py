# calculate the expected value of rolling two dice
# If our first die is fair and our second die is loaded so that the probability that it comes up 5 is 3/8 and the probability that it comes up any other number is 1/8
# what is the probability associated with each x in X?

X = [0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.02083333, 0.0625, 0.02083333]

x= [1+1,1+2,1+3,1+4,1+5,1+6,2+1,2+2,2+3,2+4,2+5,2+6,3+1,3+2,3+3,3+4,3+5,3+6,4+1,4+2,4+3,4+4,4+5,4+6,5+1,5+2,5+3,5+4,5+5,5+6,6+1,6+2,6+3,6+4,6+5,6+6]

Ex = 0.0

for i, n in zip(X,x):
    Ex += i*n

print "The E(X) = "+str(Ex)