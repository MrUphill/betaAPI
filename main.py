from fastapi import FastAPI
app = FastAPI(title="beatAPI")

def calc_heartbeat_tanaka(age):
    maxhr = 208 - 0.7 * age
    return (round(maxhr))


def calc_bmr(sex: str, age: int, weight: int):
    if sex == "female":
        if age >= 18 and age <= 29:
            return (14.8 * weight + 487)
        elif age >= 30 and age <= 59:
            return (8.3 * weight + 846)
    elif sex == "male":
        if age >= 18 and age <= 29:
            return (15.1 * weight + 692)
        elif age >= 30 and age <= 59:
            return (11.5 * weight + 873)

@app.get("/heartbeat/{sex}")
def read_heartbeat(sex: str, age: int):
    if sex == "female":
        return {"max_heartbeat": 226 - (1.0 * age)}
    if sex == "male":
        return {"max_heartbeat": 223 - (0.9 * age)}
        
@app.get("/heartbeat/tanaka/")
def read_tanaka_heartbeat(age: int):
    maxheartbeat = calc_heartbeat_tanaka(age)
    return {"descripton": "Calculation of max heartbeat with tanaka procedure.",
            "age": age,
            "max_heartbeat": maxheartbeat,
            "zones": [
                    {   "id": "zone1", 
                        "min": maxheartbeat * 0.5, "max": maxheartbeat * 0.6},
            {"id": "zone2", "min": maxheartbeat * 0.6, "max": maxheartbeat * 0.7},
            {"id": "zone3", "min": maxheartbeat * 0.7, "max": maxheartbeat * 0.8},
            {"id": "zone4", "min": maxheartbeat * 0.8, "max": maxheartbeat * 0.9},
            {"id": "zone5", "min": maxheartbeat * 0.9, "max": maxheartbeat}
            ]
            }

@app.get("/bmr/{sex}")
def read_bmr(sex: str, weight: int, age: int):
    if age < 18 or age > 59 or weight < 1:
        return {"ERROR": "Invalid Input",
            "sex":sex,
            "weight":weight,
            "age":age}

    bmr = calc_bmr(sex, age, weight)
    if sex == "female":
        return {"sex": sex,
                "age": age,
                "weight": weight,
                "bmr":  bmr,
                "inactive": 1.4 * bmr,
                "midactive": 1.6 * bmr,
                "highactive": 1.8 * bmr,
                "nutrion": {"carbs":{
                                "lowIntensityMin": weight * 3,
                                "lowIntensityMax": weight * 5,
                                "moderateIntensityMin": weight * 5,
                                "moderateIntensityMax": weight * 7,
                                "highIntensityMin": weight * 6,
                                "highIntensityMax": weight * 10,
                                "exthighIntensityMin": weight * 8,
                                "exthighIntensityMax": weight * 12
                                },
                                
                            "protein":{"minProtein": weight * 1.4,
                                        "maxProtein": weight * 1.8}                   
                            
                        
                                                          
            }}
    if sex == "male":
        return {"sex": sex,
                "age": age,
                "weight": weight,
                "bmr":bmr,
                "inactive": 1.4 * bmr,
                "midactive": 1.7 * bmr,
                "highactive": 1.9 * bmr,
                    "nutrion": {"carbs":{
                                    "lowIntensityMin": weight * 3,
                                    "lowIntensityMax": weight * 5,
                                    "moderateIntensityMin": weight * 5,
                                    "moderateIntensityMax": weight * 7,
                                    "highIntensityMin": weight * 6,
                                    "highIntensityMax": weight * 10,
                                "exthighIntensityMin": weight * 8,
                                "exthighIntensityMax": weight * 12
                                },
                                
                                "protein":{"minProtein": weight * 1.4,
                                            "maxProtein": weight * 1.8}                   
                            
                        
                                                          
                }}

    
    return {"ERROR": "Invalid Input",
            "sex":sex,
            "weight":weight,
            "age":age}

