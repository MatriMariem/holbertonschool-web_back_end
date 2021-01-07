import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';
export default function handleProfileSignup(firstName, lastName, fileName) {
  return [ {'status': 'fulfilled' , 'value': signUpUser(firstName, lastName).then((data) => data)}, {'status': 'rejected', 'value': uploadPhoto(fileName)}];
}
