console.log("Welcome to Holberton School, what is your name?");
process.stdin.on('data', (d) => {
  console.log(`Your name is: ${d.toString().trim()}`);

})
process.stdin.on('end', () => {
  console.log("This important software is now closing");
  process.exit();
});
