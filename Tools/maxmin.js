//Before we begin
arr = [2,100,99]; //create an array if length 3
arr.max(...arr); //short hand to find max
arr.min(...arr); //short hand to find min


/*
1.  JS Specific - When sorting a list using the built in function it assumes
    that elements are strings.  This is really useful for alphabetical sorting
    needs. 
2.  Remeber arrays are reference types so if we sort a the passed parameter
    will remain sorted when done. 
*/
function findMaxConcern(a) {
    
    a = a.sort(function(a,b) {
        return a - b
    })
    console.log(a[a.length - 1])
    return a[a.length - 1]
    
}

arr = [100,1,2]
findMaxConcern(arr)

/*
This function takes an array and returns the largest value
*/
function findMax(a) {

    //Big Idea: When searching a list always set the value to an element
    //          in the list
    let max = a[0]

    for (i = 0; i < a.length; i = i + 1) {
        if (max < max[i]) {
            max = a[i]
        }

    }
    return max;

}

arr = [100,1,2]
findMax(arr)

