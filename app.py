from flask import Flask, render_template, request, jsonify
from calcuationAlgorithm import *
from utility import *
app = Flask(__name__, static_url_path="/static", template_folder="templates")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    data = request.form.get('data')
    # process the data using Python code
    result = int(data) * 2
    print(data)
    print("hello wssorld")
    return str(result)


@app.route('/processPumpInfo', methods=['POST'])
def processPumpInfo():
    data = request.form

    print(data)

    # try to calculate the data that received
    try:

        head_height = float(data["headHeight"])
        if (data["pumpType"] == "Generic Pump"):

            max_flow_rate = float(data["pumpMaxFlowRate"])
            max_flow_rate_unit = data["pumpMaxFlowRateUnit"]
            if (max_flow_rate_unit == GallonPerHour):
                max_flow_rate = gallon_to_liter(max_flow_rate)
            elif (max_flow_rate_unit == LiterPerHour):
                pass
            else:
                raise ValueError("Unknow flow Rate Unit")

            max_flow_height = float(data["pumpMaxFlowHeight"])
            max_flow_height_unit = data["pumpMaxFlowHeightUnit"]
            if max_flow_height_unit == Inch:
                max_flow_height = inch_to_meter(max_flow_height)
            elif max_flow_height_unit == Meter:
                pass
            else:
                raise ValueError("Unknown max height unit")

            effective_flow_rate = estimate_effective_flow_rate_at_certain_height(
                max_flow_rate, max_flow_height, head_height)
            fish_tank_size = effective_flow_rate_to_fish_tank(
                effective_flow_rate)

            # NOTE: assume mature fish weighted about 3kg
            fish_number_min, fish_number_max = fish_tank_size_to_fish_number(
                fish_tank_size, 3)

            # NOTE: assume mature fish weighted about 3kg
            plant_bed_surface_min = fish_number_to_plant_bed_surface_area(
                fish_number_min, 3)
            plant_bed_surface_max = fish_number_to_plant_bed_surface_area(
                fish_number_max, 3)

            plant_bed_volume_min, plant_bed_volume_max = fish_tank_size_to_plant_bed_volume(
                fish_tank_size)
            print("retunring")
            return jsonify({"fishTankSizeMin": round(fish_tank_size, 2), "fishTankSizeMax": round(fish_tank_size, 2),
                            "fishNumberMin": round(fish_number_min, 2), "fishNumberMax": round(fish_number_max, 2),
                            "plantBedSurfaceAreaMin": round(plant_bed_surface_min, 2), "plantBedSurfaceAreaMax": round(plant_bed_surface_max, 2),
                            "plantBedVolumeMin": round(plant_bed_volume_min, 2), "plantBedVolumeMax": round(plant_bed_volume_max,2),
                            "flowRateFromPumpMin": round(max_flow_rate, 2), "flowRateFromPumpMax": round(max_flow_rate, 2)})
        else:
            # TODO: add special, know pump info into system
            pass
    except Exception as e:
        # TODO: what if bad data?
        pass


