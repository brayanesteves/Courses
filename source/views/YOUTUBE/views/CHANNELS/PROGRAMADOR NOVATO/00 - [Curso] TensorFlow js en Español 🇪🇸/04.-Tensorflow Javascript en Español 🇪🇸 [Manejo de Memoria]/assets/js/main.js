/**
 * Función de p5.js de bucle infinito
 */
function draw() {
    
    const tensor3d = document.getElementById("tensor3d");
    
    const val = [];
    for (var i = 0; i < 30; i++) {
        val[i] = Math.random(0, 100) * 100;
    }
    tf.tidy(() => {
        /**
         * [5, 3, 2] = 5 Registros, 3 Filas y 2 Columnas
         */
        const tens = tf.tensor3d(val, [5, 3, 2], "int32");
        
        //tens.print();
        //tensor3d.innerHTML = tens + " en 'int32'";
        /*console.log(tens.data());
        tens.data().then(function (res) {
            console.log(res);
            console.log(res[2]);
        });
        console.log(tens.dataSync())*/
        
        //tensor3d.innerHTML += "<br>" + tens.data() + " en 'int32'";
        
        //const x = tf.variable(tf.tensor([1, 2, 3]));
        //x.print();
        //x.assign(tf.tensor([4, 5, 6]));
        //x.print();
        
        const a = tf.tensor2d([[1, 2, -3], [4, 0, -2]]);
        const b = tf.tensor2d([[3, 1], [2, 4], [-1, 5]]);
        const mul = tf.matMul(a, b);
    });
    //tens.dispose();
    //a.dispose();
    //b.dispose();
    //x.dispose();
    //mul.dispose();
    console.log(tf.memory().numTensors);

}