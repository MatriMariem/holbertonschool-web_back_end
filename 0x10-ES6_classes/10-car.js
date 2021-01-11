export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const name = eval(this.constructor.name);
    console.log("heeeeeeyyyyy", typeof name);
    return new name();
  }
}
