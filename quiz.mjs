export function sayHello(firstName, lastName) {
  if (!firstName) throw "You must supply the first name parameter";

  if (!lastName) throw "You must supply the last name parameter";

  if (typeof firstName != "string") throw "First Name Must Be A String";

  if (typeof lastName != "string") throw "Last Name Must Be A String";

  return `Hello ${firstName} ${lastName}!  How are you?`;
}
