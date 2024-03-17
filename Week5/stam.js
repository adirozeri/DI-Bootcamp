console.log('To be or not to be'.indexOf('To'));
console.log('To be or not to be'.indexOf(' '));
console.log('To be or not to be'.indexOf('o', 2));
console.log('To be or not to be'.indexOf('be', 4));
console.log('To be or not to be'.indexOf('to'));
console.log('To be or not to be'.indexOf('B'));
console.log('To be or not to be'.indexOf('', 9));

string = "A quick brown fox" //string to be split
array_of_strings = string.split(" ") //The split() function 

console.log(string) //note that the split function doesn't change the original string
console.log(array_of_strings)

string = "A quick brown fox" //string to be split
array_of_strings = string.split("") //The split() function 

console.log(string) //note that the split function doesn't change the original string
console.log(array_of_strings)


var day = 2;   //change and try with different values

switch (day) {
    case 1:      //if day = 1
        console.log("Monday");
        break;
    case 2:      //if day = 2
        console.log("Tuesday");
        break;
    case 3:      //if day = 3
        console.log("Wednesday");
        break;
    case 4:      //if day = 4
        console.log("Thursday");
        break;
    case 5:      //if day = 5
        console.log("Friday");
    case 6:      //if day = 6
        console.log("Saturday");
    case 7:      //if day = 7
        console.log("Sunday");
        break;
    default:    //if day doesn't match any of above
        console.log("Invalid");
}

