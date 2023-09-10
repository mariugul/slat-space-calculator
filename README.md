# Slat Calculator

This Python script calculates the number of slats, the space between them, and other related values for a given base width and slat width. It's especially useful for planning slat installations on walls, doors or what not to put a slat on.

The calculator operates under the assumption of positioning one slat at each extremity of a given width. For example, if you have a wall with a width of 100cm and you're using slats that are 10cm wide, the calculation involves placing one slat at the far left and another at the far right, then evenly distributing the remaining space between them.


Due to this rationale, it's not particularly meaningful to perform calculations with fewer than three slats, as there would be no space to distribute. Nevertheless, the script does accommodate cases with only two slats, provided that the inputted base width exceeds twice the width of a single slat.

## Usage

To use the Slat Calculator, simply run the script using Python 3:

```bash
python slat_calculator.py
```

The script will prompt you for various inputs, including the slat width, base width, and optionally, the slat length and slat price.

## Input Parameters

* **Slat Width (mm):** Enter the width of each slat in millimeters. It must be greater than or equal to 0 mm.

* **Base Width (mm):** Enter the total width of the base where the slats will be installed. It must be greater than or equal to the product of the minimum number of slats (2) and the slat width.

* **Space Factor (optional):** This factor determines the space between slats as a fraction of the slat width. The default value is 0.4, but you can customize it by entering a different value between 0.33 and 0.5.

* **Show more options (optional):** You can choose to provide additional information, such as the slat length and the price of one slat. This is useful for calculating the total cost of slats.

* **Slat Length (optional):** If you choose to provide this, enter the length of each slat in millimeters.

* **Price of One Slat (optional):** If you choose to provide this, enter the price of one slat in kroner.

The script will then calculate and display the following information:

* Number of Slats: The calculated number of slats required to cover the base width.

* Space Between Slats (mm): The actual space between slats, taking into account the space factor.

* Space Factor (%): The space factor as a percentage of the slat width.

* Total Slat Length (m): If you provided the slat length, this will display the total length of all slats in meters.

* Cost of Slats (kr): If you provided the slat price, this will display the estimated cost of all slats.

## Requirements
Python 3

## License
This script is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed. See the LICENSE file for details.

## Author
Marius - Software/Electronics Engineer
