import { sayHello } from "./quiz.mjs";

try {
  sayHello("Patrick");

  sayHello();

  sayHello(1, 2);

  sayHello("Patrick", "Hill");
} catch (e) {
  console.log(e);
}
