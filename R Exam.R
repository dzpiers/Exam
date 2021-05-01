## Loading Libraries
library(matlib)

## Differentiation
## Enter function
f <- expression(exp(x)-5*x^3)

## Differentiate
f_1 <- D(f, 'x')
f_1

## Second derivative
f_2 <- D(f_1, 'x')
f_2

## Integration
## Enter function
g <- function(x) {1/sqrt(2*pi)*exp(-x^2/2)}

## Integrate
integrate(g, lower = -1.96, upper = 1.96)


## Matrix and vector operations
## Enter vector/matrix
v <- c(1,2,3)
A <- cbind(c(2,0,0), c(0,2,0), c(0,0,2))
B <- matrix(c(13, -4, 2, -4, 11, -2, 2, -2, 8), 3, 3, byrow=TRUE)

## Use %*% for matrix multiplication
A%*%A

## Dot product
t(v)%*%v

## Euclidean norm
norm(v, type="2")

## Transpose
t(v)

## Inverse
inv(A)

## Eigenvalues
ev_A <- eigen(B)
A_values <- ev_A$values
A_vectors <- ev_A$vectors





