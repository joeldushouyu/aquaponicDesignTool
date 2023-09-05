

from typing import List, Tuple
# note: all unit are in SI standard
def fish_number_to_fish_tank_size(number_of_fish:float, fish_kg_at_mature:float=3.0)->Tuple[float, float]:
    """
    Calculate fish tank size base on given fish number and weight

    In page 89 of the book, the author recommended 40-80 liters of water for each kg of fish.
    
    Parameters
    ----------
    number_of_fish : float
        Number of fish
    fish_kg_at_mature : float, optional
        Weight of fish when it is matured. By default assume to be 3 kg.

    Returns
    -------
    Tuple[float, float]
        The min, max tank size in liter
    """

    # in page 89 of the book
    # it says that 40-80 liters for each 1 kg of fish. 
    # if the weight of matured fish is not given, it assume to be 3 kg
    
    
    total_fish_weight = (number_of_fish*fish_kg_at_mature)
    
    return ( 40*total_fish_weight, 80*total_fish_weight )

def fish_tank_size_to_fish_number(tank_size_in_liter:float, fish_kg_at_mature:float=3)->Tuple[int, int]:
    """
    Calculate fish number base on tank size.

    In page 89 of the book, the author recommended 40-80 liters of water for each kg of fish.

    Parameters
    ----------
    tank_size_in_liter : float
        The volume of fish tank.
    fish_kg_at_mature: float, optional
        Weight of fish when it is matured. Byt default assume to be 3 kg.
    
    Returns
    -------
    Tuple[int, int]
        The min, max fish number in the fish tank
    """
    return ( round((tank_size_in_liter/80)/fish_kg_at_mature ), round((tank_size_in_liter/40)/fish_kg_at_mature )  )
    
    
    
def plant_bed_surface_area_to_fish_number(plant_bed_surface_area_in_m2:float, fish_kg_at_mature:float=3)->int:
    """
    Calculate fish number base on plant bed surface area.
    
    In page 89 of the book, the author recommended 0.1m^2 for every 0.5 Kg of fish.

    Parameters
    ----------
    plant_bed_surface_area_in_m2 : float
        Plant bed total surface area.
    fish_kg_at_mature: float, optional
        Weight of fish when it is matured. Byt default assume to be 3 kg

    Returns
    -------
    int
        Number of fish.
    """
    
    correspond_fish_weight =  (plant_bed_surface_area_in_m2/0.1)/2

    return round(correspond_fish_weight/fish_kg_at_mature)

def fish_number_to_plant_bed_surface_area(number_of_fish:int, fish_kg_at_mature:float=3)->float:
    """
    Calculate plant bed surface area base on fish number.

    In page 89 of the book, the author recommended 0.1m^2 for every 0.5 Kg of fish.
    
    Parameters
    ----------
    number_of_fish : int
        Number of fish
    fish_kg_at_mature : float, optional
        Weight of fish when it is matured. Byt default assume to be 3 kg.

    Returns
    -------
    float
        The min, max surface area of plant bed.
    """
    
    total_fish_weight = number_of_fish * fish_kg_at_mature
    
    return (total_fish_weight*2 ) *0.1


def fish_tank_size_to_plant_bed_volume(fish_tank_size:float)->Tuple[float, float]:
    """
    Calculate plant bed volume on fish tank size

    In page 73 and 75 of the book, it says that it is recommended 1:1(plant bed volume):(fish tank size), 
    but 2:1 ratio is also acceptable. The conversion factor is 1000 liters to every cubic meter
    
    Parameters
    ----------
    fish_tank_size : float
        Volume of fish tank, in liters.

    Returns
    -------
    Tuple[float, float]
        The min, max total surface area of plant bed, in m^3
    """
    

    
    return (fish_tank_size /1000, (fish_tank_size*2)/1000)
def plant_bed_volume_to_fish_tank(plant_bed_volume: float) -> Tuple[float, float]:
    """
    Calculate fish tank size base on total plant volume.
    
    
    In page 73 and 75 of the book, it says that it is recommended 1:1(plant bed volume):(fish tank size), 
    but 2:1 ratio is also acceptable. The conversion factor is 1000 liters to every cubic meter
    

    Parameters
    ----------
    plant_bed_volume : float
        _description_

    Returns
    -------
    Tuple[float, float]
        The min, max fish tank size, in liters.
    """
    
    return ( (plant_bed_volume/2)*1000, plant_bed_volume*1000)

def effective_flow_rate_to_fish_tank(effective_flow_rate: float)->float:
    """
    Calculate the min, max of both fish tank size and plant bed surface base on the flow rate(flow rate of water after consider head heigth)

    On page 107, it suggested the pump need to cycle size of fish tank every hour

    Parameters
    ----------
    effective_flow_rate : float
        Effective flow rate of water in the system, after taking into consideration that head height affect the flow rate of pump.

    Returns
    -------
    float:
        Size of fish_tank
    """
    return effective_flow_rate
    
def fish_tank_to_effective_flow_rate(fish_tank_size: float)->float:
    """
    Calculate required flow rate of system base on fish tank

    Parameters
    ----------
    fish_tank_size : float
        Fish tank size in liter.

    Returns
    -------
    float
        Flow rate of water in system, in Liter/Hour
    """
    
    return fish_tank_size


def estimate_max_flow_rate_by_oversize(effective_flow_rate:float)->Tuple[float,float]:
    """
    Opposite to estimate_effective_flow_rate_by_oversize();

    Parameters
    ----------
    effective_flow_rate : float
        Effective output flow rate from pump into the syste

    Returns
    -------
    Tuple[float,float]
        The min, max of max flow rate from water pump.
    """
    return (effective_flow_rate*1.2, effective_flow_rate*1.3)
def estimate_effective_flow_rate_by_oversize(max_flow_rate: float)->Tuple[float, float]:
    """
    Estimate the effective output flow rate from pump into the system

    In page 93, it give the rule of oversize your final pump by 20% to 100%
    Parameters
    ----------
    max_flow_rate : float
        Max flow rate of pump at height = 0

    Returns
    -------
    Tuple[float, float]
        The height that the pump need to pump up.
    """
    
    return (max_flow_rate*0.7, max_flow_rate*0.8)

def estimate_effective_flow_rate_at_certain_height(max_flow_rate:float, max_height:float, desired_height:float) ->float:
    """
    Estimate the effective output flow rate of pump at certain height

    Estimate the output flow rate by doing a linear interpolation. 
    
    Parameters
    ----------
    max_flow_rate : float
        Max flow rate of pump at height = 0
    max_height : float
        Max height the pump can pump.
    desired_height: float
        The height that the pump need to pump up.

    Returns
    -------
    float
        The estimate flow rate at "desired_height"
    """
    
    
    slope = (max_flow_rate-0)/(0-max_height)
    
    
    estimate_flow_rate = desired_height*slope + max_flow_rate
    return estimate_flow_rate    