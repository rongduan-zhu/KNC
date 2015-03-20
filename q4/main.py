#!/usr/bin/env python
import json
from math import atan, degrees

def solver(j):
    b_direction = j["BeamAngle"]
    skeletons = j["Skeletons"]
    valid_skeletons = []

    for skeleton in skeletons:
        position = skeleton["Position"]
        adjacent = float(position["Z"])
        opposite = float(position["X"])

        radius = degrees(atan(opposite / adjacent))

        if radius >= b_direction - 10.0 and radius <= b_direction + 10.0:
            valid_skeletons.append(skeleton["ID"])

    return valid_skeletons

if __name__ == '__main__':
    f = open("Xbox,-go-home_InputForSubmission_3.txt")
    for line in f:
        loaded_json = json.loads(line)
        valid_skeletons = solver(loaded_json)
        print json.dumps({"Sources": valid_skeletons}, separators=(',',':'))
