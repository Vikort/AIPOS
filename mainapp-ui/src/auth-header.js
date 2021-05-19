export default function authHeader() {
  const user = localStorage.getItem('access');

  if (user) {
    return { "Content-Type": 'application/json', Authorization: 'Bearer ' + user};
  } else {
    return {};
  }
}