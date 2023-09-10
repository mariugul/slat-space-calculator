import math
from enum import Enum


class Units(Enum):
    MILLIMETER = "mm"
    PIECES = "pcs"
    METER = "m"
    PERCENT = "%"
    KRONER = "kr"


class SlatCalculator:
    class DefaultValues(Enum):
        RANGE_FACTOR: float = 0.4
        MIN_NR_SLATS: int = 2

    def __init__(
        self,
        range_factor_is_optional: bool = True,
        slat_length_is_optional: bool = True,
        slat_price_is_optional: bool = True,
    ):
        self.slat_width = self._get_valid_slat_width()
        self.base_width = self._get_valid_base_width()

        # Read input for range factor
        if range_factor_is_optional:
            self.range_factor: float | None = self._get_valid_input(
                "Enter space in a fraction of slat width (0.33 - 0.5): ", float, True
            )

            # In the case where you don't want to specify range factor and click "enter", set to default

            if self.range_factor is None:
                self.range_factor = self.DefaultValues.RANGE_FACTOR.value

        else:
            self.range_factor: float = self.DefaultValues.RANGE_FACTOR.value

        self.slat_length = None
        self.slat_price = None
        show_more_options = self._get_valid_input(
            "Show more options (y/n): ", str, True
        )
        if show_more_options in ["y", "Y"]:
            self.slat_length: float | None = self._get_valid_input(
                "(Optional) Enter the slat length (mm): ",
                float,
                slat_length_is_optional,
            )

            if self.slat_length is not None:
                self.slat_price: float | None = self._get_valid_input(
                    "(Optional) Enter the price of one slat (kroner): ",
                    float,
                    slat_price_is_optional,
                )

        self._run()

    def _get_valid_base_width(self):
        min_required_width = self.DefaultValues.MIN_NR_SLATS.value * self.slat_width

        while True:
            user_input = self._get_valid_input(
                f"Enter the base width (must be >= {min_required_width} mm): ", float
            )

            if user_input >= min_required_width:
                return user_input

            # Provide a clear error message
            print(
                f"Error: Base width must be >= {min_required_width} mm. Please try again."
            )

    def _get_valid_slat_width(self):
        min_required_width = 0

        while True:
            user_input = self._get_valid_input(
                f"Enter the slat width (must be >= {min_required_width} mm): ", float
            )

            if user_input > min_required_width:
                return user_input

            # Provide a clear error message
            print(
                f"Error: Slat width must be > {min_required_width} mm. Please try again."
            )

    def _calculate_slat_range(self):
        desired_space = self._calculate_desired_space()
        num_slats = self._calculate_num_slats(desired_space)
        actual_space = self._calculate_actual_space(num_slats)
        total_slat_length = self._calculate_total_slat_length(num_slats)

        return num_slats, actual_space, total_slat_length

    def _calculate_desired_space(self):
        return self.range_factor * self.slat_width

    def _calculate_num_slats(self, desired_space):
        return math.ceil(self.base_width / (self.slat_width + desired_space))

    def _calculate_actual_space(self, num_slats: int):
        if num_slats < 2:
            raise ValueError(f"Need at least 2 slats to calculate space between.")

        return (self.base_width - (num_slats * self.slat_width)) / (num_slats - 1)

    def _calculate_total_slat_length(self, num_slats):
        return num_slats * self.slat_length

    def _run(self):
        desired_space = self._calculate_desired_space()
        num_slats = self._calculate_num_slats(desired_space)
        actual_space = round(self._calculate_actual_space(num_slats), 2)

        if self.slat_length is not None:
            total_slat_length = self._calculate_total_slat_length(num_slats)
            # Convert total_slat_length to meters
            total_slat_length_meters = round(total_slat_length / 1000)

            if self.slat_price is not None:
                total_cost = round(self.slat_price * total_slat_length_meters)

        print()  # newline
        self._print_info("Base Width", self.base_width, Units.MILLIMETER)
        self._print_info("Slat Width", self.slat_width, Units.MILLIMETER)
        self._print_info("Number of Slats", num_slats, Units.PIECES)
        self._print_info("Space Between Slats", actual_space, Units.MILLIMETER)
        self._print_info(
            "Space Factor",
            round((actual_space / self.slat_width) * 100, 2),
            Units.PERCENT,
        )

        if self.slat_length:
            self._print_info("Total Slat Length", total_slat_length_meters, Units.METER)

            if self.slat_price:
                self._print_info("Cost of Slats", total_cost, Units.KRONER)

    def _get_valid_input(self, prompt: str, data_type: type, optional=False):
        while True:
            try:
                user_input = input(prompt)
                if (
                    not user_input.strip()
                ):  # Check if the input is empty after stripping whitespace
                    if optional:
                        return None

                if data_type is float:
                    # Replace "," with "." to handle both decimal separators
                    user_input = user_input.replace(",", ".")

                converted_value = data_type(user_input)
                return converted_value  # Return the valid value
            except ValueError as ve:
                expected_type = data_type.__name__
                actual_type = type(user_input).__name__
                error_message = f"Invalid input type {actual_type}. Please enter a {expected_type} type."
                if not optional:
                    print(error_message)

    def _print_info(self, label: str, value: str, unit: Units):
        print(f"{label:<24} {value: <5} {unit.value}")


if __name__ == "__main__":
    calculator = SlatCalculator()
