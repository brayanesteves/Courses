let x_pos = [];
let y_pos = [];

/**
 * Grado de colsión de nuestra línea
 * 
 * w = Es el grado de lineación de la línea (La inclinación)
 * b (bias ó sesgo) = Es el punto del 0
 */
let w;
let b;

/**
 * Rango de aprendizaje 
 * Es la cantidad de movimiento de grado de inclinación
 * Ejemplo: 0.5 (50%)
 */
const learningRate = 0.5;

/**
 * 
 */
const optimizer = tf.train.sgd(learningRate);

/**
 * (Es una función interna de P5.js)
 */
function setup() {
    createCanvas(400, 400);
    background(0);
    /**
     * Tensores
     * w = Va a ser un tensor variable, porque se va a estar moviendo
     */
    w = tf.variable(tf.scalar(random(1)));
    b = tf.variable(tf.scalar(random(1)));
}

/**
 * Formula que va a estar prediciendo nuestro punto
 * ¿Que va a predecir? Va a descubrir 'x' y va a entregar 'y'
 */
function predecir(x) {
    const xs = tf.tensor1d(x);
    /**
     * Formula
     * y = w * x + b
     */
    const ys = xs.mul(w).add(b);
    return ys;
}

/**
 * Cuando hacemos click
 * (Es una función interna de P5.js)
 * Lo que vamos es dibujar el punto en donde estamos clickeando
 */
function mousePressed() {
    /**
     * map(), mapea la posición de 'x'
     */
    let x = map(mouseX, 0, width, 0, 1);
    let y = map(mouseY, 0, height, 1, 0);

    x_pos.push(x);
    y_pos.push(y);
}

/**
 * Constantemente esta dibujando
 */
function draw() {
    background(0);
    stroke(255);
    strokeWeight(8);

    /**
     * Escala inversa
     */
    for (var i = 0; i < x_pos.length; i++) {
        /**
         * Operación inversa
         */
        let px = map(x_pos[i], 0, 1, 0, width);
        let py = map(y_pos[i], 0, 1, height, 0);

        point(px, py);
    }
    tf.tidy(() => {
        if(x_pos.length > 0) {
            /**
             * ys = Es el tipo tensor
             */
            const ys = tf.tensor1d(y_pos);
            /**
             * Con esta función predecir(x_pos) estamos dibujando una línea aleatoria, con la relación a
             * la posición 'x_pos', ahora a esa línea que acabamos de dibujar, le vamos a restar la posición en
             * 'ys' sub(ys), lo mque estamos realizando con 'square()' lo estamos elevando al cuadrado y al final
             * realizamos un 'mean()' que es media y lo que ocurre es obtener todos los resultados, lo sumamos y 
             * calculamos la media, la idea es minimizarla
             */
            optimizer.minimize(() => predecir(x_pos).sub(ys).square().mean());            
        }
    });
    /**
     * Obtener el valor de 'y' y minimizarlo
     * tidy() realiza los calculos y resultados que calculó 
     * 'optimizer.minimize(() => predecir(x_pos).sub(ys).square().mean());'
     */
    let y_predecida = tf.tidy(() => predecir([0, 1]));
    let val_y_predecida = y_predecida.dataSync();
    /**
     * Limpiamos tensores
     */
    y_predecida.dispose();
    
    let x1 = map(0, 0, 1, 0, width);
    let x2 = map(1, 0, 1, 0, width);

    let y1 = map(val_y_predecida[0], 0, 1, height, 0);
    let y2 = map(val_y_predecida[1], 0, 1, height, 0);

    line(x1, y1, x2, y2);
}