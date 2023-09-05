function sendPlantInfo(event) {
    event.preventDefault();

    var plantBedWidth = document.getElementById("plantBedWidth").value;
    var plantBedWidthUnit = document.getElementById("plantBedWidthUnit").value;
    var plantBedLength = document.getElementById("plantBedLength").value;
    var plantBedLengthUnit = document.getElementById("plantBedLengthUnit").value;
    var plantBedNumber = document.getElementById("plantBedNumber").value;
    var plantBedDepth = document.getElementById("plantBedDepth").value;
    var plantBedDepthUnit = document.getElementById("plantBedDepthUnit").value;


    jQuery.ajax({

        url: "/processPlantInfo",
        type: 'POST',
        data: {
            'plantBedWidth': plantBedWidth, 'plantBedWidthUnit': plantBedWidthUnit, 'plantBedLength': plantBedLength,
            'plantBedLengthUnit': plantBedLengthUnit, 'plantBedNumber': plantBedNumber,
            'plantBedDepth':plantBedDepth, 'plantBedDepthUnit':plantBedDepthUnit
        },
        success: function (response) {
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

            var pumpCalculationTable = document.getElementById("plantCalculationTable");
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
        error: function (error) {
            console.log(error);
            //TODO: In the future, pose the error message
        }
    }
    );



}