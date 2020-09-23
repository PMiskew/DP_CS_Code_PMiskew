function scaleElementsA(a, b) {

    for (i = 0; i < b.length; i = i + 1) {
        b[i] = b[i] * a;
    }
    
}

function scaleElementsB(a, b) {
    c = []
    for (i = 0; i < b.length; i = i + 1) {
        c.push(b[i] * a);
    }

    return c;
    
}


function addStringsSmallLarge(a, b) {
   
    result = a + b;

    if (a.length > b.length) {
        result = b + a;
    }
    
    return result;
}