export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, value] of array.entries()) {
    /* eslint-disable */
    array[idx] = appendString + value;
    /* eslint-enable */
  }

  return array;
}
