const modelo = tf.sequential();
/**
 * Es una capa densa
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

modelo.add(oculta);

const salida = tf.layers.dense({
    // 1 Nodo
    units: 1, 
    activation: 'sigmoid',
});

modelo.add(salida);

/**
 * Optimizador, es una función que detecta que vaya
 * sgd (Estocastica de gradiente descendiente)
 */
const sgdOpciones = tf.train.sgd(0.1);

modelo.compile({
    optimizer: sgdOpciones,
    /**
     * Evita que nuestra perdida sea negativa
     */
    loss: tf.losses.meanSquaredError
});