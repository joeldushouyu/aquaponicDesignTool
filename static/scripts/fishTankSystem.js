const fishType = document.getElementById("fishType");
const fishNumber = document.getElementById("fishNumber");
const fishMatureWeightDiv = document.getElementById("fishMatureWeightDiv");
const fishTankSize = document.getElementById("fishTankSize");
const fishMatureWeight = document.getElementById("fishMatureWeight");
const fishTankSizeUnit = document.getElementById("fishTankSizeUnit");



function hideFishMatureWeight(){
    fishMatureWeightDiv.style.display="none";
}
function showFishMatureWeight(){
    fishMatureWeightDiv.style.display=""; // set it to default
}



function hideFishInfo(){

    fishType.value="";
    fishType.disabled=true;
    fishType.classList.add('disabled-input');

    fishNumber.value="";
    fishNumber.disabled=true;
    fishNumber.classList.add("disabled");

    fishMatureWeight.value = "";
    fishMatureWeight.disable=true;
    fishMatureWeight.classList.add("disabled");
}
function showFishInfo(){

    fishType.disabled=false;
    fishType.classList.remove('disabled-input');

    fishNumber.disabled=false;
    fishNumber.classList.remove("disabled");

    fishMatureWeight.disable=false;
    fishMatureWeight.classList.remove("disabled");
}


function hideFishTankInfo(){
    fishTankSize.value="";
    fishTankSize.disabled=true;
    fishTankSize.classList.add('disabled-input');

    fishTankSizeUnit.value=""
    fishTankSizeUnit.disabled=true;
    fishTankSizeUnit.classList.add('disabled-input');
}

function showFishTankInfo(){

    fishTankSize.disabled=false;
    fishTankSize.classList.remove('disabled-input');

    fishTankSizeUnit.disabled=false;
    fishTankSizeUnit.classList.remove('disabled-input');
}

// add event listener
fishType.addEventListener("change", function(){

    const fishTypeSelected = fishType.value;
    if(fishTypeSelected === "Other Fish"){
        showFishMatureWeight();
    }else{
        hideFishMatureWeight();
    }
});




// 
fishType.addEventListener("click",function(){

    hideFishTankInfo();
});
fishNumber.addEventListener("click",function(){
    hideFishTankInfo();
});
fishMatureWeight.addEventListener("click", function(){
    hideFishTankInfo();
})


fishTankSize.addEventListener("click", function(){
    hideFishInfo();
})
fishTankSizeUnit.addEventListener("click", function(){
    hideFishInfo();
})

function resetFishInfoData(){
    showFishInfo();
    showFishTankInfo();
}


//initialize the default statue
if(fishType.value === "Other Fish"){
    showFishMatureWeight();
}else{
    hideFishMatureWeight();
}


function  sendFishInfo(event){
    event.preventDefault();

    var fishType = document.getElementById("fishType").value;
    var fishNumber = document.getElementById("fishNumber").value;
    var fishMatureWeight = document.getElementById("fishMatureWeight").value;
    var fishTankSize = document.getElementById("fishTankSize").value;
    var fishTankSizeUnit = document.getElementById("fishTankSizeUnit").value;
    jQuery.ajax({

        url:"/processFishInfo",
        type: 'POST',
        data: {'fishType': fishType, 'fishNumber':fishNumber, 'fishMatureWeight':fishMatureWeight,
                'fishTankSize':fishTankSize, 'fishTankSizeUnit':fishTankSizeUnit,},
        success: function(response){
            var minFishTankSize = response.fishTankSizeMin;
            var maxFishTankSize = response.fishTankSizeMax;
            var fishNumberMin = response.fishNumberMin;
            var fishNumberMax = response.fishNumberMax;
            var minPlantBedSurface = response.plantBedSurfaceAreaMin;
            var maxPlantBedSurface = response.plantBedSurfaceAreaMax;
            var plantBedVolumeMin = response.plantBedVolumeMin;
            var plantBedVolumeMax = response.plantBedVolumeMax;
            var minPumpFlowRate = response.flowRateFromPumpMin;
            var maxPumpFlowRate = response.flowRateFromPumpMax;

            var pumpCalculationTable = document.getElementById("fishCalculationTable");
            var rows = pumpCalculationTable.querySelectorAll("tbody tr");
            rows[0].querySelectorAll('td')[0].textContent=minFishTankSize;
            rows[0].querySelectorAll('td')[2].textContent=maxFishTankSize;

            rows[1].querySelectorAll('td')[0].textContent=fishNumberMin;
            rows[1].querySelectorAll('td')[2].textContent=fishNumberMax;

            rows[2].querySelectorAll('td')[0].textContent=minPlantBedSurface;
            rows[2].querySelectorAll('td')[2].textContent=maxPlantBedSurface;

            rows[3].querySelectorAll('td')[0].textContent=plantBedVolumeMin;
            rows[3].querySelectorAll('td')[2].textContent=plantBedVolumeMax;

            rows[4].querySelectorAll('td')[0].textContent=minPumpFlowRate;
            rows[4].querySelectorAll('td')[2].textContent=maxPumpFlowRate;

        },  
        error: function(error){
            console.log(error);
            //TODO: In the future, pose the error message
        }

    });


    
}  