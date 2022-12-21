#include <stdio.h>
#include <math.h>

// Define a structure to represent an arc
struct Arc {
  double radius;
  double angle;
};

// Function to calculate the area of an arc
double calcArcArea(struct Arc arc) {
  double area;
  area = 0.5 * arc.radius * arc.radius * arc.angle;
  return area;
}

int main() {
  // Declare an arc with radius 10cm and angle 180 degrees
  struct Arc arc = {10, 180};

  // Calculate the area of the arc
  double area = calcArcArea(arc);
  printf("The area of the arc is %.2lf cm^2\n", area);

  return 0;
}
