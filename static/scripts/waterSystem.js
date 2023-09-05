const pumpType = document.getElementById("pumpType");
const pumpExtraInfo = document.getElementById("pumpExtraInfo")



function sendPumpData(event){
    event.preventDefault();
    var pumpType = document.getElementById("pumpType").value;
    var headHeight = document.getElementById("headHeight").value;
    var headHeightUnit = document.getElementById("headHeightUnit").value;
    var pumpMaxFlowRate = document.getElementById("pumpMaxFlowRate").value;
    var pumpMaxFlowRateUnit = document.getElementById("pumpMaxFlowRateUnit").value;
    var pumpMaxFlowHeight = document.getElementById("pumpMaxFlowHeight").value;
    var pumpMaxFlowHeightUnit = document.getElementById("pumpMaxFlowHeightUnit").value;
    var powerConsumption = document.getElementById("powerConsumption").value;

    jQuery.ajax({

        url:"/processPumpInfo",
        type: 'POST',
        data: {'pumpType': pumpType, 'headHeight':headHeight, 'headHeightUnit':headHeightUnit,
                'pumpMaxFlowRate':pumpMaxFlowRate, 'pumpMaxFlowRateUnit':pumpMaxFlowRateUnit, 
                'pumpMaxFlowHeight':pumpMaxFlowHeight, 'pumpMaxFlowHeightUnit':pumpMaxFlowHeightUnit, 
                'powerConsumption':powerConsumption},
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

            var pumpCalculationTable = document.getElementById("pumpCalculationTable");
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
function hidePumpExtraInfo(){


    pumpExtraInfo.style.display= "none"
}
function showPumpExtraInfo(){
  
    pumpExtraInfo.style.display="";
}




// initialize the state
if(pumpType.value==="Generic Pump"){
    showPumpExtraInfo();
}else{
    hidePumpExtraInfo();
}

// add event listener to monitor when user change pumpType
pumpType.addEventListener("change", function(){
    const pumpSelected = pumpType.value;
    if(pumpSelected ==="Generic Pump" ){
        showPumpExtraInfo();
    }else{
        hidePumpExtraInfo();
    }

});


