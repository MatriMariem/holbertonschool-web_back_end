import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photoval;
  let userval;
  try {
    photoval = await uploadPhoto();
  } catch (e) {
    photoval = null;
  }
  try {
    userval = await createUser();
  } catch (e) {
    userval = null;
  }
  return { photo: photoval, user: userval };
}
