//PF-Exer-9
noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=((seatingCapacityTakeOff+seatingCapacityLanded)*2)*((seatingCapacityTakeOff-noOfFlightsTakeOff)+(seatingCapacityLanded-seatingCapacityTakeOff))
console.log(totalCookies)	
