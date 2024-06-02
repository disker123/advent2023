def mapper(data: list): #version 2.0 now with less seg faults! Returns the map given a list of maps values
    seed_map = []
    for lines in data:
        val = lines.split()
        dest_start = int(val[0])
        source_start = int(val[1])
        increment = int(val[2]) #"increment" is really a rnage size so we need to subtract 1 when we return it
        seed_map.append((dest_start, source_start, source_start + (increment-1)))   #seed map is a list of tupples with the destination start, the source start, and source end
    return seed_map 

def solver(map: list, seed: int):   #finds and returns the destination value from a given seed and a given map
    for tupples in map:
        if(seed>=tupples[1] and seed<=tupples[2]):  #if the seed is in the one fo mapped ranges we will return it's mapped destination value
            return seed-tupples[1] + tupples[0]
    return seed #if the seed found no mapped ranges we return seed as the destination value


File = open("day5input.txt", "r")
data = File.readlines()


seeds = []
locations = []
for x in data[0].split()[1:]:   #create seeds list
    seeds.append(x)
for i in seeds:
    seed_to_soil = mapper(data[3:31])
    soil =  solver(seed_to_soil, int(i))
    print("soil is: ", soil)
    soil_to_fertilizer = mapper(data[33:43])
    fertilizer = solver(soil_to_fertilizer, soil)
    print("fertilizer is: ", fertilizer)
    ferilizer_to_water = mapper(data[45:54])
    water = solver(ferilizer_to_water, fertilizer)
    print("water is: ", water)
    water_to_light = mapper(data[56:79])
    light = solver(water_to_light, water)
    print("light is: ", light)
    light_to_temp = mapper(data[81:113])
    temp = solver(light_to_temp, light)
    print("temp is: ", temp)
    temp_to_humidity = mapper(data[115:160])
    humidity = solver(temp_to_humidity, temp)
    print("humidity is:", humidity)
    humidity_to_location = mapper(data[162:211])
    location = solver(humidity_to_location, humidity)
    print("location is: ", location)
    locations.append(location)
print("the smallest location value is", min(locations))
File.close()