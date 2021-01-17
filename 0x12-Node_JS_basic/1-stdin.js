console.log("Welcome to Holberton School, what is your name?");
process.stdin.on('data', (d) => {
  if (d.toString().trim() !== '') {
  process.stdout.write(`Your name is: ${d.toString().trim()}`);
} else {
  process.exit();
}
})
process.stdin.on('end', () => {
  console.log("\nThis important software is now closing");
  process.exit();
});
