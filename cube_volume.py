#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program calculates the volume of a cube


def cube_volume(length):
    # this function calculates the volume of a cube

    # process
    volume = length ** 3

    return volume


def main():
    # this function accepts inputs

    # input
    length_string = input("Enter cube length (cm): ")

    # process
    try:
        length = float(length_string)

        # call function
        cube_volume_value = cube_volume(length)
        if length < 0:
            print("\n{0} is a negative number, try again.".format(length_string))
        else:
            print("\nThe volume of the cube is {} cm³".format(cube_volume_value))

    except Exception:
        print("\n{} is an invalid input, try again.".format(length_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
