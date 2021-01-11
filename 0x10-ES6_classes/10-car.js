export default class Car {
  constructor(brand, motor, color) {
    // if (typeof brand !== 'string' || typeof motor !== 'string' || typeof color !== 'string') {
    //   throw TypeError('parameters must be strings');
    // }
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }
    cloneCar() {
      return new Car();
    }
}
