const tensor = document.getElementById("tensor");
// Mostrar por consola
tf.tensor([1, 2, 3, 4]).print();
console.log(tf.tensor([1, 2, 3, 4]));

tf.tensor([[1, 2], [3, 4]]).print();
console.log(tf.tensor([[1, 2], [3, 4]]));

tf.tensor([[1.5, 2], [3, 4]]).print();
console.log(tf.tensor([[1.5, 2], [3, 4]]));

tf.tensor([[1.5, 2], [3, 4]], null, "int32").print();
console.log(tf.tensor([[1.5, 2], [3, 4]], null, "int32"));

tf.tensor([1, 2, 3, 4], [2, 2]).print();
console.log(tf.tensor([1, 2, 3, 4], [2, 2]));
// Mostrar en HTML
tensor.innerHTML = tf.tensor([1, 2, 3, 4]);
tensor.innerHTML += "<br>" + tf.tensor([[1, 2], [3, 4]]);
tensor.innerHTML += "<br>" + tf.tensor([[1.5, 2], [3, 4]]);
tensor.innerHTML += "<br>" + tf.tensor([[1.5, 2], [3, 4]], null, "int32") + " es 'int32'";
tensor.innerHTML += "<br>" + tf.tensor([1, 2, 3, 4], [2, 2]);

const scalar = document.getElementById("scalar");

tf.scalar(3.14).print();
console.log(tf.scalar(3.14));
scalar.innerHTML = tf.scalar(3.14);

tf.tensor(3.14).print();
console.log(tf.tensor(3.14));
scalar.innerHTML += "<br>" + tf.tensor(3.14);

const tensor1d = document.getElementById("tensor1d");

tf.tensor1d([1, 2, 3]).print();
console.log(tf.tensor1d([1, 2, 3]));
tensor1d.innerHTML = tf.tensor1d([1, 2, 3]);

const tensor3d = document.getElementById("tensor3d");

const val = [];
for (var i = 0; i < 30; i++) {
    val[i] = Math.random(0, 100);
}
/**
 * [5, 3, 2] = 5 Registros, 3 Filas y 2 Columnas
 */
tf.tensor3d(val, [5, 3, 2]).print();
console.log(tf.tensor3d(val, [5, 3, 2]));
tensor3d.innerHTML = tf.tensor3d(val, [5, 3, 2]);