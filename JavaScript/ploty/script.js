const getData = () => {
    return Math.random();
}


var trace1 = {
    // x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    y: [getData()],
    type: 'line',
    line: {
        shape: 'spline',
        color: '#faa',
    },
};

var layout = {
    dragmode: 'pan',
    margin: {
        l: 10,
        r: 10,
        b: 20,
        t: 20,
    },
    xaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: true,
        autotick: true,
        showticklabels: false
    },
    yaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        showticklabels: true
    }
};

var data = [trace1];

var config = {
    responsive: true,
    displaylogo: false,
    scrollZoom: true,
    displayModeBar: false,
}

Plotly.newPlot('chart', data, layout, config);




let count = 0;



setInterval(() => {
    Plotly.extendTraces('chart', { y:[ [getData()] ] }, [0])
    count++;

    if (count > 20) {
        Plotly.relayout('chart', {
            xaxis: {
                range: [count-20, count],
                autorange: false,
                showgrid: false,
                zeroline: false,
                showline: true,
                autotick: true,
                showticklabels: false
            }
        });
    }
}, 2000)