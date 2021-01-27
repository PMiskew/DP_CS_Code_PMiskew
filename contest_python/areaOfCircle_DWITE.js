x1 = 4
y1 = 2
x2 = 2
y2 = 8

r = Math.pow((y2 - y1)*(y2 - y1) + (x2 - x1)*(x2 - x1),1/2)

a = 3.14159*r*r

/*
a = a*1000
a = Math.round(a)
a = a/1000
console.log(a)
*/
a = a.toFixed(3)
console.log(a)