@app.route("/processPlantInfo", methods=["POST"])
def processPlantInfo():

    data = request.form
    print(data)

    try:
        plant_bed_width = float(data["plantBedWidth"])
        plant_bed_width_unit = data["plantBedWidthUnit"]
        plant_bed_length = float(data["plantBedLength"])
        plant_bed_length_unit = (data["plantBedLengthUnit"])
        plant_bed_number = int(data["plantBedNumber"])
        plant_bed_depth = float(data["plantBedDepth"])
        plant_bed_depth_unit = data["plantBedDepthUnit"]
        if plant_bed_width_unit == Inch:
            plant_bed_width = inch_to_meter(plant_bed_width)
        elif plant_bed_width_unit == Meter:
            pass
        else:
            raise ValueError("Unknown unit for plant bed width")

        if plant_bed_length_unit == Inch:
            plant_bed_length = inch_to_meter(plant_bed_length)
        elif plant_bed_length_unit == Meter:
            pass
        else:
            raise ValueError("unknown unit for plant bed length")

        if plant_bed_depth_unit == Inch:
            plant_bed_depth = inch_to_meter(plant_bed_depth)
        elif plant_bed_depth_unit == Meter:
            pass
        else:
            raise ValueError("unknown unit for plant bed depth")
        
        total_plant_bed_surface_area = plant_bed_number * \
            plant_bed_length * plant_bed_width

        total_plant_bed_volume = total_plant_bed_surface_area * plant_bed_depth
        fish_number = plant_bed_surface_area_to_fish_number(
            total_plant_bed_surface_area)

        # NOTE: assume fish is mature at 3 kg
        res1, res2, = fish_number_to_fish_tank_size(fish_number, 3)

        # NOTE: consider using the

        res3, res4 = plant_bed_volume_to_fish_tank(total_plant_bed_volume)
        fish_tank_size_min = min(res1, res2, res3, res4)
        fish_tank_size_max = max(res1, res2, res3, res4)

   

        # flow rate
        effective_flow_rate_min = fish_tank_to_effective_flow_rate(
            fish_tank_size_min)
        effective_flow_rate_max = fish_tank_to_effective_flow_rate(
            fish_tank_size_max)

        res1, res2 = estimate_max_flow_rate_by_oversize(
            effective_flow_rate_min)
        res3, res4 = estimate_max_flow_rate_by_oversize(
            effective_flow_rate_max)

        max_pump_flow_rate_min = min(res1, res2, res3, res4)
        max_pump_flow_rate_max = max(res1, res2, res3, res4)
        return jsonify({"fishTankSizeMin": round(fish_tank_size_min, 2), "fishTankSizeMax": round(fish_tank_size_max, 2),
                        "fishNumberMin": round(fish_number, 2), "fishNumberMax": round(fish_number, 2),
                        "plantBedSurfaceAreaMin": round(total_plant_bed_surface_area, 2), "plantBedSurfaceAreaMax": round(total_plant_bed_surface_area, 2),
                        "plantBedVolumeMin": round(total_plant_bed_volume, 2), "plantBedVolumeMax": round(total_plant_bed_volume,2),
                        "flowRateFromPumpMin": round(max_pump_flow_rate_min, 2), "flowRateFromPumpMax": round(max_pump_flow_rate_max, 2)})
    except Exception as e:
        # TODO: add error message
        pass


@app.route("/processFishInfo",  methods=['POST'])
def processFishInfo():

    data = request.form

    print(data)

    try:
        if data["fishTankSize"] != "":

            fish_tank_size = float(data["fishTankSize"])
            fish_tank_size_unit = data["fishTankSizeUnit"]
            if fish_tank_size_unit == Gallon:
                fish_tank_size = gallon_to_liter(fish_tank_size)
            elif fish_tank_size_unit == Liter:
                pass
            else:
                raise ValueError("Unknown unit for fish tank size")

            # Note: assume fish matured is 3 kg
            fish_number_min, fish_number_max = fish_tank_size_to_fish_number(fish_tank_size, 3)\

            print(fish_number_min, fish_number_max)
            plant_bed_surface_min = fish_number_to_plant_bed_surface_area(
                fish_number_min, 3)
            plant_bed_surface_max = fish_number_to_plant_bed_surface_area(
                fish_number_max, 3)

            plant_bed_volume_min, plant_bed_volume_max = fish_tank_size_to_plant_bed_volume(
                fish_tank_size)
            effective_flow_rate = fish_tank_to_effective_flow_rate(
                fish_tank_size)
            max_pump_flow_rate_min, max_pump_flow_rate_max = estimate_max_flow_rate_by_oversize(
                effective_flow_rate)

            return jsonify({"fishTankSizeMin": round(fish_tank_size, 2), "fishTankSizeMax": round(fish_tank_size, 2),
                            "fishNumberMin": round(fish_number_min, 2), "fishNumberMax": round(fish_number_max, 2),
                            "plantBedSurfaceAreaMin": round(plant_bed_surface_min, 2), "plantBedSurfaceAreaMax": round(plant_bed_surface_max, 2),
                            "plantBedVolumeMin": round(plant_bed_volume_min, 2), "plantBedVolumeMax": round(plant_bed_volume_max,2),
                            "flowRateFromPumpMin": round(max_pump_flow_rate_min, 2), "flowRateFromPumpMax": round(max_pump_flow_rate_max, 2)})
        else:
            print("In else statement")
            # TODO: load fish specifcc
            pass
    except Exception as e:
        # TODO: add special warning message or feedback message
        pass


if __name__ == '__main__':
    app.run(debug=True)
