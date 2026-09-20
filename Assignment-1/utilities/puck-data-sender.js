let isPressed = false;

// Watch the physical button state
setWatch(function(e) {
  isPressed = e.state; // e.state is true when pressed, false when released
}, BTN, { repeat: true, edge: "both", debounce: 50 });

Puck.accelOn();
Puck.on('accel', accel => {
  // Only send data out over Bluetooth while the button is actively held down
  if (isPressed) {
    if (accel && accel.acc) {
      x_g = (accel.acc.x / 41); //1G therefore 41
      y_g = (accel.acc.y / 41);
      z_g = (accel.acc.z / 41);
    }
    Bluetooth.println(`${x_g},${y_g},${z_g}`); //,${d.acc.y/8192},${d.acc.z/8192}
  }
});