// let newcases = {}
// let i = 0
// Object.keys(cases).forEach(key => {
//     if (i % 5 == 0) {
//         newcases[key] = cases[key]
//     }
//     i++;
// })

// test = () => {
//     chart.destroy()
//     chart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 2,
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             },
//             interaction: {
//                 mode: 'nearest'
//             }
//         }
//     }
// })
// }

newcases = {}
let chartCases = ''
let chartDeaths = ''
let canvasCases = ''
let ctxCases = ''
let canvasDeaths = ''
let ctxDeaths = ''

let cases30d = document.querySelector('#cases30d')
let cases90d = document.querySelector('#cases90d')
let cases180d = document.querySelector('#cases180d')
let casesalld = document.querySelector('#casesalld')

let deaths30d = document.querySelector('#deaths30d')
let deaths90d = document.querySelector('#deaths90d')
let deaths180d = document.querySelector('#deaths180d')
let deathsalld = document.querySelector('#deathsalld')

if (history != 'no_data') {
    canvasCases = document.querySelector('#canvas-cases')
    ctxCases = canvasCases.getContext('2d')
    canvasDeaths = document.querySelector('#canvas-deaths')
    ctxDeaths = canvasDeaths.getContext('2d')
    chartCases = new Chart(ctxCases, {
    type: 'line',
    data: {
        labels: Object.keys(history.timeline.cases),
        datasets: [{
            label: 'Случаев заражения',
            data: Object.values(history.timeline.cases),
            borderWidth: 2,
            pointRadius: 0,
            backgroundColor: 'rgb(180, 0, 0)',
            borderColor: 'rgb(180, 0, 0)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
    })
    chartDeaths = new Chart(ctxDeaths, {
    type: 'line',
    data: {
        labels: Object.keys(history.timeline.deaths),
        datasets: [{
            label: 'Смертей',
            data: Object.values(history.timeline.deaths),
            borderWidth: 2,
            pointRadius: 0,
            backgroundColor: 'rgb(0, 0, 0)',
            borderColor: 'rgb(0, 0, 0)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
    })
}

let countryListItem = document.querySelector('.country-list')
let searchBar = document.querySelector('#search')
let countryChoiceItem = document.querySelector('.country-choice')

function toggleCountryChoice() {
    if (countryChoiceItem.classList.contains('disabled')) {
        countryChoiceItem.classList.remove('disabled')
    } else {
        countryChoiceItem.classList.add('disabled')
    }
}

function searchUpdate() {
    countryListItem.innerHTML = ''
    let val = searchBar.value.toLowerCase()
    let newobj = {}
    Object.keys(countries).forEach(key => {
        if (countries[key].toLowerCase().includes(val)) {
            let a = document.createElement('a')
            a.innerText = countries[key]
            a.href = key.toLowerCase()
            countryListItem.appendChild(a)
        }
    });

}

function graphCases(num, id) {
    cases30d.classList.remove('active')
    cases90d.classList.remove('active')
    cases180d.classList.remove('active')
    casesalld.classList.remove('active')
    document.querySelector('#' + id).classList.add('active')
    if (num != 'all') {
        thiscases = Object.keys(history.timeline.cases)
        thiscases = thiscases.slice(thiscases.length - num)
        thiscasesdict = {}
        thiscases.forEach(key => {
            thiscasesdict[key] = history.timeline.cases[key]
        })
    } else {
        thiscasesdict = history.timeline.cases
    }
    chartCases.destroy()
    chartCases = new Chart(ctxCases, {
    type: 'line',
    data: {
        labels: Object.keys(thiscasesdict),
        datasets: [{
            label: 'Случаев заражения',
            data: Object.values(thiscasesdict),
            borderWidth: 2,
            pointRadius: 0,
            backgroundColor: 'rgb(180, 0, 0)',
            borderColor: 'rgb(180, 0, 0)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: false
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
})
}

function graphDeaths(num, id) {
    deaths30d.classList.remove('active')
    deaths90d.classList.remove('active')
    deaths180d.classList.remove('active')
    deathsalld.classList.remove('active')
    document.querySelector('#' + id).classList.add('active')
    if (num != 'all') {
        thiscases = Object.keys(history.timeline.deaths)
        thiscases = thiscases.slice(thiscases.length - num)
        thiscasesdict = {}
        thiscases.forEach(key => {
            thiscasesdict[key] = history.timeline.deaths[key]
        })
    } else {
        thiscasesdict = history.timeline.deaths
    }
    chartDeaths.destroy()
    chartDeaths = new Chart(ctxDeaths, {
    type: 'line',
    data: {
        labels: Object.keys(thiscasesdict),
        datasets: [{
            label: 'Смертей',
            data: Object.values(thiscasesdict),
            borderWidth: 2,
            pointRadius: 0,
            backgroundColor: 'rgb(0, 0, 0)',
            borderColor: 'rgb(0, 0, 0)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: false
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
    })
}

let canvasTopCases = document.querySelector("#top-cases")
let ctxTopCases = canvasTopCases.getContext('2d')
let chartTopCases = new Chart(ctxTopCases, {
    type: 'bar',
    data: {
        labels: Object.keys(topCases),
        datasets: [{
            data: Object.values(topCases),
            borderWidth: 0,
            backgroundColor: ['#7F1D1D', '#991B1B', '#B91C1C', '#DC2626', '#EF4444', '#F87171', '#FCA5A5', '#FECACA', '#FEE2E2', '#FEF2F2']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
    })

let canvasTopDeaths = document.querySelector('#top-deaths')
let ctxTopDeaths = canvasTopDeaths.getContext('2d')
let chartTopDeaths = new Chart(ctxTopDeaths, {
    type: 'bar',
    data: {
        labels: Object.keys(topDeaths),
        datasets: [{
            data: Object.values(topDeaths),
            borderWidth: 0,
            backgroundColor: ['#171717', '#262626', '#404040', '#525252', '#737373', '#A3A3A3', '#D4D4D4', '#E5E5E5', '#F5F5F5', '#FAFAFA']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: false,
            label: true
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
    })