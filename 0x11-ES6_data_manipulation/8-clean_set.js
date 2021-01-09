export default function cleanSet(set, startString) {
  const list = [];
  if (startString === '') {
    return '';
  }
  for (const x of set) {
    if (x.startsWith(startString)) {
      list.push(x.slice(startString.length));
    }
  }
  return list.join('-');
}
