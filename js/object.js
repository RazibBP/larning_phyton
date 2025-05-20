const car  = {
    name: "BMW",
    model: "volel",
    weght: "600kg",
    color : "white",
    start: function(name) {
        console.log(name + "Driver is sart this car.")
    },
    running: function(){
        console.log("car is running to the road.")
    },
    end: function(){
        console.log("Deiver is stop the car and jurnney is end.")
    },
    
};
car.start("Bmw car");
car.running();
car.end();


