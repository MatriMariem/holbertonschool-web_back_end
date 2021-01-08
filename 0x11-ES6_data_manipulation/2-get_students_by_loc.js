export default function getStudentsByLocation(students, city) {
  if (Array.isArray(students) === false) {
    return [];
  }
  return students.filter((x) => x.location === city);
}
