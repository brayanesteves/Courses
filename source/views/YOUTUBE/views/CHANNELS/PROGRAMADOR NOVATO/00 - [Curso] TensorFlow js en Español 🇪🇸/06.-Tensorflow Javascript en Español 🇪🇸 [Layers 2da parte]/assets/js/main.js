const modelo = tf.sequential();
/**
 * Es una capa densa
 * Creamos una capa oculta
 */
const oculta = tf.layers.dense({
    // 4 Nodos
    units: 4,
    // Nodos de entradas
    inputShape: [2],
    /**
     * Función de activación
     */
    activation:'sigmoid'
});

// Ingresamos la capa oculta en el modelo
modelo.add(oculta);

// Creamos la capa de salida
const salida = tf.layers.dense({
    // 1 Nodo
    units: 1, 
    activation: 'sigmoid',
});

// Ingresamos la capa de salida en el modelo
modelo.add(salida);

/**
 * Optimizador, es una función que detecta que vaya
 * sgd (Estocastica de gradiente descendiente)
 */
// Creamos la opciones del 'SGD'
const sgdOpciones = tf.train.sgd(0.1);

// Compilamos el modelo
modelo.compile({
    // Le asignamos la optimización
    optimizer: sgdOpciones,
    /**
     * Evita que nuestra perdida sea negativa
     * Asignamos la forma de reducir la perdida
     */
    loss: tf.losses.meanSquaredError
});

// Datos que conocemos
const x1 = tf.tensor2d([[0, 0], [0.2, 0.2], [0.4, 0.4]]);
// Datos que NO conocemos
const x2 = tf.tensor2d([[0.1], [0.3], [0.5]]);

async function intento() {
    for (var i = 0; i < 100; i++) {
        /**
         * fit = Realiza los calculos
         * (x1, x2) Parametros de entradas
         * shuffle = Toma datos y realiza una especie de random, lo barajea
         * epochs = Son la cantidad de repeticiones
         */
        const respuesta = await modelo.fit(x1, x2, { shuffle: true, epochs: 100 });
        console.log(i + " - " + respuesta.history.loss[0]);
    }
}
//intento();
intento().then(() => {
    const salida_ = modelo.predict(x1);
    salida_.print();
});